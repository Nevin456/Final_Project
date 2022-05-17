import os
import hashlib
import datetime
from time import process_time
from colorama import Fore


class hashing:



    def block_AlyPrehashcheck():

        os.system('clear')

        global b_Destination

        b_Destination = input(Fore.YELLOW+"Enter the location of the block file "+Fore.RESET)


        BLOCKSIZE = 16384
        start_time = process_time()
        global pre_hash
        pre_hash = hashlib.sha512()

        with open(b_Destination, 'rb') as pre_hashfile:
            pre_blk = pre_hashfile.read(BLOCKSIZE)
            while len(pre_blk) > 0:
                pre_hash.update(pre_blk)
                pre_blk = pre_hashfile.read(BLOCKSIZE)
            pre_hashfile.close()
            end_time = process_time()
            time = end_time - start_time
            timenow = datetime.datetime.now()
            timestat = timenow.strftime("%Y-%m-%d_%H-%M")

            pre_hashtxt = open((b_Destination.replace("\\","\\\\"))+"Hash_CheckSum-Pre_Analysis.txt", "a")
            pre_hashtxt.write(pre_hash.hexdigest())
            

            print(Fore.YELLOW+"\nPre-Analysis Hash Checksum SHA512: "+Fore.RESET, pre_hash.hexdigest())
            print(Fore.YELLOW+"Pre-Analysis Time Elapsed: "+Fore.RESET, time, " seconds")
            print(Fore.BLUE+"\nHash Checksum(Pre-Analysis) for the selected Block File is Generated \n"+Fore.RESET)
            print("\n")

            print("______________________________________________________\n")

    def PreAnalysis_Compare():

        global postExt_hash,preAna_hash
        global b_destination
        

        with open('/home/nevin/Desktop/Blocks/s9/Hash_CheckSum-Post_Extraction.txt','r') as file:
            postExt_hash=file.read()

        with open('/home/nevin/Desktop/Blocks/s9/sda1Hash_CheckSum-Pre_Analysis.txt','r') as file:
            preAna_hash=file.read()

        print (preAna_hash)
        print (postExt_hash)
        

        #global repo_generation
        #repo_generation = open((b_Destination.replace("\\","\\\\"))+" Hash Verification.txt", "a+", encoding="utf-8")

        #repo_generation.write("\nBlock File Location"+b_Destination)
        #repo_generation.write("\nResult Storage Location"+b_Destination)


        #repo_generation.write("\nPre-Analysis Hash Checksum SHA512: "+ pre_hash.hexdigest()+"\n")
        #repo_generation.write("\nPost-Analysis Hash Checksum SHA512: "+ postExt_hash+"\n")

        if (preAna_hash) is (postExt_hash):
            #repo_generation.write("\nHash Checksum Remains Identical after Analysis")
            print(Fore.CYAN+"\nHash Checksum Remains Identical after Analysis\n\n"+Fore.RESET)
        else:
            #repo_generation.write("\nHash Checksum DIFFERED after Analysis")
            print(Fore.CYAN+"\nHash Checksum DIFFERED after Analysis\n\n"+Fore.RESET)
        #repo_generation.write("\n\n\n------------------ Analysis Process Completed ------------------")
        #repo_generation.close()

        #print(Fore.GREEN+"Project Summary Generated!"+Fore.RESET+"\n") 

    

    def block_AlyPosthashcheck():

        print(Fore.MAGENTA+"Please wait while The POST_HASH is being Generated!"+Fore.RESET)
        
        BLOCKSIZE = 32768
        start_time = process_time()
        global post_hash
        post_hash = hashlib.sha512()

        with open(b_Destination, 'rb') as post_hashfile:
            post_blk = post_hashfile.read(BLOCKSIZE)
            while len(post_blk) > 0:
                post_hash.update(post_blk)
                post_blk = post_hashfile.read(BLOCKSIZE)
            post_hashfile.close()
            end_time = process_time()
            time = end_time - start_time
            timenow = datetime.datetime.now()
            timestat = timenow.strftime("%Y-%m-%d_%H-%M")

            post_hashtxt = open((b_Destination.replace("\\","\\\\"))+"Hash_CheckSum-Post_Analysis(" + str(timestat) + ").txt", "a")
            post_hashtxt.write("Post-Analysis Hash Checksum SHA512: "+ post_hash.hexdigest())
            post_hashtxt.write("\nPost-Analysis Time Elapsed: "+(str(time))+" seconds")

            print(Fore.YELLOW+"\nPost-Analysis Hash Checksum SHA512: "+Fore.RESET, post_hash.hexdigest())
            print(Fore.YELLOW+"Post-Analysis Time Elapsed: "+Fore.RESET, time, " seconds")
            print(Fore.BLUE+"\nHash Checksum(Post-Analysis) for the selected Block File is Generated \n"+Fore.RESET)


    def block_Comparehash():

        global repo_generation
        repo_generation = open((b_Destination.replace("\\","\\\\"))+" Hash Verification.txt", "a+", encoding="utf-8")

        repo_generation.write("\nBlock File Location"+b_Destination)
        repo_generation.write("\nResult Storage Location"+b_Destination)


        repo_generation.write("\nPre-Analysis Hash Checksum SHA512: "+ pre_hash.hexdigest())
        repo_generation.write("\nPost-Analysis Hash Checksum SHA512: "+ post_hash.hexdigest()+"\n")

        if (post_hash.hexdigest()) == (pre_hash.hexdigest()):
            repo_generation.write("\nHash Checksum Remains Identical after Analysis")
            print(Fore.CYAN+"\nHash Checksum Remains Identical after Analysis\n\n"+Fore.RESET)
        else:
            repo_generation.write("\nHash Checksum DIFFERED after Analysis")
            print(Fore.CYAN+"\nHash Checksum DIFFERED after Analysis\n\n"+Fore.RESET)
        repo_generation.write("\n\n\n------------------ Analysis Process Completed ------------------")
        repo_generation.close()

        print(Fore.GREEN+"Project Summary Generated!"+Fore.RESET+"\n")




#hashing.block_AlyPrehashcheck()
#hashing.block_Posthashcheck()
#hashing.block_Comparehash()
hashing.PreAnalysis_Compare()