import time

counter = 0  # инициализация счетчика повторений

with open('output.log', 'a') as f:  # открываем файл для добавления сообщений в лог
    while True:
        counter += 1
        log_message = f"Приложение работает. Повторение №{counter}\n"
        print(log_message)  # вывод в стандартный вывод (stdout)
        f.write(log_message)  # запись в файл output.log
        time.sleep(1)  # ожидание 1 секунда
        if counter >= 10:
            print("Приложение завершено")  # вывод в стандартный вывод (stdout)
            f.write("Приложение завершено")  # запись в файл
            break
