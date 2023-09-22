import paramiko

import subprocess

import pytest

# Функция для выполнения команды по SSH
def run_ssh_command(hostname, username, password, command):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname, username=username, password=password)
    stdin, stdout, stderr = client.exec_command(command)
    output = stdout.read().decode('utf-8')
    client.close()
    return output


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
    assert checkout("cd /home/nata/out; 7z t arx2.7z", "Everything is OK"), "test3 FAIL"import subprocess


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

# Подключение по SSH
hostname = 'example.com'
username = 'your_username'
password = 'your_password'

# Шаг 1. Проверка соединения с сервером
output = run_ssh_command(hostname, username, password, 'echo "Connection Successful"')
print(output)

# Шаг 2. Создание директории
output = run_ssh_command(hostname, username, password, 'mkdir test_directory')
print(output)

# Шаг 3. Переход в созданную директорию
output = run_ssh_command(hostname, username, password, 'cd test_directory')
print(output)

# Шаг 4. Создание файла внутри директории
output = run_ssh_command(hostname, username, password, 'touch test_file.txt')
print(output)

# Шаг 5. Проверка существования файла
output = run_ssh_command(hostname, username, password, 'ls test_file.txt')
print(output)

# Шаг 6. Удаление созданных файлов и директорий
output = run_ssh_command(hostname, username, password, 'rm test_file.txt')
print(output)

output = run_ssh_command(hostname, username, password, 'cd .. && rm -r test_directory')
print(output)

