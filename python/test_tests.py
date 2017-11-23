from File_Manip import File_Manipy

def test_getFileName():
    assert getFileName("gg/hello\something/file.exe") == "file.exe"