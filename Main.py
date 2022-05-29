
from cProfile import label
from curses import window
import os
from colorama import Fore
from PyInquirer import prompt
from PyInquirer import Separator
import sys
import Main
from art import *


class MainScreen:


    def home():

        os.system('clear')

        print("\n\n")
        title=text2art("Cybernate","random")
        print(Fore.BLUE+title+Fore.RESET)

        ART = """  
      ooooooooooooooooooooooooooooooooooooo
      8                                .d88
      8  oooooooooooooooooooooooooooood8888
      8  8888888888888888888888888P"   8888    oooooooooooooooo
      8  8888888888888888888888P"      8888    8              8
      8  8888888888888888888P"         8888    8             d8
      8  8888888888888888P"            8888    8            d88
      8  8888888888888P"               8888    8           d888
      8  8888888888P"                  8888    8          d8888
      8  8888888P"                     8888    8         d88888
      8  8888P"                        8888    8        d888888
      8  8888oooooooooooooooooooooocgmm8888    8       d8888888
      8 .od88888888888888888888888888888888    8      d88888888
      8888888888888888888888888888888888888    8     d888888888
                                               8    d8888888888
         ooooooooooooooooooooooooooooooo       8   d88888888888
        d                       ...oood8b      8  d888888888888
       d              ...oood888888888888b     8 d8888888888888
      d     ...oood88888888888888888888888b    8d88888888888888
     dood8888888888888888888888888888888888b

                      """

        
        
        print(Fore.GREEN+ART+Fore.RESET)

        
        home_questions = [
        {
            'type': 'list',
            'name': 'main_select',
            'message': 'Cybernate will discover and recover all! What shall we start with?',
            'choices': [
                Separator(),
                
                'Perform Block File Extraction on Android Device',
                'Perform Block File Analysis and Report Generation',
                'Perform Password Bypassing on Android',

                Separator(),
                'Perform Addition of a New Regex Pattern',
                'Perform Device Properties Acquisition',
                'Perform Contact List Acquistion',
                'Perform Device Properties Acquisition',
                'Generate Battery Health Report',
                
                Separator(),
                'About',
                'Exit',
            ]
        }
    ]

        print(Fore.BLUE+"\n")
        home_answers = prompt(home_questions)
        print(Fore.RESET+"\n")


        if home_answers == {'main_select':'Perform Block File Extraction on Android Device'}:
            import BLKExtraction
            BLKExtraction

       
        elif home_answers == {'main_select':'Perform Block File Analysis and Report Generation'}:
            import BLKAnalysis
            BLKAnalysis

            
        elif home_answers == {'main_select':'Perform Password Bypassing'}:
            import PBypass
            PBypass.PBypass


        elif home_answers == {'main_select':'Perform Addition of a New Regex Pattern'}:
            import RegexAddition
            RegexAddition

    
        elif home_answers == {'main_select':'Perform Contact List Acquisition'}:
            import ContactExt
            ContactExt
            
        
        elif home_answers == {'main_select':'Perform Device Properties Acquistion'}:
            import DProperties
            DProperties
            
        elif home_answers == {'main_select':'Generate Battery Health Report'}:
            import Battery
            Battery
        
        elif home_answers == {'main_select':'About'}:
            import WA
            WA
        elif home_answers == {'main_select':'Exit'}:
            os.system('clear')
            sys.exit()   
            
MainScreen.home()
        