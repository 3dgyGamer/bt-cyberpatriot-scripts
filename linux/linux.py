import os
import subprocess

#### Variables for use
media_files_raw= [
    # Audio formats
    'aa',
    'aac',
    'aax',
    'act',
    'aif',
    'aiff',
    'alac',
    'amr',
    'ape',
    'au',
    'awb',
    'dss',
    'dvf',
    'flac',
    'gsm',
    'iklax',
    'ivs',
    'm4a',
    'm4b',
    'mmf',
    'mp3',
    'mpc',
    'msv',
    'nmf',
    'ogg',
    'oga',
    'mogg',
    'opus',
    'ra',
    'raw',
    'rf64',
    'sln',
    'tta',
    'voc',
    'vox',
    'wav',
    'wma',
    'wv',
    '8svx',
    'cda',
    # Video formats
    'webm',
    'mkv',
    'flv',
    'vob',
    'ogv',
    'ogg',
    'drc',
    'gif',
    'gifv',
    'mng',
    'avi',
    'mts',
    'm2ts',
    'mov',
    'qt',
    'wmv',
    'yuv',
    'rm',
    'rmvb',
    'viv',
    'asf',
    'amv',
    'mp4',
    'm4p',
    'm4v',
    'mpg',
    'mp2',
    'mpeg',
    'mpe',
    'mpv',
    'm2v',
    'svi',
    '3gp',
    '3g2',
    'mxf',
    'roq',
    'nsv',
    'f4v',
    'f4p',
    'f4a',
    'f4b',
    # Picture formats
    'png',
    'jpg',
    'jpeg',
    'jfif',
    'exif',
    'tif',
    'tiff',
    'gif',
    'bmp',
    'ppm',
    'pgm',
    'pbm',
    'pnm',
    'webp',
    'heif',
    'avif',
    'ico',
    'tga',
    'psd',
    'xcf',
]

# clamav settings
clamscan_path='/'
clamscan_logs='clamav.log'

#password settings
pass_max='90'
pass_min='7'
pass_warn='7'

admin_groups = 'sudo adm lpadmin sambashare'

bad_software='aircrack-ng deluge gameconqueror hashcat hydra john nmap openvpn qbittorrent telnet wireguard zenmap'

### setup 
def checkIfRoot():
    if os.geteuid() != 0:
        return False

### installations
def installUFW():
    #do a subprocess call to install UFW
    proc = subprocess.Popen('apt-get install -y gufw', shell=True, stdin=None, stdout=open("/dev/null", "w"), stderr=None, executable="/bin/bash")
    proc.wait()

def installClamAV():
    proc = subprocess.Popen('apt-get install -y clamav', shell=True, stdin=None, stdout=open("/dev/null", "w"), stderr=None, executable="/bin/bash")
    proc.wait()
    pass

def installPam():
    proc = subprocess.Popen('apt-get install -y libpam-cracklib', shell=True, stdin=None, stdout=open("/dev/null", "w"), stderr=None, executable="/bin/bash")
    proc.wait()

def installAudit():
    proc = subprocess.Popen('apt-get install -y auditd', shell=True, stdin=None, stdout=open("/dev/null", "w"), stderr=None, executable="/bin/bash")
    proc.wait()
    
def installBum():
    proc = subprocess.Popen('apt-get install -y bum', shell=True, stdin=None, stdout=open("/dev/null", "w"), stderr=None, executable="/bin/bash")
    proc.wait()


### cleaning / securing
def updateUbuntu():
    proc = subprocess.Popen('apt-get install -y libpam-cracklib', shell=True, stdin=None, stdout=open("/dev/null", "w"), stderr=None, executable="/bin/bash")
    proc.wait()
def updateBrowser():
    pass
def findAndRemoveMediaFiles():
    EXCLUDE_DIRECTORY = (   
                            #Windows system directory
                            'Program Files',
                            'Program Files (x86)',
                            'Windows',
                            'AppData',
                            'logs',

    )
    for root, dirs, files in os.walk("/"):
            if any(s in root for s in EXCLUDE_DIRECTORY):
                pass
            else:
                for file in files:
                    if file.endswith(EXTENSIONS):
                        TARGET = os.path.join(root, file)
                        try:
                            print("Found media file: " + TARGET)
                            choice = input("Delete file? y/n")
                            if choice == 'y':
                                pass
                            elif choice == 'n':
                                pass
                            else:
                                pass

                        except Exception:
                            continue
def runClamAV():
    pass

def killServices():
    pass

def removeProhibitedSoftware():
    global bad_software
    bad_software = bad_software.split(" ")
    for root, dirs, files in os.walk("/"):
        if any(s in root for s in EXCLUDE_DIRECTORY):
            pass
        else:
            for file in files:
                if file in bad_software:
                    TARGET = os.path.join(root, file)
                    try:
                        print("Found media file: " + TARGET)
                        choice = input("Delete file? y/n")
                        if choice == 'y':
                            pass
                        elif choice == 'n':
                            pass
                        else:
                            pass

                    except Exception:
                        continue

def turnOffGuest():
    pass

def turnOnFirewall():
    pass

def secureKernel():
    pass

def setUID():
    pass

### user and group policy changes
def updatePasswordPolicy():
    pass
def changeUpdatePolicy():
    pass
def findGroupsToChange():
    pass
def changeOrRemoveGroup():
    pass
def removeUnauthorizedUsers():
    pass
def addUser():
    pass
def addNewGroup():
    pass
def checkFilesWithHighPermissions():
    pass




#main menu
def menu():
    #print ascii banner
    print("""
    """)
    #print menu
    print("""
    Note: PLEASE READ THE README AS WELL AS THE FORENSIC QUESTIONS FIRST BEFORE STARTING THE SCRIPT!!!\nWARNING: FILES NEEDED IN FORENSIC QUESTIONS MAY CHANGE BECAUSE OF THE SCRIPT
    
    INSTALLING PROGRAMS                        CLEANING UP / SECURING                         POLICY CHANGES
    1. Install UFW                             1. 
    2. Install ClamAV
    3. Install Auditd
    4. Install 
    x. Install anything else

    99. Exit
    """)

   
#need a while choice does not equal a number (!)
    choice = input(">")
    if choice == "1":
        pass
    elif choice == "2":
        pass
    elif choice == "3":
        pass
    elif choice == "4":
        pass
    elif choice  == "5":
        pass
    elif choice  == "6":
        pass
    elif choice == "7":
        pass
    elif choice == "8":
        pass
    elif choice  == "99":
        print("Exiting the program... Have Fun!")
        exit()
    else: 

#main function for executable
if __name__ == "__main__":
    if checkIfRoot():
        menu()
    else:
        print('Please run this file as root!!! USE SUDO! Terminating...')
        exit()