from posixpath import basename
from colorama import Fore
from tqdm import tqdm
from PyInquirer import prompt
from PyInquirer import Separator
import os
import subprocess
import time
from time import process_time
import hashlib
import datetime
#import Analysis
import Main
#import Hashing


class Block_Extraction:

    def extraction_init():

        global devtype

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
        print(Fore.GREEN+"")
        devtype_answers = prompt(devtype_questions)
        print(Fore.RESET+"")


        if devtype_answers == {'device_select':'1. Physical Device'}:
            devtype = ("-d")

        elif devtype_answers == {'device_select':'2. Emulator'}:
            devtype = ('-e')
        elif devtype_answers == {'device_select':'Exit'} :
            os.system('clear') 

    
    def block_name():

        global bName
        global bloLoc

        print(Fore.YELLOW+"Available blocks that can be extracted "+Fore.RESET)
        print("______________________________________________________\n")
        time.sleep(2)
        os.system("adb shell ls /dev/block")
        print("\n\n")
        # subprocess.call("adb shell ls",shell=True)
        # subprocess.call("ls",shell=True)
        time.sleep(1)

        bName = input(Fore.YELLOW+"Enter required Block File Name: "+Fore.RESET)

        print(Fore.YELLOW+"Extraction Process Commencing"+Fore.RESET)
        print("__________________________________")

        bloLoc = input(Fore.YELLOW+"Enter the location where the block file should be extracted to"+Fore.RESET)
        
        print("Total Size to be Extracted (Bytes): ")
        os.system("adb shell blockdev --getsize /dev/block/"+bName)
        print("\n")
        os.system("adb "+devtype+" pull /dev/block/"+bName+" "+bloLoc+"")

        if os.path.isfile("/home/nevin/Desktop/Nev/New/"+bName):

            print(Fore.GREEN+"\n\nExtraction Completed!"+Fore.RESET)
        else:
            print(Fore.RED+"\n\nError!"+Fore.RESET)

    def block_PostExthashcheck():

        os.system('clear')

        global b_Destination

        b_Destination = bloLoc

        BLOCKSIZE = 16384
        start_time = process_time()
        global post_Exthash
        postExt_hash = hashlib.sha512()

        with open(b_Destination, 'rb') as postExt_hash:
            pre_blk = postExt_hash.read(BLOCKSIZE)
            while len(pre_blk) > 0:
                post_Exthash.update(pre_blk)
                post_Extblk = postExt_hash.read(BLOCKSIZE)
            postExt_hash.close()
            end_time = process_time()
            time = end_time - start_time
            timenow = datetime.datetime.now()
            timestat = timenow.strftime("%Y-%m-%d_%H-%M")

            pre_hashtxt = open((b_Destination.replace("\\","\\\\"))+"Hash_CheckSum-Pre_Analysis(" + str(timestat) + ").txt", "a")
            pre_hashtxt.write("Post-Extraction Hash Checksum SHA512: "+ post_Exthash.hexdigest())
            pre_hashtxt.write("\nPost-Extraction Time Elapsed: "+(str(time))+" seconds")

            print(Fore.YELLOW+"\nPost-Extraction Hash Checksum SHA512: "+Fore.RESET, post_Exthash.hexdigest())
            print(Fore.YELLOW+"Post-Extraction Time Elapsed: "+Fore.RESET, time, " seconds")
            print(Fore.BLUE+"\nHash Checksum(Post-Extraction) for the selected Block File is Generated \n"+Fore.RESET)
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


        if devtype_answers == {'proceed_select':'1. Yes'}:
            MainScreen.home()
            

        elif devtype_answers == {'device_select':'2. No, Exit to the Main Menu'}:
            MainScreen.home()
            


Block_Extraction.extraction_init()
Block_Extraction.block_name()
Block_Extraction.block_PostExthashcheck()






    

        









