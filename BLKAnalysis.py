import os
from PyInquirer import prompt
from PyInquirer import Separator
from colorama import Fore
import hashlib
from time import process_time
import datetime
import re
import codecs
import Main
import regex
import textwrap
from fpdf import FPDF
import aspose.words as aw


class blk_analysis:

    def Investigation():

        print(Fore.GREEN+"Enter The Following Details\n"+Fore.RESET)

        case_info= [
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
                'name': 'Case Number:',
                'message': 'Enter a Case Number:',
            },
            {
                'type': 'input',
                'name': 'Analysis Date:',
                'message': 'Enter Analysis Date:',
            },
            ]

        global answers_project

        answers_project = prompt(case_info)



    def Block_Location():

        global bLoc

        bLoc = input("\nEnter Location of the Block File: ")
        if os.path.isfile(bLoc):
            print("Block Found!")
        else:
            print("Block not found! Please Try Again")
            blk_analysis.Block_Location()

    def Result_SL():

        global s_Dest,sDes
        s_Dest = input("\nEnter Location to store Results: ")
        sDes = (s_Dest+"/")
        print (sDes)
        try:
            if os.path.exists(sDes):
                confirmation = [
                    {
                        'type': 'confirm',
                        'message': 'This directory already exists. Would you like to use it anyway?',
                        'name': 'continue',
                        'default': False,
                    },
                ]
                choice = prompt(confirmation)
                if choice == {'continue': False}:
                    blk_analysis.Result_SL()
            else:
                os.mkdir(sDes)
                print("Directory has been Created!")
        except FileNotFoundError:
            blk_analysis.Result_SL()
            

    def block_AlyPrehashcheck():

        print(Fore.MAGENTA+"\n\nPre-Analysis Hash is being generated. HOLD TIGHT!!!"+Fore.RESET)
        print("______________________________________________________\n")

        BLKSIZE = 16384
        start_time = process_time()
        global pre_hash
        pre_hash = hashlib.sha512()

        with open(bLoc, 'rb') as pre_hashfile:
            pre_blk = pre_hashfile.read(BLKSIZE)
            while len(pre_blk) > 0:
                pre_hash.update(pre_blk)
                pre_blk = pre_hashfile.read(BLKSIZE)
            pre_hashfile.close()
            end_time = process_time()
            time = end_time - start_time
            timenow = datetime.datetime.now()
            timestat = timenow.strftime("%Y-%m-%d_%H-%M")

            preExttxt = open((sDes.replace("\\","\\\\"))+"Hash_CheckSum-Pre_Analysis(" + str(timestat) + ").txt", "a")
            preExttxt.write("Pre-Analysis Hash Checksum SHA512: "+ pre_hash.hexdigest())
            preExttxt.write("\nPre-Analysis Time Elapsed: "+(str(time))+" seconds")

            print(Fore.YELLOW+"\nPre-Analysis Hash Checksum SHA512: "+Fore.RESET, pre_hash.hexdigest())
            print(Fore.YELLOW+"Pre-Analysis Time Elapsed: "+Fore.RESET, time, " seconds")
            print(Fore.BLUE+"\nHash Checksum (Pre-Analysis) for the selected Block File has been Generated \n"+Fore.RESET)
            print("\n")

            print("______________________________________________________\n")

    def appselect():

        app_choice = [
            {
                'type': 'checkbox',
                'message': 'Select the Apps required to be analyzed?',
                'name': '',
                'choices': [
                    Separator('Application Selection'),
                    {
                        'name': 'Facebook Messenger'
                    },
                    {
                        'name': 'Instagram'
                    },
                    {
                        'name': 'WhatsApp'
                    },
                    {
                        'name': 'IMO'
                    },
                    {
                        'name': 'Test'
                    }
                ]
            }
        ]


        global selected_app
        selected_app = prompt(app_choice)
        print("\n\nAndroid Applications Selected for Analysis: ")
        for x in selected_app:
            one = (str(selected_app[x]).replace("[", ""))
            two = one.replace("\'", "")
            three = two.replace(",", "\n")
            print(Fore.BLUE+" "+three+Fore.RESET)

        que_confirm = [
            {
                'type': 'confirm',
                'message': 'Analysis will be done on these applications!!!',
                'name': 'continue',
                'default': True,
            },
        ]

        print(Fore.BLUE+"\n")
        confirm_ans = prompt(que_confirm)
        print(Fore.RESET+"\n")

        if confirm_ans == {'continue': False}:
            Main.MainScreen.home()

    def app_regexmatch():

        selection = (str(selected_app))
        if "Facebook Messenger" in selection:
            blk_analysis.FBMessenger_analysis()
        else:
            pass

        if "Instagram" in selection:
            blk_analysis.insta_analysis()
        else:
            pass

        if "WhatsApp" in selection:
            blk_analysis.whatsapp_analysis()
        else:
            pass

        if "IMO" in selection:
            blk_analysis.IMO_Analysis()
        else:
            pass

        if "Booking.com" in selection:
            blk_analysis.insta_analysis()
        else:
            pass 


    def FBMessenger_analysis():


        regex_results = codecs.open((sDes)+"FB Messenger Chat Results.txt", "a+", encoding="utf-8")
        BLKSIZE = 16384
        print(Fore.LIGHTBLUE_EX+"\n\nFB Messenger Chat Messages Extracted: \n\n"+Fore.RESET)
        regex_results.write("FB Messenger Chat Messages Extracted: \n\n")
        global FBMessenger_Num
        FBMessenger_Num = 0
        with codecs.open(bLoc, 'r', encoding='utf-8', errors='ignore') as FBM:
            blk = FBM.read(BLKSIZE)
            while len(blk) > 0:
                FB_mess_reg = r"""ONE_TO_ONE:\d+:\d+(.*?){"user_key":"(.*?)","name":"(.*?)","email":(.*?),"phone":(.*?),.*?"birthday_month":(.*?),"birthday_day":(.*?)}"""
                FB_mess_find = re.finditer(FB_mess_reg, blk, re.MULTILINE)
                for FBMessenger_Num, match in enumerate(FB_mess_find):
                    FBMessenger_Num = FBMessenger_Num + 1
                    print(Fore.MAGENTA+"\n\nEntire Match {FBMessenger_Num} found: {match}".format(FBMessenger_Num=FBMessenger_Num, match=match.group())+Fore.RESET)
                    regex_results.write("\nEntire Match {FBMessenger_Num} found: {match}".format(FBMessenger_Num=FBMessenger_Num,match=match.group()))
                    print(Fore.BLUE+"\n\nSender Namer(group {groupNum}) found: {group}".format(groupNum=3, group=match.group(3))+Fore.RESET)
                    regex_results.write("\n\nSender Name (group {groupNum}) found: {group}".format(groupNum=3, group=match.group(3)))
                    print(Fore.BLUE+"\n\nFB Messenger Message Sent (group {groupNum}) found: {group}".format(groupNum=1, group=match.group(1))+Fore.RESET)
                    regex_results.write("\n\nFB Messenger Message Sent (group {groupNum}) found: {group}".format(groupNum=1, group=match.group(1)))
                    print(Fore.BLUE+"\n\nFB Messenger ID: (group {groupNum}) found: {group}".format(groupNum=2, group=match.group(2))+Fore.RESET)
                    regex_results.write("\n\nFB Messenger ID (group {groupNum}) found: {group}".format(groupNum=2, group=match.group(2)))
                    print(Fore.BLUE+"\n\nFB Messenger Email: (group {groupNum}) found: {group}".format(groupNum=4, group=match.group(4))+Fore.RESET)
                    regex_results.write("\n\nFB Messenger Email(group {groupNum}) found: {group}".format(groupNum=4, group=match.group(4)))
                    print(Fore.BLUE+"\n\nFB Messenger Phone Number (group {groupNum}) found: {group}".format(groupNum=5, group=match.group(5))+Fore.RESET)
                    regex_results.write("\n\nFB Messenger Phone Number(group {groupNum}) found: {group}".format(groupNum=5, group=match.group(5)))
                    print(Fore.BLUE+"\n\nFB Messenger Birthday Month (group {groupNum}) found: {group}".format(groupNum=6, group=match.group(6))+Fore.RESET)
                    regex_results.write("\n\nFB Messenger Birthday Month (group {groupNum}) found: {group}".format(groupNum=6, group=match.group(6)))
                    print(Fore.BLUE+"\n\nFB Messenger Birthday Day (group {groupNum}) found: {group}".format(groupNum=7, group=match.group(7))+Fore.RESET)
                    regex_results.write("\n\nFB Messenger Birthday Day (group {groupNum}) found: {group}".format(groupNum=7, group=match.group(7)))
                blk = FBM.read(BLKSIZE)
        FBM.close()
        regex_results.close()

    def insta_analysis():


        regex_results = codecs.open((sDes)+"Instagram Messsage Results.txt", "a+", encoding="utf-8")
        BLKSIZE = 16384
        print(Fore.LIGHTBLUE_EX+"\n\nInstagram Messages Extracted: \n\n"+Fore.RESET)
        regex_results.write("Instagram Messages Extracted: \n\n")
        global insta_matchNum
        insta_matchNum = 0
        with codecs.open(bLoc, 'r', encoding='utf-8', errors='ignore') as ins:
            blk = ins.read(BLKSIZE)
            while len(blk) > 0:
                insta_mess_reg = r"""(user_id":"(\d+)",".*?,"text":"(.*?)".*?thread_id":"(\d+)".*?recipient_ids":\["(\d+)"]})"""
                insta_mess_find = re.finditer(insta_mess_reg, blk, re.MULTILINE)
                for insta_matchNum, match in enumerate(insta_mess_find):
                    insta_matchNum = insta_matchNum + 1
                    print(Fore.CYAN+"\n\nEntire Match {insta_matchNum} found: {match}".format(insta_matchNum=insta_matchNum, match=match.group())+Fore.RESET)
                    regex_results.write("\nEntire Match {insta_matchNum} found: {match}".format(insta_matchNum=insta_matchNum, match=match.group()))
                    print(Fore.LIGHTGREEN_EX+"\n\nInstagram Sender ID (group {groupNum}) found: {group}".format(groupNum=1, group=match.group(1))+Fore.RESET)
                    regex_results.write("\n\nInstagram Sender ID  (group {groupNum}) found: {group}".format(groupNum=1, group=match.group(1)))
                    print(Fore.LIGHTGREEN_EX+"\n\nInstagram Message Sent (group {groupNum}) found: {group}".format(groupNum=2, group=match.group(2))+Fore.RESET)
                    regex_results.write("\n\nInstagram Message Sent (group {groupNum}) found: {group}".format(groupNum=2, group=match.group(2)))
                    print(Fore.LIGHTGREEN_EX+"\n\nInstagram Receiver ID (group {groupNum}) found: {group}".format(groupNum=4, group=match.group(4))+Fore.RESET)
                    regex_results.write("\n\nInstagram Receiver ID (group {groupNum}) found: {group}".format(groupNum=4, group=match.group(4)))
                    print(Fore.LIGHTGREEN_EX+"\n\nThread ID: (group {groupNum}) found: {group}".format(groupNum=3, group=match.group(3))+Fore.RESET)
                    regex_results.write("\n\nThread ID(group {groupNum}) found: {group}".format(groupNum=3, group=match.group(3)))
                blk = ins.read(BLKSIZE)
        ins.close()
        regex_results.close()

    def whatsapp_analysis():


        bLocation=("/home/kali/Desktop/Cybernate/Analysis/dm-1")
        regex_results = codecs.open((sDes)+"WhatsApp Messsage Results.txt", "a+", encoding="utf-8")
        BLKSIZE = 16384
        print(Fore.LIGHTBLUE_EX+"WhatsApp Messages Extracted: \n\n"+Fore.RESET)
        regex_results.write("WhatsApp Messages Extracted: \n\n")
        global whatsapp_matchnum
        whatsapp_matchnum = 0
        with codecs.open(bLocation, 'r', encoding='utf-8', errors='ignore') as y:
            blk = y.read(BLKSIZE)
            while len(blk) > 0:
                whatsapp_mess_reg = r'((\d{11})(@s.whatsapp.net)(\w{32}))([\s\S]+?)(yJ|K|-)'
                whatsapp_mess_find = re.finditer(
                    whatsapp_mess_reg, blk, re.MULTILINE)
                for whatsapp_matchnum, match in enumerate(whatsapp_mess_find):
                    whatsapp_matchnum = whatsapp_matchnum + 1
                    print("\n\nEntire Match {whatsapp_matchnum} found: {match}".format( whatsapp_matchnum=whatsapp_matchnum, match=match.group()))
                    regex_results.write("\nEntire Match {whatsapp_matchnum} found: {match}".format(whatsapp_matchnum=whatsapp_matchnum, match=match.group()))
                    print("\n\nWhatsApp Business Mobile Number (group {groupNum}) found: {group}".format(groupNum=2, group=match.group(2)))
                    regex_results.write("\n\nWhatsApp Business Mobile Number (group {groupNum}) found: {group}".format(groupNum=2, group=match.group(2)))
                    print("\n\nWhatsApp Business Message Sent: (group {groupNum}) found: {group}".format(groupNum=5, group=match.group(5)))
                    regex_results.write("\n\nWhatsApp Business Message Sent (group {groupNum}) found: {group}".format(groupNum=5, group=match.group(5)))
                blk = y.read(BLKSIZE)
        y.close()
        regex_results.close()

    def IMO_Analysis():
        
        bloc=("/home/kali/Desktop/BLK/Report/dm-1")
        sDes=("/home/kali/Desktop/BLK/Report/")
        os.system('clear')
        regex_results = codecs.open((sDes)+"IMO Chat Results.txt", "a+", encoding="utf-8")
        BLOCKSIZE = 16384
        print(Fore.LIGHTGREEN_EX+"IMO Chat Messages Extracted: \n\n"+Fore.RESET)
        regex_results.write("IMO Chat Messages Extracted: \n\n")
        global IMO_matchNum
        IMO_matchNum = 0
        with codecs.open(bloc, 'r', encoding='utf-8', errors='ignore') as imo:
            blk = imo.read(BLOCKSIZE)
            while len(blk) > 0:
                IMO_mess_reg = r"""\d{16}(.*?){"msg_id":"(.*?)"}(.*?)9"""
                IMO_mess_find = re.finditer(IMO_mess_reg, blk, re.MULTILINE)
                for IMO_matchNum, match in enumerate(IMO_mess_find):
                    IMO_matchNum = IMO_matchNum + 1
                    print("\n\nEntire Match {IMO_matchNum} found: {match}".format(IMO_matchNum=IMO_matchNum, match=match.group()))
                    regex_results.write("\nEntire Match {IMO_matchNum} found: {match}".format(IMO_matchNum=IMO_matchNum, match=match.group()))
                    print(Fore.LIGHTGREEN_EX+"\n\nIMO Message ID (group {groupNum}) found: {group}".format(groupNum=2, group=match.group(2))+Fore.RESET)
                    regex_results.write("\n\nIMO Message ID  (group {groupNum}) found: {group}".format(groupNum=2, group=match.group(2)))
                    print(Fore.LIGHTGREEN_EX+"\n\nIMO Sender Name (group {groupNum}) found: {group}".format(groupNum=1, group=match.group(1))+Fore.RESET)
                    regex_results.write("\n\nIMO Sender Name (group {groupNum}) found: {group}".format(groupNum=1, group=match.group(1)))
                    print(Fore.LIGHTGREEN_EX+"\n\nIMO Message(group {groupNum}) found: {group}".format(groupNum=3, group=match.group(3))+Fore.RESET)
                    regex_results.write("\n\nIMO Message (group {groupNum}) found: {group}".format(groupNum=3, group=match.group(3)))
                blk = imo.read(BLOCKSIZE)
        imo.close()
        regex_results.close() 


    def block_AlyPosthashcheck():

        print(Fore.MAGENTA+"\n\nPost-Analysis Hash is being generated. HOLD TIGHT!!!\n"+Fore.RESET)
        print("______________________________________________________\n")
        
        BLKSIZE = 32768
        start_time = process_time()
        global post_hash
        post_hash = hashlib.sha512()

        with open(bLoc, 'rb') as post_hashfile:
            post_blk = post_hashfile.read(BLKSIZE)
            while len(post_blk) > 0:
                post_hash.update(post_blk)
                post_blk = post_hashfile.read(BLKSIZE)
            post_hashfile.close()
            end_time = process_time()
            time = end_time - start_time
            timenow = datetime.datetime.now()
            timestat = timenow.strftime("%Y-%m-%d_%H-%M")

            post_hashtxt = open((sDes.replace("\\","\\\\"))+"Hash_CheckSum-Post_Analysis(" + str(timestat) + ").txt", "a")
            post_hashtxt.write("Post-Analysis Hash Checksum SHA512: "+ post_hash.hexdigest())
            post_hashtxt.write("\nPost-Analysis Time Elapsed: "+(str(time))+" seconds")

            print(Fore.YELLOW+"\nPost-Analysis Hash Checksum SHA512: "+Fore.RESET, post_hash.hexdigest())
            print(Fore.YELLOW+"Post-Analysis Time Elapsed: "+Fore.RESET, time, " seconds")
            print(Fore.BLUE+"\nHash Checksum(Post-Analysis) for the selected Block File is Generated \n"+Fore.RESET)

    def Creation_Report():


        print(Fore.BLUE+"Report Creation!!!"+Fore.RESET)
        print("______________________________________________________\n")


        outputformat= [
            {
                'type': 'list',
                'name': 'format_select',
                'message': 'In which format do you want to output the Analysis Report?',
                'choices': [
                    Separator(),

                    '1. PDF Format',
                    '2. Text Format',


                    Separator(),
                    'Exit',
                ]
            }
        ] 
        print(Fore.GREEN+"")
        formatout = prompt(outputformat)
        print(Fore.RESET+"")

        if formatout == {'format_select': '1. PDF Format'}:
            blk_analysis.Txtreport_Creation()
            blk_analysis.Pdfreport_Creation()
            


        elif formatout == {'format_select': '2. Text Format'}:
            blk_analysis.Txtreport_Creation()
            

        
    def Txtreport_Creation():
 
        global txtrport_create
        txtrport_create = open((sDes.replace("\\","\\\\"))+"Analysis Report.txt","+a",encoding="utf-8")

        for x in answers_project:
            txtrport_create.write(x)
            txtrport_create.write(" "+answers_project[x])
            txtrport_create.write("\n")

        for x in selected_app:
        
            one = (str(selected_app[x]).replace("[",""))
            two = one.replace("\'","")
            three = two.replace(",","\n")
            txtrport_create.write("\n\nAndroid Applications Selected for Analysis: \n "+three+"\n\n")


        txtrport_create.write("\nBlock File Location: "+bLoc)
        txtrport_create.write("\nResult Storage Location: "+sDes)

        txtrport_create.write("\nPre-Analysis Hash Checksum SHA512: "+ pre_hash.hexdigest())
        txtrport_create.write("\nPost-Analysis Hash Checksum SHA512: "+ post_hash.hexdigest()+"\n")

        if (post_hash.hexdigest()) == (pre_hash.hexdigest()):
            txtrport_create.write("\nHash Checksum Remains Identical after Analysis")
            print(Fore.CYAN+"\nHash Checksum Remains Identical after Analysis\n\n"+Fore.RESET)
        else:
            txtrport_create.write("\nHash Checksum DIFFERED after Analysis")
            print(Fore.CYAN+"\nHash Checksum DIFFERED after Analysis\n\n"+Fore.RESET)
        txtrport_create.write("\n\n\n------------------ Analysis Process Completed ------------------")
        txtrport_create.close()

        print(Fore.LIGHTGREEN_EX+"Analysis Report Generated!!!")


    def Pdfreport_Creation():


        try:
            doc=aw.Document(sDes+"Analysis Report.txt")
            doc.save(sDes+"Analysis Report.pdf",aw.SaveFormat.PDF)
            os.remove(sDes+"Analysis Report.txt")

        except ImportError:
            print("Done")
        





 
    def returnHome():

        exit = input("\n\nPress Enter to Go back to the Home Screen\n")
        if quit == "":
            
            os.system('clear')
            Main.MainScreen.home()
        else:
            blk_analysis.returnHome()

blk_analysis.Investigation()    
blk_analysis.Block_Location()
blk_analysis.Result_SL()
blk_analysis.block_AlyPrehashcheck()
blk_analysis.appselect()
blk_analysis.app_regexmatch()
blk_analysis.block_AlyPosthashcheck()
blk_analysis.Creation_Report()