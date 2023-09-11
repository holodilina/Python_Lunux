# Задание 2. (повышенной сложности)
# Доработать функцию из предыдущего задания таким образом, 
# чтобы у неё появился дополнительный режим работы, 
# в котором вывод разбивается на слова с удалением всех знаков пунктуации
# (их можно взять из списка string.punctuation модуля string). 
# В этом режиме должно проверяться наличие слова в выводе.


import string

def word_exists(text):
    # Удаление знаков пунктуации из текста
    text = text.translate(str.maketrans("", "", string.punctuation))
    
    # Разбиение текста на слова
    words = text.split()
    
    # Проверка наличия слова в выводе
    def check_word_exists(word):
        return word in words
    
    return check_word_exists

# Пример использования
check_fn = word_exists("Hello world! How are you?")
print(check_fn("Hello"))  # True
print(check_fn("goodbye"))  # False
