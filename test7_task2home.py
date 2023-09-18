import subprocess

folder_tst = " /home/nata/tst"
folder_out = " /home/nata/out"
folder_ext = " /home/nata/folder1"

def checkout(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    if text in result.stdout and result.retruncode == 0:
        return True
    else:
        return False


def test_1():
    # test1
    assert checkout(cmd:f"cd {folder_tst}; 7z a ../out/arx2", "Everything is OK"), "test_1 FAIL"

def test_2():
    # test2
    assert checkout(cmd:f"cd {folder_out}; 7z e arx2.7z {folder_ext}", "Everything is OK"), "test_2 FAIL"

def test_3():
    # test3
    assert checkout(cmd:f"cd {folder_out}; 7z t arx2.7z", "Everything is OK"), "test_3 FAIL"

def test_4():
    # test3
    assert checkout(cmd:f"cd {folder_out}; 7z l arx2.7z", "Everything is OK"), "test_4 FAIL"

