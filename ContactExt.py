import os
from colorama import Fore

class contact_extract:

    def con_ex():
        
        os.system('clear')
        print(Fore.GREEN+"---------Contact List Extraction!---------"+Fore.RESET)
        print("\n")
        os.system("adb shell content query --uri content://contacts/phones/  --projection display_name:number:")
        os.system("adb shell content query --uri content://contacts/phones/  --projection display_name:number: >> /home/nevin/Desktop/Nev/New/Contact_List.txt")

contact_extract.con_ex()