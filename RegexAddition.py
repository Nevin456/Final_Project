import os
from tokenize import String
from PyInquirer import prompt
from PyInquirer import Separator
from colorama import Fore
import hashlib
#from Hashing import hashing
from time import process_time
import datetime
import re
import codecs

import regex


class app_addition:


    def add_app():

        os.system('clear')


        global appname
        global bLoc
        global regpat


        bLoc = "/home/nevin/Desktop/Blocks/dm-1"

        appname = input(Fore.YELLOW+"Enter Application to be added: "+Fore.RESET)
        print("\n")
        regpat = input(Fore.YELLOW+"Enter Regex Pattern for the Application:"+Fore.RESET)
        print("\n")

        regex_results = codecs.open((bLoc)+"Results.txt", "a+", encoding="utf-8")
        BLOCKSIZE = 16384
        print(Fore.LIGHTYELLOW_EX+"\n\n"+appname+" Details Extracted: \n\n"+Fore.RESET)
        regex_results.write("Details Extracted: \n\n")
        global app_matchNum
        app_matchNum = 0
        with codecs.open(bLoc, 'r', encoding='utf-8', errors='ignore') as y:
            blk = y.read(BLOCKSIZE)
            while len(blk) > 0:
                app_reg = regpat
                app_find = re.finditer(app_reg, blk, re.MULTILINE)
                for app_matchNum, match in enumerate(app_find):
                    app_matchNum = app_matchNum + 1
                    
                    print("\n\nEntire Match {app_matchNum} found: {match}".format(app_matchNum = app_matchNum, match = match.group()))
                    regex_results.write("\nEntire Match {app_matchnum} found: {match}".format(app_matchNum = app_matchNum, match = match.group()))
                    print("\n\nInstagram Sender ID (group {groupNum}) found: {group}".format(groupNum = 1, group = match.group(1)))
                    regex_results.write("\n\nInstagram Sender ID  (group {groupNum}) found: {group}".format(groupNum = 1, group = match.group(1)))
                    print("\n\nInstagram Message Sent: (group {groupNum}) found: {group}".format(groupNum = 2, group = match.group(2)))
                    regex_results.write("\n\nInstagram Message Sent (group {groupNum}) found: {group}".format(groupNum = 2, group = match.group(2)))
                    print("\n\nInstagram Receiver ID: (group {groupNum}) found: {group}".format(groupNum = 3, group = match.group(3)))
                    regex_results.write("\n\nInstagram Receiver ID (group {groupNum}) found: {group}".format(groupNum = 3, group = match.group(2)))
                    


                blk = y.read(BLOCKSIZE)
        y.close()
        regex_results.close()

app_addition.add_app()

    




    