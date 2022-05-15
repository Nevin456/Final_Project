import colorama
import os

class Battery_Health:

    def B_Health():

        os.system('clear')

        print(colorama.Fore.YELLOW+"Android Device Battery Health Information!"+colorama.Fore.RESET)
        print("\n");

        os.system("adb shell dumpsys battery")
        