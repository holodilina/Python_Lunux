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


def test_step1():
    # test1
    assert checkout(cmd:f"cd {folder_tst}; 7z a ../out/arx2", "Everything is OK"), "test1 FAIL"

def test_step2():
    # test2
    assert checkout(cmd:f"cd {folder_out}; 7z e arx2.7z {folder_ext}", "Everything is OK"), "test2 FAIL"

def test_step3():
    # test3
    assert checkout(cmd:f"cd {folder_out}; 7z t arx2.7z", "Everything is OK"), "test3 FAIL"

def test_step4():
    # test4
    assert checkout(cmd:f"cd {folder_out}; 7z u arx2.7z", "Everything is OK"), "test4 FAIL"

def test_step5():
    # test5
    assert checkout(cmd:f"cd {folder_out}; 7z d arx2.7z", "Everything is OK"), "test5 FAIL"


