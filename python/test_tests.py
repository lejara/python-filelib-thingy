import File_Manipy

def test_getFileName():
    assert File_Manipy.getFileName("gg/hello\something/file.exe") == "file.exe"
    
