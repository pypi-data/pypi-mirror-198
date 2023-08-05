# MIT License

# Copyright (c) 2023 MatrixEditor

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

################################################################################
# ISU-Inspector::import
################################################################################
import os
import argparse
import zlib

from time import sleep
from io import UnsupportedOperation

from fsapi.isu.fsfs import FSFSFile
from fsapi.isu.model import (
    ISUInspector,
    ISUFileBuffer,

    get_instance
)
from fsapi.isu.inspectors import OtaIspector, MMI_HEADER_LENGTH

################################################################################
# ISU-Inspector::globals
################################################################################
__BANNER__ = """\
    ╦╔═╗╦ ╦   ╦┌┐┌┌─┐┌─┐┌─┐┌─┐┌┬┐┌─┐┬─┐
    ║╚═╗║ ║───║│││└─┐├─┘├┤ │   │ │ │├┬┘
    ╩╚═╝╚═╝   ╩┘└┘└─┘┴  └─┘└─┘ ┴ └─┘┴└─
───────────────────────────────────────────
"""

ALLOWED_SUFFIXES = ('isu.bin', 'ota.bin')

ERR_FATAL = 'ERROR - FATAL: '
ERR_INFO = 'ERROR - INFO: '

################################################################################
# ISU-Inspector::functions
################################################################################
def parse_header(fp: ISUFileBuffer, inspector: ISUInspector, root: FSFSFile = None,
                 verbose: bool = False) -> None:
    try: # read and print header
        header = inspector.get_header(buffer=fp, verbose=verbose)
        if header is not None and root is not None:
            root.append(FSFSFile('header', attributes={
                'size': header.size,
                'version': str(header.version),
                'customisation': str(header.customisation)
            }))
    except NotImplementedError as err:
        print(ERR_INFO, str(err))

    try: # read and print partitions
        partitions = inspector.get_partitions(fp, verbose=verbose)
        if partitions is not None and root is not None:
            p_e = FSFSFile('partitions', {'amount': len(partitions)})
            for partition in partitions:
                p_e.append(FSFSFile('partition', attributes={
                    'type': partition.entry_type,
                    'number': partition.partition,
                    'is_web_partition': partition.is_web_partition()
                }))
            root.append(p_e)
    except NotImplementedError as err:
        print(ERR_INFO, str(err))
    except UnsupportedOperation:
        pass

    try: # read and print uboot
        if isinstance(inspector, OtaIspector):
            config = inspector.get_uboot_config(fp, verbose=verbose)
            if config is not None and root is not None:
                # REVISIT: maybe iterate over mtdparts and add them
                # individually.
                p_e = FSFSFile('uboot', attributes=config)
                root.append(p_e)
    except NotImplementedError as err:
        print(ERR_INFO, str(err))
    except UnsupportedOperation:
        pass

    try: # read and print compression/decompression fields
        fields = inspector.get_compression_fields(fp, verbose=verbose)
        if fields is not None and root is not None:
            p_e = FSFSFile('FieldList', {})
            for field in fields:
                p_e.append(FSFSFile(field.name, {'size': field.size}))
            root.append(p_e)
    except NotImplementedError as err:
        print(ERR_INFO, str(err.args))
    except UnsupportedOperation:
        pass


def parse_directory_archive(fp: ISUFileBuffer, inspector: ISUInspector,
                            root: FSFSFile = None, verbose: bool = False):
    try: # read and print header
        fs_tree = inspector.get_fs_tree(fp, verbose=verbose)
        if fs_tree is not None:
            root.append(fs_tree)
    except (UnsupportedOperation, NotImplementedError) as e:
        print(ERR_FATAL, str(e))


def save_dir_entry(root: FSFSFile, buffer: bytes, path: str, start: int):
    name = root.get_attribute('name')
    if root.get_attribute('type') == 0x00: # file
        with open(path + name, 'wb') as res:
            off = start + root.get_attribute('offset')
            if root.get_attribute('compressed') == 'True':
                dc_data = zlib.decompress(buffer[off:off+root.get_attribute('compression_size')])
                res.write(dc_data)
            else:
                res.write(buffer[off:off+root.get_attribute('size')])
    else:
        if name == 'root':
            name = 'fsh1'
        try:
            os.mkdir(path + name)
        except OSError:
            pass

        for element in root:
            save_dir_entry(element, buffer, path + name + '/', start)


