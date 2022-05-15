import os
from colorama import Fore
from colorama import Style
import time
from PyInquirer import prompt
from PyInquirer import Separator


class dev_Prop:

    def extraction_Devprop():

        os.system('clear')

        print(Fore.YELLOW+Style.BRIGHT +
              "Extraction of Device Properties!"+Style.NORMAL+Fore.RESET)

        dprop_options = [
            {
                'type': 'list',
                'name': 'dprop_select',
                'message': 'Select the option you require?',
                'choices': [
                    Separator(),

                    '1. Device IMEI(International Mobile Equipment Identity) Number',


                    Separator(),
                    '2. Main Device Propertices',


                    Separator(),
                    '3. All Device Properties',


                    Separator(),
                    'Exit',
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

        elif dprop_answers == {'dprop_select': '2. Main Device Propertices'}:
            print(Fore.GREEN+"\'Main Properties"+Fore.RESET)
            print("__________________________")
            time.sleep(1)
            os.system(
                'adb shell getprop | grep "model\|version.sdk\|manufacturer\|hardware\|platform\|revision\|serialno\|product.name\|brand"')
            print("\n")

        elif dprop_answers == {'dprop_select': '3. All Device Properties'}:
            print(Fore.GREEN+"All Properties"+Fore.RESET)
            print("__________________________")
            time.sleep(2)
            os.system("adb shell getprop")

        """ print(Fore.GREEN+"\nDevice IMEI Number"+Fore.RESET)
        print("__________________________")
        os.system(""""adb shell service call iphonesubinfo 1"""")
        print("\n")
        print(Fore.GREEN+"\'dprop Properties"+Fore.RESET)
        print("__________________________")
        time.sleep(1)
        os.system('adb shell getprop | grep "model\|version.sdk\|manufacturer\|hardware\|platform\|revision\|serialno\|product.name\|brand"')
        print("\n")
        print(Fore.GREEN+"All Properties"+Fore.RESET)
        print("__________________________")
        time.sleep(2)
        os.system("adb shell getprop") """


dev_Prop.extraction_Devprop()
