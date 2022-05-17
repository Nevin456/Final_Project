from posixpath import basename
import _hashlib
import hashlib
from secrets import choice
from colorama import Fore
from tqdm import tqdm
from PyInquirer import prompt
from PyInquirer import Separator
import os
import subprocess
import re
import time
from time import process_time
import hashlib
import codecs
import datetime
from Analysis import app_analysis
from Hashing import hashing
import Main
#import Analysis

#import Hashing


class Block_Extraction:

    def extraction_init():

        global devtype
        global devname

        os.system('clear')

        print(Fore.YELLOW+"Extraction of Non-Volatile Memory!"+Fore.RESET)
        time.sleep(1)

        print(Fore.YELLOW+"\n\nDetecting Android Debug Bridge Connections"+Fore.RESET)
        print("______________________________________________________\n")
        time.sleep(1)
        os.system("adb devices")
        print("\n")
        time.sleep(1)

        print(Fore.YELLOW+"Checking Root Status Android Device "+Fore.RESET)
        print("______________________________________________________\n")
        time.sleep(1)
        os.system("adb root")
        print("\n")
        time.sleep(1)

        devtype_questions = [
            {
                'type': 'list',
                'name': 'device_select',
                'message': 'Is this an emulator or a physical device?',
                'choices': [
                    Separator(),

                    '1. Physical Device',
                    '2. Emulator',


                    Separator(),
                    'Exit',
                ]
            }
        ]
        print(Fore.BLUE+"")
        devtype_answers = prompt(devtype_questions)
        print(Fore.RESET+"")

        if devtype_answers == {'device_select': '1. Physical Device'}:
            devtype = ("-d")

        elif devtype_answers == {'device_select': '2. Emulator'}:
            devtype = ('-e')
        elif devtype_answers == {'device_select': 'Exit'}:
            os.system('clear')
    

        devname = input(Fore.BLUE+"\nEnter the device id of the suspect device: "+Fore.RESET)
        os.system('clear')

    def block_name():

        global bName
        global bloLoc

        bloLoc = input(Fore.YELLOW+"Enter the location where the block file should be extracted to: "+Fore.RESET)
        try:
            if os.path.exists(bloLoc+"/"+devname):
                confirmation = [
                    {
                        'type': 'confirm',
                        'message': 'A folder with same device id exists? Do you want to use it anyway?',
                        'name': 'creation',
                        'default': True,
                        
                    },
                ]
                    
                choice = prompt(confirmation)
                if choice == {'creation': True}:
                    bloLoc=""+bloLoc+"/"+devname
            else:
                os.mkdir(bloLoc+"/"+devname)
                print("\nThe folder directory is created!")
        except FileNotFoundError:
            os.mkdir(bloLoc/devname)
            os.system('clear')

        print(Fore.YELLOW+"Available blocks that can be extracted "+Fore.RESET)
        print("______________________________________________________\n")
        time.sleep(2)
        os.system("adb shell ls /dev/block")
        print("\n\n")
        
        time.sleep(1)

        bName = input(Fore.YELLOW+"Enter required Block File Name: "+Fore.RESET)

        print(Fore.YELLOW+"Extraction Process Commencing"+Fore.RESET)
        print("__________________________________")

        

        print("Total Size to be Extracted (Bytes): ")
        os.system("adb shell blockdev --getsize /dev/block/"+bName)
        print("\n")
        os.system("adb "+devtype+" pull /dev/block/"+bName+" "+bloLoc+"")

        if os.path.isfile(bloLoc+"/"+bName):

            print(Fore.GREEN+"\n\nExtraction Completed!"+Fore.RESET)
        else:
            print(Fore.RED+"\n\nError!"+Fore.RESET)



    def block_PreExthashcheck():

        os.system('clear')

        """ global b_Location,s_Destination
        b_Location=(bloLoc+"/"+bName)
        s_Destination=(bloLoc+"/") """

        b_Location
        BLOCKSIZE = 16384
        start_time = process_time()
        global postExt_hash
        
        postExt_hash = hashlib.sha512()
        

        with open(b_Location,'rb') as postExt_hashfile:
            postExt_blk = postExt_hashfile.read(BLOCKSIZE)
            while len(postExt_blk) > 0:
                postExt_hash.update(postExt_blk)
                postExt_blk = postExt_hashfile.read(BLOCKSIZE)
            postExt_hashfile.close()
            end_time = process_time()
            time = end_time - start_time
            timenow = datetime.datetime.now()
            timestat = timenow.strftime("%Y-%m-%d_%H-%M")

            postExttxt = open((s_Destination.replace("\\","\\\\"))+"Hash_CheckSum-Post_Extraction(" + str(timestat) + ").txt", "a")
            postExttxt.write("Post Extraction Hash Checksum SHA512: "+ postExt_hash.hexdigest())
            postExttxt.write("\nPost Extraction Time Elapsed: "+(str(time))+" seconds")

            

            postExttxt1 = open((s_Destination.replace("\\","\\\\"))+"Hash_CheckSum-Post_Extraction.txt", "a")
            postExttxt1.write(postExt_hash.hexdigest())

            print(Fore.YELLOW+"\nPost Extraction Hash Checksum SHA512: "+Fore.RESET, postExt_hash.hexdigest())
            print(Fore.YELLOW+"Post Extraction Time Elapsed: "+Fore.RESET, time, " seconds")
            print(Fore.BLUE+"\nHash Checksum (Post-Extraction) for the selected Block File has been Generated \n"+Fore.RESET)
            print("\n")

            print("______________________________________________________\n")
            

    def block_PostExthashcheck():

        os.system('clear')

        global b_Location,s_Destination
        b_Location=(bloLoc+"/"+bName)
        s_Destination=(bloLoc+"/")

        BLOCKSIZE = 16384
        start_time = process_time()
        global postExt_hash
        
        postExt_hash = hashlib.sha512()
        

        with open(b_Location,'rb') as postExt_hashfile:
            postExt_blk = postExt_hashfile.read(BLOCKSIZE)
            while len(postExt_blk) > 0:
                postExt_hash.update(postExt_blk)
                postExt_blk = postExt_hashfile.read(BLOCKSIZE)
            postExt_hashfile.close()
            end_time = process_time()
            time = end_time - start_time
            timenow = datetime.datetime.now()
            timestat = timenow.strftime("%Y-%m-%d_%H-%M")

            postExttxt = open((s_Destination.replace("\\","\\\\"))+"Hash_CheckSum-Post_Extraction(" + str(timestat) + ").txt", "a")
            postExttxt.write("Post Extraction Hash Checksum SHA512: "+ postExt_hash.hexdigest())
            postExttxt.write("\nPost Extraction Time Elapsed: "+(str(time))+" seconds")

            

            postExttxt1 = open((s_Destination.replace("\\","\\\\"))+"Hash_CheckSum-Post_Extraction.txt", "a")
            postExttxt1.write(postExt_hash.hexdigest())

            print(Fore.YELLOW+"\nPost Extraction Hash Checksum SHA512: "+Fore.RESET, postExt_hash.hexdigest())
            print(Fore.YELLOW+"Post Extraction Time Elapsed: "+Fore.RESET, time, " seconds")
            print(Fore.BLUE+"\nHash Checksum (Post-Extraction) for the selected Block File has been Generated \n"+Fore.RESET)
            print("\n")

            print("______________________________________________________\n")

        proceed_questions = [
            {
                'type': 'list',
                'name': 'proceed_select',
                'message': 'Do you want to proceed to the Analysis Stage?',
                'choices': [
                    Separator(),

                    '1. Yes',
                    '2. No, Exit to the Main Menu',


                    Separator(),
                    'Exit',
                ]
            }
        ]
        print(Fore.GREEN+"")
        devtype_answers = prompt(proceed_questions)
        print(Fore.RESET+"")

        if devtype_answers == {'proceed_select': '1. Yes'}:
            app_analysis()

        elif devtype_answers == {'device_select': '2. No, Exit to the Main Menu'}:
            Main.MainScreen.home()
        

Block_Extraction.extraction_init()
Block_Extraction.block_name()
Block_Extraction.block_PostExthashcheck()






    

        









