import File_Manip

def test_getFileName():
    assert getFileName("gg/hello\something/file.exe") == "file.exe"