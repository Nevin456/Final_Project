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
import Main


class app_addition:


    def add_app():

        os.system('clear')


        global appname
        global bLoc
        global regpat


        bLoc = input("\nEnter Location of the Block File: ")
        if os.path.isfile(bLoc):
            print("Block Found!")
        else:
            print("Block not found! Please Try Again")
            app_addition.add_app()
        sDes = "/home/kali/Desktop/Cybernate/Regex_Addition/"
        appname = input(Fore.YELLOW+"Enter Application to be added: "+Fore.RESET)
        print("\n")
        regpat = input("Enter Regex Pattern: ")
        print("\n")
        print (regpat)

        regex_results = codecs.open((sDes)+"Results.txt ", "a+", encoding="utf-8")
        BLKSIZE = 16384
        print(Fore.LIGHTGREEN_EX+"\n\n"+appname+" Details Extracted: \n\n"+Fore.RESET)
        regex_results.write("Details Extracted: \n")
        global app_matchnum
        app_matchnum = 0
        with codecs.open(bLoc, 'r', encoding='utf-8', errors='ignore') as addreg:
            blk = addreg.read(BLKSIZE)
            while len(blk) > 0:       
                app_find = re.finditer(regpat, blk, re.MULTILINE)
                for app_matchNum, match in enumerate(app_find):
                    app_matchNum = app_matchNum + 1             
                    print("\n\nEntire Match {app_matchNum} found: {match}".format(app_matchNum = app_matchNum, match = match.group()))
                    regex_results.write("\nEntire Match {app_matchnum} found: {match}".format(app_matchnum = app_matchnum, match = match.group()))

                blk = addreg.read(BLKSIZE)
        addreg.close()
        regex_results.close()

    def returnHome():

        exit = input("\n\nPress Enter to Go back to the Home Screen\n")
        if quit == "":
            
            os.system('clear')
            Main.MainScreen.home()
        else:
            app_addition.returnHome()


app_addition.add_app()

    




    