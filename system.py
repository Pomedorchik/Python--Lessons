import os
import sys
import platform


os_name = platform.system()
os_version = platform.version()
architecture = platform.architecture()[0]
computer_name = platform.node()
current_folder = os.getcwd()
python_version = sys.version


system_info = [
    os_name,
    os_version,
    architecture,
    computer_name,
    current_folder,
    python_version
]


def write(text):
    sys.stdout.write(text + "\n")


def read():
    return sys.stdin.readline().strip()


while True:
    write("\n=== Openings OS ===")
    write("1. Название операционной системы")
    write("2. Версия операционной системы")
    write("3. Архитектура системы")
    write("4. Имя компьютера")
    write("5. Текущая папка")
    write("6. Версия Python")
    write("0. Выход")
    write("Выберите пункт: ")

    choice = read()

    if choice == "1":
        write("\nОперационная система:")
        write(system_info[0])

    elif choice == "2":
        write("\nВерсия операционной системы:")
        write(system_info[1])

    elif choice == "3":
        write("\nАрхитектура системы:")
        write(system_info[2])

    elif choice == "4":
        write("\nИмя компьютера:")
        write(system_info[3])

    elif choice == "5":
        write("\nТекущая папка:")
        write(system_info[4])

    elif choice == "6":
        write("\nВерсия Python:")
        write(system_info[5])

    elif choice == "0":
        write("\nПрограмма завершена.")
        break

    else:
        write("\nТакого пункта нет.")