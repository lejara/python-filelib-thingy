import os

def getFileName(pathName):
    """ returns filename when path is given regardless of slash types or OS file directory type"""
    return os.path.basename(os.path.normpath(pathName))