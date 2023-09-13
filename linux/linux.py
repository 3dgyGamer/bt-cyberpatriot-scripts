import os
import subprocess

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

def installSSH():
    pass



### cleaning
def update():
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


### policy changes
def updatePasswordPolicy():
    pass

def findGroups():
    pass



#main menu
def menu():
    #print ascii banner
    print("""
    """)
    #print menu
    print("""
    
    
    
    """)
#main function for executable
if __name__ == "__main__":
    if checkIfRoot():
        menu()
    else:
        print('Please run this file as root!!! USE SUDO! Terminating...')
        exit()