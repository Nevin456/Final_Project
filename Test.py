import os
from colorama import Fore
from PyInquirer import prompt
from PyInquirer import Separator
import pyfiglet
import sys



class MainScreen:


    def home():

        HEADER = 'Cosmos Forensics Predator'
        ART = """                                   
            i!!!!!!!!!!!!!!!!!!!~{:!!!!i                          
          i!!!!!!!!!!!!!!!!!!!!!!!~{:!!!!i
        i!~!!))!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
       i!!)!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    '!h!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
  '!!`!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!i
  ~:!4~/!!!!!!!!!!!!!!!!!!!!!!!~!!!!!!!!!!!!!!!!!!!!!
  :~!!~)(!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   ``~!!).~!!!!!!!!!!!!!{!!!!!!!!!!!!!!!!!!!!!!!!!!!!!:
        ~  '!\!!!!!!!!!!(!!!!!!!!!!!!!!!!!!!!!!4!!!~:
           '      '--`!!!!!!!!/:\!!{!!((!~.~!!`?~-      :
              ``-.    `~!{!`)(>~/ \~                   :
   .                \  : `{{`. {-   .-~`              /
    .          !:       .\\?.{\   :`      .          :!
    \ :         `      -~!{:!!!\ ~     :!`         .>!
    '  ~          '    '{!!!{!!!t                 ! !!
     '!  !.            {!!!!!!!!!              .~ {~!
      ~!!..`~:.       {!!!!!!!!!!:          .{~ :LS{
       `!!!!!!h:!?!!!!!!!!!!!!!(!!!!::..-~~` {!!!!.
         4!!!!!!!!!!!!!!!!!!!!!~!{!~!!!!!!!!!!!!'
            `!!!!!!!!!!!{\``!!``(!!!!!!!!!~~  .
             `!!!!!!!!!!!!!!!!!!!!!!!!!!!!(!:
               .!!!!!!!!!!!!!!!!!!!!!!!!\~ 
               .`!!!!!!!/`.;;~;;`~!!!!! '
                 -~!!!!!!!!!!!!!(!!!!/ .
                    `!!!!!!!!!!!!!!'
                      `\!!!!!!!!!~ """

        os.system('clear')
        C = pyfiglet.Figlet(font='slant')

        print(Fore.RED+C.renderText(HEADER)+Fore.RESET)
        print(ART)


        home_questions = [
        {
            'type': 'list',
            'name': 'main_select',
            'message': 'Cosmos Forensic Predator will discover and devour all! What shall we start with?',
            'choices': [
                Separator(),
                
                'Perform Block File Extraction on Android Device',
                'Perform Block FIle Analysis and Report Generation',
                'Perform Password Bypassing',
                'Perform Hashing on Extracted Block File',

                Separator(),
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

        print(Fore.GREEN+"")
        home_answers = prompt(home_questions)
        print(Fore.RESET+"")


        if home_answers == {'main_select':'Perform Block File Extraction on Android Device'}:
            import Extraction
            Extraction
        
        
            """ elif home_answers == {'main_select':'Perform Block FIle Analysis and Report Generation'}:
            import Analysis """
            
        elif home_answers == {'main_select':'Perform Password Bypassing'}:
            import PBypass
            PBypass.PBypass

        elif home_answers == {'main_select':'Perform Hashing on Extracted Block File'}:
            import Hashing
            Hashing
        
        
            """ elif home_answers == {'main_select':'Perform Contact List Extraction'}:
            import Contact_EX
            Contact_EX.contact_extract.con_ex()
            Contact_EX.contact_extract.return_to_climain()
        
        elif answers == {'main_select':'Perform Device Properties Extraction'}:
            import Device_Properties
            Device_Properties.device_prop.prop_extraction()
            Device_Properties.device_prop.return_to_climain()
        
        elif answers == {'main_select':'View Available Blocks for Extraction'}:
            import Block_List
            Block_List.Blk_Listing.blk_list()
            Block_List.Blk_Listing.return_to_climain()
        
        elif answers == {'main_select':'Generate Battery Health Report'}:
            import Battery
            Battery.Battery_Health.Batt_Health()
            Battery.Battery_Health.return_to_climain()
        
        elif answers == {'main_select':'About'}:
            import About
            About.about_main.about_screen()
            About.about_main.return_to_climain() """

        elif home_answers == {'main_select':'Exit'}:
            os.system('clear')
            sys.exit()

MainScreen.home()