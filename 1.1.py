# Задание 1.
# Условие:
# Написать функцию на Python, которой передаются в качестве параметров команда и текст.
# Функция должна возвращать True, если команда успешно выполнена и текст найден в её выводе и False в противном случае. 
# Передаваться должна только одна строка, разбиение вывода использовать не нужно.


def check_output(command, text):
    import subprocess
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
        
        if text in output:
            return True
        else:
            return False
    except subprocess.CalledProcessError:
        return False

# Пример использования функции
command = "ls"  # Пример команды
text = "file.txt"  # Пример текста

result = check_output(command, text)
print(result)
