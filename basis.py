import threading
import subprocess

def run_file(file_name):
    subprocess.Popen(['python', file_name])
    print(f"Файл {имя_файла} был запущен.")

# Список файлов для запуска
files = ['file1.py', 'file2.py', 'file3.py']

# Запускаем каждый файл в отдельном потоке
threads = []
for file in files:
    thread = threading.Thread(target=run_file, args=(file,))
    thread.start()
    threads.append(thread)

# Продолжаем выполнение основной программы без ожидания завершения потоков
print("Discord бот и другие файлы были запущены.")
