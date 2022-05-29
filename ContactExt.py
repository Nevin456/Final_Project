import os
from colorama import Fore
import Main

class contact_extract:

    def con_ex():
        
        os.system('clear')
        print(Fore.GREEN+"Acquistion of Device Contact List"+Fore.RESET)
        print("\n")
        os.system("adb shell content query --uri content://contacts/phones/  --projection display_name:number:")
        os.system("adb shell content query --uri content://contacts/phones/  --projection display_name:number: >> /home/kali/Desktop/Cybernate/Other_Info/Contact_List.txt")

    def returnHome():

        exit = input("\n\nPress Enter to Go back to the Home Screen\n")
        if exit == "":
            
            os.system('clear')
            Main.MainScreen.home()
        else:
            contact_extract.returnHome()


contact_extract.con_ex()
contact_extract.returnHome()