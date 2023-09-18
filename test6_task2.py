from lib_checkout import checkout_negativ

folder_tst = " /home/nata/tst"
folder_out = " /home/nata/out"
folder_ext = " /home/nata/folder1"

def checkout(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    print(result.stdout)
    if text in result.stdout and result.retruncode == 0:
        return True
    else:
        return False

def test_1():
    # test1
    res1 = checkout(cmd:f"cd {folder_tst}; 7z a ../out/arx2 text_file.txt", text:"Everything is OK")
    res2 = checkout(cmd:f"ls {folder_out}, text:"arx2.7z"
    assert res1 and res2, "test_1 FAIL"

def test_2():
    # test2
    res1 = checkout(cmd:f"cd {folder_out}; 7z e arx3.7z -o{folder_ext}", text:"Everything is OK")
    res2 = checkout(cmd:f"ls {folder_ext}, text:"test_file.txt"
    assert res1 and res2, "test_2 FAIL"

def test_3():
    # test3
    assert checkout(cmd:f"cd {folder_out}; 7z t arx2.7z", "Everything is OK"), "test_3 FAIL"
