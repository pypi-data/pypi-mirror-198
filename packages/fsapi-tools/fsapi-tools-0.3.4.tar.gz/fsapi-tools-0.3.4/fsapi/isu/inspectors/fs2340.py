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

from io import UnsupportedOperation

from fsapi.isu.ioutils import to_ui32, verify_skip, skip
from fsapi.isu.model import (
    ISUInspector,
    ISUFileBuffer,
    ISUHeader,
    
    set_inspector,
    
    ISU_MAGIC_BYTES
)
from fsapi.isu.product import FSCustomisation, FSVersion

__all__ = [
  'FS2340CUIInspector', 'FS2340MMIInspector'
]

@set_inspector('ir/cui/fs2340')
class FS2340CUIInspector(ISUInspector):

    def get_header(self, buffer: ISUFileBuffer, offset: int = 0, **kwgs) -> ISUHeader:
        verbose = 'verbose' in kwgs and kwgs['verbose']

        index, success = verify_skip(
        skip(buffer._file, offset, ISU_MAGIC_BYTES),
            "Malformed ISU-File",
            verbose
        )

        if not success: return None
        if verbose: print("[+] Analyzing ISU File header...")

        header = ISUHeader()
        header.size = to_ui32(buffer, index)

        if header.size != 124:
            if verbose: print("[-] Unknown header size: %d" % header.size)
            return header
        
        index += 4
        header.meos_version = to_ui32(buffer, index)
        if verbose:
            print("  - MeOS Version: %d" % (header.meos_version))

        fsv = FSVersion()
        fsc = FSCustomisation()

        index += 4
        index, fsv_name = self._get_header_name(buffer, index)
        index, fsc_name = self._get_header_name(buffer, index)

        fsv.loads(fsv_name)
        fsc.loads(fsc_name)
        if verbose:
            print("  - Version: '%s'" % str(fsv))
            print("     | SDK Version: %s" % (fsv.sdk_version))
            print("     | Revision: %s" % (fsv.revision))
            print("     | Branch: %s\n" % (fsv.branch))
            print("\n  - Customisation: '%s'" % str(fsc))
            print("     | DeviceType: %s" % ('internet radio' if fsc.device_type == 'ir' else fsc.device_type))
            print("     | Interface: %s" % ('multi media interface' if fsc.interface == 'mmi' else fsc.interface))
            print("     | Module: %s (version=%s)\n" % (fsc.get_module_name(), fsc.module_version))

        header.customisation = fsc
        header.version = fsv

        return header

    def _get_header_name(self, buffer: ISUFileBuffer, index: int) -> tuple:
        endpos = buffer._file.index(b" ", index)
        fsv_name = str(buffer[index:endpos], 'utf-8')
        
        index = endpos
        while buffer[index] == 0x20: index += 1
        return index, fsv_name
    
    def get_compression_fields(self, buffer: ISUFileBuffer, offset: int = 0, **kwgs) -> list:
        raise UnsupportedOperation("CUI-Files does not store compression fields in plain text")

    def get_fs_tree(self, buffer: ISUFileBuffer, offset: int = 0, **kwgs):
        raise UnsupportedOperation("CUI-Files does not store FSH1 in plain text")

@set_inspector('ir/mmi/fs2340')
class FS2340MMIInspector(FS2340CUIInspector):
  pass
