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


class WitcherData:
    def __init__(self):
        self.geralt_health = 100
        self.current_quest = ""
        self.current_objective = ""
        self.near_monsters = []


def get_W3_data():

    return data

def loop_program(file):
    fp = open(file, 'r')
    while True:
        new_line = fp.readline()
        # from game the log message follow the convention [ChatMod]request:response
        if new_line.startswith(MOD_PREFIX):
            # return only the request:response string (croppping prefix)
            yield (new_line[len(MOD_PREFIX)+1:])
        else:
            time.sleep(0.1)


data = WitcherData()

def update_W3_data():
    if directory_found:
        for line in loop_program(log_file):
            # splitting on character ':' to have list [request,response]
            request, response = line.split(':')
            # print(request)
            # print(response)

            # check request (look in bot_helpers.ws)
            if request == "current_quest":
                # send whatever string to NLG using response as current quest
                print("The current quest is", response)  # TODO call NLG
                # update local data
                data.current_quest = response
            elif request == "current_objective":
                # send whatever string to NLG using response as current quest
                print("The current objective is", response)  # TODO call NLG
                # update local data
                data.current_objective = response
            elif request == "monsters":
                # monsters returns like name1,level;name2,level;
                monsters = response.split(";")
                # clear previous data
                data.near_monsters.clear()
                for m in monsters:
                    if m:
                        # split name,level
                        monster_name, monster_level = m.split(',')
                        # update data
                        data.near_monsters.append(
                            {"name": monster_name, "level": monster_level})
                        print(monster_name, monster_level)
                # TODO call NLG
if __name__ == "__main__":
    if directory_found:
        for line in loop_program(log_file):
            # splitting on character ':' to have list [request,response]
            request, response = line.split(':')
            # print(request)
            # print(response)

            # check request (look in bot_helpers.ws)
            if request == "current_quest":
                # send whatever string to NLG using response as current quest
                print("The current quest is", response)  # TODO call NLG
                # update local data
                data.current_quest = response
            elif request == "current_objective":
                # send whatever string to NLG using response as current quest
                print("The current objective is", response)  # TODO call NLG
                # update local data
                data.current_objective = response

            elif request == "geralt_health":
                # send whatever string to NLG using response as current quest
                print("Geralt's health is", response)  # TODO call NLG
                # update local data
                data.geralt_health = response

            elif request == "monsters":
                # monsters returns like name1,level;name2,level;
                monsters = response.split(";")
                # clear previous data
                data.near_monsters.clear()
                for m in monsters:
                    if m:
                        # split name,level
                        monster_name, monster_level = m.split(',')
                        # update data
                        data.near_monsters.append(
                            {"name": monster_name, "level": monster_level})
                        print(monster_name, monster_level)
