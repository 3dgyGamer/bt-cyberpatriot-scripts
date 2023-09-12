import os


edia_files_raw= [
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
    pass

### installations
def installUFW():
    pass

def installClamAV():
    pass

def installPam():
    pass

def installSSH():
    pass
### cleaning


### policy changes
def updatePasswordPolicy():
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
        print('Please run this file as root!. Terminating...')
        exit