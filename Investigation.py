import os
from colorama import Fore
from PyInquirer import prompt
from PyInquirer import Separator


class case_details:

    def case():

        os.system('clear')

        print(Fore.GREEN+"Enter The Following Details\n"+Fore.RESET)

        case_info= [
            {
                'type': 'input',
                'name': 'Case Number:',
                'message': 'Enter a Case Number:',
            },
            {
                'type': 'input',
                'name': 'Analysis Date:',
                'message': 'Enter Analysis Date:',
            },
            {
                'type': 'input',
                'name': 'Forensic Investigator:',
                'message': 'Enter the name of the Forensic Investigator:',
            },
            {
                'type': 'input',
                'name': 'Investigator ID Number:',
                'message': 'Enter ID Number of Forensic Investigator:',
            },
            {
                'type': 'input',
                'name': 'Suspect Device_ID:',
                'message': "Enter ID of Suspect's Device:",
            },
            ]

        global answers_project

        answers_project = prompt(case_info)

case_details.case();
        

