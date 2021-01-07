#!/bin/bash
import os
import webbrowser
#print ('are you on mac os (1) or windows (2) if you are on linix select mac os \n make shure this .py file is in the same derectory as youre server files')
mach = input("are you on mac os (1) or windows (2) if you are on linix select mac os \n make shure this .py file is in the same derectory as youre server files")
if mach == '1':
    os.system("git clone https://github.com/Duedot43/update.git ; cd update ; cp update.txt ..")
    updates = ()
    #git hub crap i will add later
    update = open('update.txt','r')
    for line in update:
        updates = line.strip()
    os.system("rm -rf update ; rm update.txt")
    if updates == '1':
        print("Hey! there is a minecraft update!\n i will update you now give me a sec to download ma things")
        os.system('git clone https://github.com/Duedot43/minecraft-update.git ; rm papper.jar ; cd minecraft-update-master ; cp papper.jar .. ; cd .. ; rm -rf minecraft-update-master')
    os.system('java -Xmx1024M -Xms1024M -jar papper.jar')
if mach == '2':
    os.system('echo "hello! i am sorry but windows support is still in beta so use it at your own risk and you also need to install git')
    git = os.popen('git')
    for line in git:
        gits = line.strip()
    print (gits)
    if gits == ("'git' is not recognized as an internal or external command, operable program or batch file."):
        print ("installing git")
        webbrowser.open('https://download1493.mediafire.com/ru1o50w5wuog/gd5y6qy38baxhxe/Git-2.30.0-32-bit.exe', new=2)
        os.system('cd .. && cd downloads && start git-2.30.0-32-bit.exe')
    os.system("git clone https://github.com/Duedot43/update.git && cd update && copy update.txt ..")
    updates = ()
    #git hub crap i will add later
    update = open('update.txt','r')
    for line in update:
        updates = line.strip()
    os.system("rmdir update && del update.txt")
    if updates == '1':
        print("Hey! there is a minecraft update!\n i will update you now give me a sec to download ma things")
        os.system('git clone https://github.com/Duedot43/minecraft-update.git && del papper.jar && cd minecraft-update && copy papper.jar .. && cd .. && rmdir minecraft-updates')
        
