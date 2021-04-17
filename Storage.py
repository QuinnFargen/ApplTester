
import os
from datetime import datetime

# Set Directory
def setdirectory():
    if os.name == 'posix':
        os.chdir('/Users/quinnfargen/Documents/GitHub/ApplTester')
    elif os.name == 'nt':
        os.chdir('C:\\Users\\Quinn\\Desktop\\AppTester')
    return os.getcwd()


# Make temp folder
def maketempfolder(Path):
    if os.name == 'posix':
        folder = '/tempCurrentApp'
    elif os.name == 'nt':
        folder = '\\tempCurrentApp'
    tempfolder = Path + folder
    if os.path.exists(tempfolder):
        os.rmdir(tempfolder)
    os.makedirs(tempfolder)
    return tempfolder


# Rename Folder with AppID and Datetime
def renametempfolder(Portfolio, Path, AppID):
    if os.name == 'posix':
        folder = '/tempCurrentApp'
        slash = '/'
    elif os.name == 'nt':
        folder = '\\tempCurrentApp'
        slash = '\\'
    now = datetime.now()  # current date and time
    date_time = now.strftime("%m%d%y_%H%M%S")
    os.chdir(Path)
    tempfolder = Path + folder
    newfolder = Path + slash + Portfolio +  '_AppID_' + str(AppID) + '_' + date_time
    if os.path.exists(tempfolder):
        os.rename(tempfolder, newfolder)
    return newfolder
