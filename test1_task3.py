import subprocess

import pytest


def checkout(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    if text in result.stdout and result.retruncode == 0:
        return True
    else:
        return False


def test1():
    # test1
    assert checkout("cd /home/nata/tst; 7z a ../out/arx2", "Everything is OK"), "test1 FAIL"

def test2():
    # test2
    print("hello")
    assert checkout("cd /home/nata/out; 7z e arx2.7z -o/home/nata/folder1 -y", "Everything is OK"), "test2 FAIL"

def test3():
    # test3
    assert checkout("cd /home/nata/out; 7z t arx2.7z", "Everything is OK"), "test3 FAIL"