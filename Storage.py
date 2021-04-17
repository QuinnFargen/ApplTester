
import os
from datetime import datetime

# Set Directory


def setdirectory():
    os.chdir('C:\\Users\\Quinn\\Desktop\\AppTester')
    return os.getcwd()


# Make temp folder
def maketempfolder(Path):
    tempfolder = Path + '\\tempCurrentApp'
    if os.path.exists(tempfolder):
        os.rmdir(tempfolder)
    os.makedirs(tempfolder)
    return tempfolder


# Rename Folder with AppID
def renametempfolder(Path, AppID):
    now = datetime.now()  # current date and time
    date_time = now.strftime("%m%d%y_%H%M%S")
    os.chdir(Path)
    tempfolder = Path + '\\tempCurrentApp'
    newfolder = Path + '\\' + 'AppID_' + str(AppID) + '_' + date_time
    if os.path.exists(tempfolder):
        os.rename(tempfolder, newfolder)
    return newfolder
