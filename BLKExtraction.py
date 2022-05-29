from colorama import Fore
from tqdm import tqdm
from PyInquirer import prompt
from PyInquirer import Separator
import os
import time
import Main

class extractblk:

    def extraction_init():

        global devtype
        global devname

        os.system('clear')


        print(Fore.YELLOW+"\n\nDetecting Android Debug Bridge Connections"+Fore.RESET)
        print("______________________________________________________\n")
        time.sleep(1)
        os.system("adb devices")
        print("\n")
        time.sleep(1)

        print(Fore.YELLOW+"Checking Root Status of Android Device "+Fore.RESET)
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
                    bloLoc=(""+bloLoc+"/"+devname)
            else:
                os.mkdir(bloLoc+"/"+devname)
                bloLoc=(""+bloLoc+"/"+devname)
                print("\n\nThe folder directory is created!")
        except FileNotFoundError:
            os.mkdir(bloLoc+"/"+devname)
            bloLoc=(""+bloLoc+"/"+devname)
            os.system('clear')

        print(Fore.YELLOW+"Available blocks that can be extracted "+Fore.RESET)
        print("______________________________________________________\n")
        time.sleep(2)
        os.system("adb shell ls /dev/block")
        print("\n\n")
        
        

        bName = input(Fore.YELLOW+"Enter required Block File Name (bootdevice->userdata.img or vda/sda(0-1)): "+Fore.RESET)

        
        time.sleep(1)
        print(Fore.YELLOW+"Extraction Process Commencing"+Fore.RESET)
        print("__________________________________")

        

        print("Total Size to be Extracted (Bytes): ")
        os.system("adb shell blockdev --getsize /dev/block/"+bName)
        print("\n")
        os.system("adb "+devtype+" pull /dev/block/"+bName+" "+bloLoc+"")

        if os.path.isfile(bloLoc+"/"+bName):
            print(Fore.GREEN+"\n\nExtraction Completed!"+Fore.RESET)
        else:
            print(Fore.RED+"\n\nError in Extraction!"+Fore.RESET)


        """ proceed_questions = [
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
            import BLKAnalysis
            BLKAnalysis
        elif devtype_answers == {'device_select': '2. No, Exit to the Main Menu'}:
            extractblk.block_PostExthashcheck()
            extractblk.PreAnalysis_Compare() """

    """     def block_PostExthashcheck():

        b_Location=(bloLoc+"/"+bName)
        s_Destination=("/home/kali/Desktop/Cybernate/Report_Summary")

        BLOCKSIZE = 16384
        start_time = process_time()
        global postExt_hash
        postExt_hash = hashlib.sha512()
        global post1
        
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
            post1=hashlib.sha512("pos".encode("utf8")).hexdigest()

            postExttxt = open((b_Location.replace("\\","\\\\"))+devname+"(Hash_CheckSum-Post_Extraction).txt", "a")
            postExttxt.write(post1)
            print(Fore.YELLOW+"\nPost Extraction Hash Checksum SHA512: "+Fore.RESET, postExt_hash.hexdigest())
            print(Fore.YELLOW+"Post Extraction Time Elapsed: "+Fore.RESET, time, " seconds")
            print(Fore.BLUE+"\nHash Checksum (Post-Extraction) for the selected Block File has been Generated \n"+Fore.RESET)
            print("\n")

            print("______________________________________________________\n")

    def PreAnalysis_Compare():

        b_Location=(bloLoc+"/"+bName)
        postAnatxt=open((b_Location.replace("\\","\\\\"))+devname+"(Hash_CheckSum-Post_Extraction1).txt", "a")
        postAnatxt.write(post1)

        with open(bloLoc+"/"+bName+devname+"(Hash_CheckSum-Post_Extraction).txt")as f:
            postExt_hashtxt=f.readline
            #post1=hashlib.sha512("postExt_hash".encode("utf8")).hexdigest()

        with open(bloLoc+"/"+bName+devname+"(Hash_CheckSum-Post_Extraction1).txt")as d:
            preAnahashtxt=d.readline

        if postExt_hashtxt == preAnahashtxt:
            #repo_generation.write("\nHash Checksum Remains Identical after Analysis")
            print(Fore.CYAN+"\nHash Checksum Remains Identical after Analysis\n\n"+Fore.RESET)
        else:
            #repo_generation.write("\nHash Checksum DIFFERED after Analysis")
            print(Fore.CYAN+"\nHash Checksum DIFFERED after Analysis\n\n"+Fore.RESET)
            #repo_generation.write("\n\n\n------------------ Analysis Process Completed ------------------" """

    def returnHome():

        exit = input("\n\nPress Enter to Go back to the Home Screen\n")
        if exit == "":
            os.system('clear')
            Main.MainScreen.home()
        else:
            extractblk.returnHome()



extractblk.extraction_init()
extractblk.block_name()
extractblk.returnHome()   

