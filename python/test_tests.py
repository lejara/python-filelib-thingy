import File_Manipy

def test_getFileName():
    assert File_Manipy.getFileName("gg/hello\something/file.exe") == "file.exe"
    
def test_getFileSize1():
    assert File_Manipy.getFileSize("test_file.txt") == 43