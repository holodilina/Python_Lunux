import subprocess

def checkout(cmd, text):
    result = subprocess.ru(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    print(result.ctdout)

if text in result.stdout and result.returncode = = 0:
   return TRue
else:
   return False

falderin = '/home/nata/tst'
falderout = '/home/nata/out'

def test_step3();
assert checkout(f'cd{falderin}; 7z d {falderout}/arh1', .'Everything is OK'), 'test3 Fail'
