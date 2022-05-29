import os
from PyInquirer import prompt
from PyInquirer import Separator
from colorama import Fore
import hashlib
# from Hashing import hashing
from time import process_time
import datetime
import re
import codecs
import Main
import regex
import textwrap
from fpdf import FPDF


class testA:

    # def whatsappanalysis():

    #     bLoc = ("/home/kali/Desktop/Blocks/sda")
    #     sDes = ("/home/kali/Desktop/Blocks/sda")
    #     os.system('clear')
    #     regex_results = codecs.open(
    #         (sDes)+"WhatsApp Messsage Results.txt", "a+", encoding="utf-8")
    #     BLOCKSIZE = 16384
    #     print(Fore.LIGHTGREEN_EX+"WhatsApp Messages Extracted: \n\n"+Fore.RESET)
    #     regex_results.write("WhatsApp Messages Extracted: \n\n")
    #     global whatsapp_matchnum
    #     whatsapp_matchnum = 0
    #     with codecs.open(sDes, 'r', encoding='utf-8', errors='ignore') as y:
    #         blk = y.read(BLOCKSIZE)
    #         while len(blk) > 0:
    #             whatsapp_mess_reg = r'((\d{11})(@s.whatsapp.net)(\w{32}))([\s\S]+?)(yJ|K|-)'
    #             whatsapp_mess_find = re.finditer(
    #                 whatsapp_mess_reg, blk, re.MULTILINE)
    #             for whatsapp_matchnum, match in enumerate(whatsapp_mess_find):
    #                 whatsapp_matchnum = whatsapp_matchnum + 1
    #                 print("\n\nEntire Match {whatsapp_matchnum} found: {match}".format(whatsapp_matchnum=whatsapp_matchnum, match=match.group()))
    #                 regex_results.write("\nEntire Match {whatsapp_matchnum} found: {match}".format(whatsapp_matchnum=whatsapp_matchnum, match=match.group()))
    #                 print("\n\nWhatsApp Business Mobile Number (group {groupNum}) found: {group}".format(groupNum=2, group=match.group(2)))
    #                 regex_results.write("\n\nWhatsApp Business Mobile Number (group {groupNum}) found: {group}".format(groupNum=2, group=match.group(2)))
    #                 print("\n\nWhatsApp Business Message Sent: (group {groupNum}) found: {group}".format(groupNum=5, group=match.group(5)))
    #                 regex_results.write("\n\nWhatsApp Business Message Sent (group {groupNum}) found: {group}".format(groupNum=5, group=match.group(5)))
    #             blk = y.read(BLOCKSIZE)
    #     y.close()
    #     regex_results.close()

    # def Instagram():

    #     global bLoc
    #     bLoc = ("/home/kali/Desktop/BLK/dm-1")
    #     sDes = ("/home/kali/Desktop/BLK/dm-1")
    #     # bLoc=input("\nEnter Block File Location: ")
    #     os.system('clear')
    #     regex_results = codecs.open((sDes)+"Instagram Messsage Results.txt", "a+", encoding="utf-8")
    #     BLOCKSIZE = 16384
    #     print(Fore.LIGHTGREEN_EX+"Instagram Messages Extracted: \n\n"+Fore.RESET)
    #     regex_results.write("Instagram Messages Extracted: \n\n")
    #     global insta_matchnum
    #     insta_matchnum = 0
    #     with codecs.open(sDes, 'r', encoding='utf-8', errors='ignore') as ins:
    #         blk = ins.read(BLOCKSIZE)
    #         while len(blk) > 0:
    #             insta_mess_reg = r"""(user_id":"(\d+)",".*?,"text":"(.*?)".*?thread_id":"(\d+)".*?recipient_ids":\["(\d+)"]})"""
    #             insta_mess_find = re.finditer(
    #                 insta_mess_reg, blk, re.MULTILINE)
    #             for FBM, match in enumerate(insta_mess_find):
    #                 FBM = FBM + 1
    #                 print(Fore.CYAN+"\n\nEntire Match {FBM} found: {match}".format(FBM=FBM, match=match.group())+Fore.RESET)
    #                 regex_results.write("\nEntire Match {insta_matchnum} found: {match}".format(insta_matchnum=insta_matchnum, match=match.group()))
    #                 print(Fore.LIGHTGREEN_EX+"\n\nInstagram Sender ID (group {groupNum}) found: {group}".format(groupNum=1, group=match.group(1))+Fore.RESET)
    #                 regex_results.write("\n\nInstagram Sender ID  (group {groupNum}) found: {group}".format(groupNum=1, group=match.group(1)))
    #                 print(Fore.LIGHTGREEN_EX+"\n\nInstagram Message Sent: (group {groupNum}) found: {group}".format(groupNum=2, group=match.group(2))+Fore.RESET)
    #                 regex_results.write("\n\nInstagram Message Sent (group {groupNum}) found: {group}".format(groupNum=2, group=match.group(2)))
    #                 print(Fore.LIGHTGREEN_EX+"\n\nInstagram Receiver ID: (group {groupNum}) found: {group}".format(groupNum=4, group=match.group(4))+Fore.RESET)
    #                 regex_results.write("\n\nInstagram Receiver ID (group {groupNum}) found: {group}".format(groupNum=4, group=match.group(4)))
    #                 print(Fore.LIGHTGREEN_EX+"\n\nThread ID: (group {groupNum}) found: {group}".format( groupNum=3, group=match.group(3))+Fore.RESET)
    #                 regex_results.write("\n\nThread ID(group {groupNum}) found: {group}".format(groupNum=3, group=match.group(3)))
    #             blk = ins.read(BLOCKSIZE)
    #     ins.close()
    #     regex_results.close()



 
    # def FBMessenger():

    #     global bLoc
    #     bLoc = ("/home/kali/Desktop/BLK/dm-1")
    #     sDes = ("/home/kali/Desktop/BLK/dm-1")
    #     os.system('clear')
    #     regex_results = codecs.open((sDes)+"FB Messenger Chat Results.txt", "a+", encoding="utf-8")
    #     BLOCKSIZE = 16384
    #     print(Fore.LIGHTGREEN_EX +"FB Messenger Chat Messages Extracted: \n\n"+Fore.RESET)
    #     regex_results.write("FB Messenger Chat Messages Extracted: \n\n")
    #     global IMO_matchNum
    #     IMO_matchNum = 0
    #     with codecs.open(sDes, 'r', encoding='utf-8', errors='ignore') as FBM:
    #         blk = FBM.read(BLOCKSIZE)
    #         while len(blk) > 0:
    #             FB_mess_reg = r"""\d{16}(.*?){"msg_id":"(.*?)"}(.*?)ñ"""
    #             FB_mess_find = re.finditer(FB_mess_reg, blk, re.MULTILINE)
    #             for IMO_matchNum, match in enumerate(FB_mess_find):
    #                 IMO_matchNum = IMO_matchNum + 1
    #                 print(Fore.MAGENTA+"\n\nEntire Match {IMO_matchNum} found: {match}".format(IMO_matchNum=IMO_matchNum, match=match.group())+Fore.RESET)
    #                 regex_results.write("\nEntire Match {IMO_matchNum} found: {match}".format(IMO_matchNum=IMO_matchNum,match=match.group()))
    #             blk = FBM.read(BLOCKSIZE)
    #     FBM.close()
    #     regex_results.close()

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

    # def pickme_details():

    #     global bLoc
    #     sDes=("/home/kali/Desktop/BLK/dm-1")

    #     regex_results = codecs.open((sDes)+"Pickme Results.txt", "a+", encoding="utf-8")
    #     BLOCKSIZE = 16384
    #     print(Fore.LIGHTYELLOW_EX+"\n\nPickme Details Extracted: \n\n"+Fore.RESET)
    #     regex_results.write("Pickme Details Extracted: \n\n")
    #     global pickme_matchNum
    #     pickme_matchNum = 0
    #     with codecs.open(sDes, 'r', encoding='utf-8', errors='ignore') as y:
    #         blk = y.read(BLOCKSIZE)
    #         while len(blk) > 0:
    #             pickme_reg = r"(?<={\"AppVersion\":)(.*?)(,\"Email\":)(.*?)(,\"device_id\":)(.*?)(,\"Phone\":)(.*?)(\"default_payment_method\":)(.*?)(\"passenger_id\":)(.*?)(\"language\":)(.*?)(\"Identity\":)(.*?)(\"AppType\":)(.*?)(\"Name\":)(.*?)[}]"
    #             pickme_find = re.finditer(pickme_reg, blk)
    #             for pickme_matchNum, match in enumerate(pickme_find):/home/kali/Desktop
    #                 pickme_matchNum = pickme_matchNum + 1
    #                 print("\nEntire Match {pickme_matchNum} found: {match}".format(
    #                     pickme_matchNum=pickme_matchNum, match=match.group()))
    #                 regex_results.write("\nEntire Match {pickme_matchNum} found: {match}".format(
    #                     pickme_matchNum=pickme_matchNum, match=match.group()))
    #                 print("\n\nApplication version (group {groupNum}) found: {group}".format(
    #                     groupNum=1, group=match.group(1)))
    #                 regex_results.write("\n\nApplication Version (group {groupNum}) found: {group}".format(
    #                     groupNum=1, group=match.group(1)))
    #                 print("\n\nEmail Address (group {groupNum}) found: {group}".format(
    #                     groupNum=3, group=match.group(3)))
    #                 regex_results.write("\n\nEmail Address (group {groupNum}) found: {group}".format(
    #                     groupNum=3, group=match.group(3)))
    #                 print("\n\nDevice ID (group {groupNum}) found: {group}".format(
    #                     groupNum=5, group=match.group(5)))
    #                 regex_results.write("\n\nDevice ID (group {groupNum}) found: {group}".format(
    #                     groupNum=5, group=match.group(5)))
    #                 print("\n\nPhone Number (group {groupNum}) found: {group}".format(
    #                     groupNum=7, group=match.group(7)))
    #                 regex_results.write("\n\nPhone Number (group {groupNum}) found: {group}".format(
    #                     groupNum=7, group=match.group(7)))
    #                 print("\n\nDefault Payment Method (group {groupNum}) found: {group}".format(
    #                     groupNum=9, group=match.group(9)))
    #                 regex_results.write("\n\nDefault Payment Method (group {groupNum}) found: {group}".format(
    #                     groupNum=9, group=match.group(9)))
    #                 print("\n\nPassenger ID (group {groupNum}) found: {group}".format(
    #                     groupNum=11, group=match.group(11)))
    #                 regex_results.write("\n\nPassenger ID (group {groupNum}) found: {group}".format(
    #                     groupNum=11, group=match.group(11)))
    #                 print("\n\nApplication Language (group {groupNum}) found: {group}".format(
    #                     groupNum=13, group=match.group(13)))
    #                 regex_results.write("\n\nApplication Language (group {groupNum}) found: {group}".format(
    #                     groupNum=13, group=match.group(13)))
    #                 print("\n\nPickme ID (group {groupNum}) found: {group}".format(
    #                     groupNum=15, group=match.group(15)))
    #                 regex_results.write("\n\nPickme ID (group {groupNum}) found: {group}".format(
    #                     groupNum=15, group=match.group(15)))
    #                 print("\n\nApplication Type (group {groupNum}) found: {group}".format(
    #                     groupNum=17, group=match.group(17)))
    #                 regex_results.write("\n\nApplication Type (group {groupNum}) found: {group}".format(
    #                     groupNum=17, group=match.group(17)))
    #                 print("\n\nPickme Name (group {groupNum}) found: {group}".format(
    #                     groupNum=19, group=match.group(19)))
    #                 regex_results.write("\n\nPickme Name (group {groupNum}) found: {group}".format(
    #                     groupNum=19, group=match.group(19)))

    #             blk = y.read(BLOCKSIZE)
    #     y.close()
    #     regex_results.close()



# testA.whatsappanalysis()
# testA.IMOanalysis()
#testA.IMOanalysis()
#testA.IMO_Analysis()
testA.IMO_Analysis()
#testA.pickme_details()

