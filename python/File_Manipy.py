import sys,os


def getFileName(pathName):
    """ returns filename when path is given regardless of slash types or OS file directory type"""
    return os.path.basename(os.path.normpath(pathName))

def getFileSize(pathName):
    """gets size of file, if it's an absolute path it'll find the file specifed otherwise it's a relative path and it will use a sub directory"""
    if(os.path.isabs(pathName)):
        return os.path.getsize(pathName)
    else:
        fn = os.path.join(os.path.dirname(__file__), 'pathName')
        return os.path.getsize(fn)

