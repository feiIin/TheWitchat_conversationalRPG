import time
import os

### CHECKING USER'S DOCUMENT DEFALULT FOLDER ####

import ctypes
from ctypes.wintypes import MAX_PATH
directory_found = False
LOG_WITCHER_PATH = "The Witcher 3\scriptslog.txt"
MOD_PREFIX = "[ChatMod]"
# using windows shell https://docs.microsoft.com/en-gb/windows/win32/api/_shell/
shell = ctypes.windll.shell32
buffer = ctypes.create_unicode_buffer(MAX_PATH + 1)
# window's shell function https://docs.microsoft.com/en-us/windows/win32/api/shlobj_core/nf-shlobj_core-shgetspecialfolderpathw
if shell.SHGetSpecialFolderPathW(None, buffer, 0x0005, False):
    documents_path = buffer.value
    log_file = os.path.join(documents_path, LOG_WITCHER_PATH)
    directory_found = True
else:
    print("Unable to Get Document folder")


def loop_program(file):
    fp = open(file, 'r')
    while True:
        new_line = fp.readline()
        if new_line.startswith(MOD_PREFIX):
            yield (new_line)
        else:
            time.sleep(0.1)


if __name__ == "__main__":
    if directory_found:
        for line in loop_program(log_file):
            print(line)