def extract_bytes(fp: ISUFileBuffer, root: FSFSFile, nspace: dict) -> None:
    name: str = root.get_attribute('path').split('/')[-1]
    if name.endswith(ALLOWED_SUFFIXES[0]) or name.endswith(ALLOWED_SUFFIXES[1]):
        name = name[:-8]

    path = root.get_attribute('path')
    if nspace['header']:
        try:
            with open('%s.header.bin' % path, 'wb') as ofp:
                ofp.write(fp.get_buffer()[:MMI_HEADER_LENGTH])
        except OSError:
            print('[i] Could not save header file to "%s.header.bin"' % path)

    if nspace['archive']:
        try:
            fsh = root.get_element('fsh1')
            if fsh is not None:
                dir_path = f'{path}.extracted/'
                if not os.path.exists(dir_path):
                    os.mkdir(dir_path)

                    for element in fsh:
                        save_dir_entry(element, fp.get_buffer(), dir_path, start=fsh.get_attribute('offset'))
                    
                    print('[+] Saved directory archive to "%s"' % dir_path)
        except OSError:
            print('[i] Could not save directory archive')

    if nspace['core']:
        size = -1
        for field in root.get_element('FieldList'):
            if field.tag == 'CompSize':
                size = field.get_attribute('size')

        index = fp.get_buffer().find(b'\x1B\x00\x55\xAA')
        if size != -1 and index != -1:
            try:
                with open('%s.core.bin' % path, 'wb') as ofp:
                    ofp.write(fp.get_buffer()[index:index+size])
            except OSError:
                print('[i] Could not save binary core to "%s.core.bin"' % path)


################################################################################
# ISU-Inspector::main
################################################################################
if __name__ == '__main__':
    # Parser-Args
    parser = argparse.ArgumentParser()
    parser.add_argument('-if', type=str, required=True,
        help="The input file (optional *.isu.bin or *.ota.bin extension)"
    )
    parser.add_argument('-of', type=str, required=False,
        help="The output file (Format: XML)."
    )
    parser.add_argument('--verbose', '-v', action='store_true', default=False,
        help="Prints useful information during the specified process."
    )
    parser.add_argument('--insp', '-I', type=str, required=False, default=None,
        help="Sets the ISUInspector descriptor, which will be used to retrieve\n\
        the inspector instance."
    )

    group_info = parser.add_argument_group("information gathering")
    group_info.add_argument('--header', '-H', action='store_true', default=False,
        help="Parses the header of the given file and extracts information."
    )
    group_info.add_argument('--archive', '-A', action='store_true', default=False,
        help="Parses the directory archive."
    )

    group_extract = parser.add_argument_group("extract data")
    group_extract.add_argument('-e', '--extract', action='store_true', default=False,
        help="Extract data (usually combined with other parameters)."
    )
    group_extract.add_argument('--core', '-C', action='store_true', default=False,
        help="Extract the compressed core partition source."
    )

    nspace = parser.parse_args().__dict__
    verbose = nspace['verbose']

    if verbose: print(__BANNER__)
    if 'if' not in nspace:
        print('[-] Input file not specified -> Quitting...')
        exit(1)

    ipath = nspace['if']
    opath = nspace['of'] if 'of' in nspace else None
    tree  = FSFSFile('isu', {'path': os.path.abspath(ipath)})

    try:
        fp = ISUFileBuffer(ipath)
    except OSError:
        print('[i] Could not open input file (%s)' % ipath)
        exit(1)

    if 'insp' in nspace and nspace['insp']:
        inspector = get_instance(nspace['insp'])
    else:
        inspector = get_instance(ipath.split(os.sep)[-1])

    if nspace['header']:
        parse_header(fp, inspector, tree, verbose)

    if nspace['archive']:
        parse_directory_archive(fp, inspector, tree, verbose)

    if opath and tree is not None:
        try:
            with open(opath, 'w') as ofp:
                ofp.write('<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>\n')
                ofp.write(tree.to_xml())

            if verbose: print('[i] Saved XML-output to', opath)
        except OSError:
            print('[i] Could not save output to file (%s)' % opath)

    if nspace['extract']:
        extract_bytes(fp, tree, nspace)
