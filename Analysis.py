import os
from PyInquirer import prompt
from PyInquirer import Separator
from colorama import Fore
import hashlib
#from Hashing import hashing
from time import process_time
import datetime
import re
import codecs


class app_analysis:

    def whatsappanalysis():

        # hashing.block_Prehashcheck()

        global bLoc
        bLoc=input("\nEnter Block File Location: ")
        os.system('clear')
        regex_results = codecs.open((bLoc)+"WhatsApp Messsage Results.txt", "a+", encoding="utf-8")
        BLOCKSIZE = 16384
        print(Fore.LIGHTGREEN_EX+"WhatsApp Messages Extracted: \n\n"+Fore.RESET)
        regex_results.write("WhatsApp Messages Extracted: \n\n")
        global whatsapp_matchnum
        whatsapp_matchnum = 0
        with codecs.open(bLoc, 'r', encoding='utf-8', errors='ignore') as y:
            blk = y.read(BLOCKSIZE)
            while len(blk) > 0:
                whatsapp_mess_reg = r"(\d{11})(@s.whatsapp.net)(\w{32})\s((\w+\s|\S)+)"
                whatsapp_mess_find = re.finditer(whatsapp_mess_reg, blk, re.MULTILINE)
                for whatsapp_matchnum, match in enumerate(whatsapp_mess_find):
                    whatsapp_matchnum = whatsapp_matchnum + 1
                    print("\n\nEntire Match {whatsapp_matchnum} found: {match}".format(whatsapp_matchnum = whatsapp_matchnum, match = match.group()))
                    regex_results.write("\nEntire Match {whatsapp_matchnum} found: {match}".format(whatsapp_matchnum = whatsapp_matchnum, match = match.group()))
                    print("\n\nWhatsApp Business Mobile Number (group {groupNum}) found: {group}".format(groupNum = 2, group = match.group(2)))
                    regex_results.write("\n\nWhatsApp Business Mobile Number (group {groupNum}) found: {group}".format(groupNum = 2, group = match.group(2)))
                    print("\n\nWhatsApp Business Message Sent: (group {groupNum}) found: {group}".format(groupNum = 5, group = match.group(5)))
                    regex_results.write("\n\nWhatsApp Business Message Sent (group {groupNum}) found: {group}".format(groupNum = 5, group = match.group(5)))
                blk = y.read(BLOCKSIZE)
        y.close()
        regex_results.close()

        #hashing.block_Posthashcheck()
        #hashing.block_Comparehash()
 
    def instaanalysis():

        global bLoc
        bLoc=input("\nEnter Block File Location: ")
        os.system('clear')
        regex_results = codecs.open((bLoc)+"Instagram Messsage Results.txt", "a+", encoding="utf-8")
        BLOCKSIZE = 16384
        print(Fore.LIGHTGREEN_EX+"Instagram Messages Extracted: \n\n"+Fore.RESET)
        regex_results.write("Instagram Messages Extracted: \n\n")
        global insta_matchnum
        insta_matchnum = 0
        with codecs.open(bLoc, 'r', encoding='utf-8', errors='ignore') as y:
            blk = y.read(BLOCKSIZE)
            while len(blk) > 0:
                insta_mess_reg = r"""user_id":"(\d{11})","text":"(.*?)",.*?recipient_ids":\["(\d{9})"]"""
                insta_mess_find = re.finditer(insta_mess_reg, blk, re.MULTILINE)
                for insta_matchNum, match in enumerate(insta_mess_find):
                    insta_matchNum = insta_matchNum + 1
                    print("\n\nEntire Match {insta_matchNum} found: {match}".format(insta_matchNum = insta_matchNum, match = match.group()))
                    regex_results.write("\nEntire Match {insta_matchnum} found: {match}".format(insta_matchnum = insta_matchnum, match = match.group()))
                    print("\n\nInstagram Sender ID (group {groupNum}) found: {group}".format(groupNum = 1, group = match.group(1)))
                    regex_results.write("\n\nInstagram Sender ID  (group {groupNum}) found: {group}".format(groupNum = 1, group = match.group(1)))
                    print("\n\nInstagram Message Sent: (group {groupNum}) found: {group}".format(groupNum = 2, group = match.group(2)))
                    regex_results.write("\n\nInstagram Message Sent (group {groupNum}) found: {group}".format(groupNum = 2, group = match.group(2)))
                    print("\n\nInstagram Receiver ID: (group {groupNum}) found: {group}".format(groupNum = 3, group = match.group(3)))
                    regex_results.write("\n\nInstagram Receiver ID (group {groupNum}) found: {group}".format(groupNum = 3, group = match.group(2)))
                blk = y.read(BLOCKSIZE)
        y.close()
        regex_results.close()


    def viberanalysis():

        global bLoc
        bLoc=input("\nEnter Block File Location: ")
        os.system('clear')
        regex_results = codecs.open((bLoc)+"Viber Messsage Results.txt", "a+", encoding="utf-8")
        BLOCKSIZE = 16384
        print(Fore.LIGHTGREEN_EX+"Viber Messages Extracted: \n\n"+Fore.RESET)
        regex_results.write("Viber Messages Extracted: \n\n")
        global viber_matchnum
        viber_matchnum = 0
        with codecs.open(bLoc, 'r', encoding='utf-8', errors='ignore') as y:
            blk = y.read(BLOCKSIZE)
            while len(blk) > 0:
                viber_mess_reg = r"NèÈ.*?[ÉO|S][\s\S]+?(.*?){}no_sp"
                viber_mess_find = re.finditer(viber_mess_reg, blk, re.MULTILINE)
                for viber_matchNum, match in enumerate(viber_mess_find):
                    viber_matchNum = viber_matchNum + 1
                    print("\n\nEntire Match {viber_matchNum} found: {match}".format(viber_matchNum = viber_matchNum, match = match.group()))
                    regex_results.write("\nEntire Match {viber_matchnum} found: {match}".format(viber_matchnum = viber_matchnum, match = match.group()))
                    print("\n\nViber Message Text(group {groupNum}) found: {group}".format(groupNum = 1, group = match.group(1)))
                    regex_results.write("\n\nViber Text Message (group {groupNum}) found: {group}".format(groupNum = 1, group = match.group(1)))
                blk = y.read(BLOCKSIZE)
        y.close()
        regex_results.close()


  
    
app_analysis.whatsappanalysis()
#app_analysis.instaanalysis()
#app_analysis.viberanalysis()
