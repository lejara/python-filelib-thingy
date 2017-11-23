import File_Manip

def test_getFileName():
    assert File_Manip.File_Manipy.getFileName("gg/hello\something/file.exe") == "file.exe"