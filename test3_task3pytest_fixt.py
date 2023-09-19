import time

class StatFixture:
    def __init__(self, config_file_path):
        self.config_file_path = config_file_path
        self.stat_file_path = "stat.txt"
    
    def _get_file_stats(self):
        # Логика для получения статистики из файла config_file_path
        # Возвращаем пример: количество файлов, размер файла
        return 10, 1024
    
    def _get_cpu_load_stats(self):
        # Логика для получения статистики загрузки процессора из файла /proc/loadavg
        with open("/proc/loadavg", "r") as file:
            cpu_load_stats = file.read()
        return cpu_load_stats
    
    def after_step(self):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
        files_count, file_size = self._get_file_stats()
        cpu_load_stats = self._get_cpu_load_stats()
        
        with open(self.stat_file_path, "a") as file:
            file.write(f"{timestamp}, {files_count}, {file_size}, {cpu_load_stats}\n")

# Пример использования фикстуры после каждого шага теста
stat_fixture = StatFixture("config.txt")

# Шаг 1
# ...

stat_fixture.after_step()

# Шаг 2
# ...

stat_fixture.after_step()

# Шаг 3
# ...

stat_fixture.after_step()

# Результат будет записываться в файл stat.txt в виде строки,
# содержащей время, количество файлов из конфига, 
# размер файла из конфига и статистику загрузки процессора 
# из файла /proc/loadavgи. 
# Каждая запись будет добавлена в новую строку.
