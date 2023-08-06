

""""""# start delvewheel patch
def _delvewheel_init_patch_1_3_4():
    import ctypes
    import os
    import sys
    libs_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'FastWARC.libs'))
    is_pyinstaller = getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS')
    load_order_filepath = os.path.join(libs_dir, '.load-order-FastWARC-0.14.3')
    if not is_pyinstaller or os.path.isfile(load_order_filepath):
        with open(os.path.join(libs_dir, '.load-order-FastWARC-0.14.3')) as file:
            load_order = file.read().split()
        for lib in load_order:
            lib_path = os.path.join(libs_dir, lib)
            if not is_pyinstaller or os.path.isfile(lib_path):
                ctypes.WinDLL(lib_path)


_delvewheel_init_patch_1_3_4()
del _delvewheel_init_patch_1_3_4
# end delvewheel patch

# Copyright 2021 Janek Bevendorff
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from .stream_io import FileStream, GZipStream, LZ4Stream
from .stream_io import FastWARCError, StreamError
from .warc import ArchiveIterator, WarcRecord, WarcRecordType
