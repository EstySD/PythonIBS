import threading
import time

def countdown(name):
    print(f"{name} начал выполнение")
    for i in range(10, 0, -1):
        print(f"{name}: {i}")
        time.sleep(1)
    print(f"{name} завершил выполнение")

thread1 = threading.Thread(target=countdown, args=("Поток 1",))
thread2 = threading.Thread(target=countdown, args=("Поток 2",))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Оба потока завершили выполнение.")
