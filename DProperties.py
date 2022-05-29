import os
from colorama import Fore
from colorama import Style
import time
from PyInquirer import prompt
from PyInquirer import Separator
import Main


class dev_Prop:

    def extraction_Devprop():

        os.system('clear')

        print(Fore.YELLOW+Style.BRIGHT +"Acquisition of Device Properties!"+Style.NORMAL+Fore.RESET)

        dprop_options = [
            {
                'type': 'list',
                'name': 'dprop_select',
                'message': 'Select the option you require?',
                'choices': [
                    Separator(),

                    '1. Device IMEI(International Mobile Equipment Identity) Number',


                    Separator(),
                    '2. Main Device Properties',


                    Separator(),
                    '3. All Device Properties',


                    Separator(),
                    'Go Back',

                     Separator(),
                    'Exit to Main Screen',
                ]
            }
        ]

        print(Fore.GREEN+"")
        dprop_answers = prompt(dprop_options)
        print(Fore.RESET+"")

        if dprop_answers == {'dprop_select': '1. Device IMEI(International Mobile Equipment Identity) Number'}:
            print(Fore.GREEN+"\nDevice IMEI Number"+Fore.RESET)
            print("__________________________")
            os.system("""adb shell service call iphonesubinfo 1""")

            print("\n")

        elif dprop_answers == {'dprop_select': '2. Main Device Properties'}:
            print(Fore.GREEN+"\'Main Properties"+Fore.RESET)
            print("__________________________")
            time.sleep(1)
            os.system('adb shell getprop | grep "model\|version.sdk\|manufacturer\|hardware\|platform\|revision\|serialno\|product.name\|brand"')

            print("\n")

        elif dprop_answers == {'dprop_select': '3. All Device Properties'}:
            print(Fore.GREEN+"All Properties"+Fore.RESET)
            print("__________________________")
            time.sleep(2)
            os.system("adb shell getprop")
            os.system("adb shell getprop >> /home/kali/Desktop/Cybernate/Other_Info/AllProperties.txt")

    def returnHome():

        exit = input("\n\nPress Enter to Go back to the Home Screen\n")
        if exit == "":
            
            os.system('clear')
            Main.MainScreen.home()
        else:
            dev_Prop.returnHome()



dev_Prop.extraction_Devprop()
dev_Prop.returnHome()
