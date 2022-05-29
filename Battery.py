import colorama
import os
import Main

class Battery_Health:

    def B_Health():

        os.system('clear')

        print(colorama.Fore.YELLOW+"Android Device Battery Health Information!"+colorama.Fore.RESET)
        print("\n")

        os.system("adb shell dumpsys battery")
        os.system("adb shell dumpsys battery >> /home/kali/Desktop/Cybernate/Other_Info/Battery_Health_Report.txt")

    def returnHome():

        quit = input("\n\nPress Enter to Go back to the Home Screen\n")
        if quit == "":
            
            os.system('clear')
            Main.MainScreen.home()
        else:
            Battery_Health.returnHome()

        

Battery_Health.B_Health()
Battery_Health.returnHome()
        