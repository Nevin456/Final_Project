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

import regex


class app_analysis:

    

    def whatsappanalysis():

        # hashing.block_Prehashcheck()

        global bLoc
        #bLoc=input("\nEnter Block File Location: ")
        bLoc = "/home/nevin/Desktop/AndroidB/data.img"
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
                whatsapp_mess_reg = r"((\d{11})(@s.whatsapp.net)(\w{32}))([\s\S]+?)(yJ|K|-)"
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
        bLoc = "/home/nevin/Desktop/Blocks/dm-1"
        #bLoc=input("\nEnter Block File Location: ")
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
                    regex_results.write("\nEntire Match {insta_matchnum} found: {match}".formatr(insta_matchnum = insta_matchnum, match = match.group()))
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
        bLoc = "/home/nevin/Desktop/Blocks/dm-1"
        #bLoc=input("\nEnter Block File Location: ")
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

    def pickme_details():


        global bLoc
        bLoc = "/home/nevin/Desktop/Blocks/dm-1"

        regex_results = codecs.open((bLoc)+"Pickme Results.txt", "a+", encoding="utf-8")
        BLOCKSIZE = 16384
        print(Fore.LIGHTYELLOW_EX+"\n\nPickme Details Extracted: \n\n"+Fore.RESET)
        regex_results.write("Pickme Details Extracted: \n\n")
        global pickme_matchNum
        pickme_matchNum = 0
        with codecs.open(bLoc, 'r', encoding='utf-8', errors='ignore') as y:
            blk = y.read(BLOCKSIZE)
            while len(blk) > 0:
                pickme_reg = r"(?<={\"AppVersion\":)(.*?)(,\"Email\":)(.*?)(,\"device_id\":)(.*?)(,\"Phone\":)(.*?)(\"default_payment_method\":)(.*?)(\"passenger_id\":)(.*?)(\"language\":)(.*?)(\"Identity\":)(.*?)(\"AppType\":)(.*?)(\"Name\":)(.*?)[}]"
                pickme_find = re.finditer(pickme_reg, blk)
                for pickme_matchNum, match in enumerate(pickme_find):
                    pickme_matchNum = pickme_matchNum + 1
                    print("\nEntire Match {pickme_matchNum} found: {match}".format(pickme_matchNum = pickme_matchNum, match = match.group()))
                    regex_results.write("\nEntire Match {pickme_matchNum} found: {match}".format(pickme_matchNum = pickme_matchNum, match = match.group()))
                    print("\n\nApplication version (group {groupNum}) found: {group}".format(groupNum = 1, group = match.group(1)))
                    regex_results.write("\n\nApplication Version (group {groupNum}) found: {group}".format(groupNum = 1, group = match.group(1)))
                    print("\n\nEmail Address (group {groupNum}) found: {group}".format(groupNum = 3, group = match.group(3)))
                    regex_results.write("\n\nEmail Address (group {groupNum}) found: {group}".format(groupNum = 3, group = match.group(3)))
                    print("\n\nDevice ID (group {groupNum}) found: {group}".format(groupNum = 5, group = match.group(5)))
                    regex_results.write("\n\nDevice ID (group {groupNum}) found: {group}".format(groupNum = 5, group = match.group(5)))
                    print("\n\nPhone Number (group {groupNum}) found: {group}".format(groupNum = 7, group = match.group(7)))
                    regex_results.write("\n\nPhone Number (group {groupNum}) found: {group}".format(groupNum = 7, group = match.group(7)))
                    print("\n\nDefault Payment Method (group {groupNum}) found: {group}".format(groupNum = 9, group = match.group(9)))
                    regex_results.write("\n\nDefault Payment Method (group {groupNum}) found: {group}".format(groupNum = 9, group = match.group(9)))
                    print("\n\nPassenger ID (group {groupNum}) found: {group}".format(groupNum = 11, group = match.group(11)))
                    regex_results.write("\n\nPassenger ID (group {groupNum}) found: {group}".format(groupNum = 11, group = match.group(11)))
                    print("\n\nApplication Language (group {groupNum}) found: {group}".format(groupNum = 13, group = match.group(13)))
                    regex_results.write("\n\nApplication Language (group {groupNum}) found: {group}".format(groupNum = 13, group = match.group(13)))
                    print("\n\nPickme ID (group {groupNum}) found: {group}".format(groupNum = 15, group = match.group(15)))
                    regex_results.write("\n\nPickme ID (group {groupNum}) found: {group}".format(groupNum = 15, group = match.group(15)))
                    print("\n\nApplication Type (group {groupNum}) found: {group}".format(groupNum = 17, group = match.group(17)))
                    regex_results.write("\n\nApplication Type (group {groupNum}) found: {group}".format(groupNum = 17, group = match.group(17)))
                    print("\n\nPickme Name (group {groupNum}) found: {group}".format(groupNum = 19, group = match.group(19)))
                    regex_results.write("\n\nPickme Name (group {groupNum}) found: {group}".format(groupNum = 19, group = match.group(19)))


                blk = y.read(BLOCKSIZE)
        y.close()
        regex_results.close()





  
    
app_analysis.whatsappanalysis()
app_analysis.instaanalysis()
#app_analysis.viberanalysis()
#app_analysis.pickme_details()
