from colorama import Fore, init
from datetime import datetime
import zipfile
import os
import platform

init(autoreset=True)

class Lego:
    __initialized = False

    @staticmethod
    def __check_init():
        if not Lego.__initialized:
            print(Fore.RED + "[Ошибка] Сначала вызови Lego.init() перед использованием других функций!")
            Lego.log_event("Error! No init!", level="ERROR")
            raise RuntimeError("Lego.init() не был вызван")

    @staticmethod
    def log_event(message="init called", file_name="logs.txt", level="INFO"):
        now = datetime.now()
        time_str = now.strftime("%H:%M")
        date_str = now.strftime("%-d/%m/%y")
        line = f"[{level.upper():<5}] {time_str:<10} {date_str:<10} {message}\n"
        with open(file_name, "a") as f:
            f.write(line)

    @staticmethod
    def init(debug=False):
        print(Fore.RED + "#_# Initialization...")
        if os.path.exists("logs.txt"):
            print(Fore.GREEN + "✓ logs.txt exists.")
        else:
            print(Fore.YELLOW + "× logs.txt not found! Creating...")
            with open("logs.txt", "w") as f:
                f.write("## log file, version: 5.2.15\n")
            print(Fore.GREEN + "✓ logs.txt created.")
            Lego.log_event("logs.txt created")

        if debug and not os.path.exists("debug.txt"):
            with open("debug.txt", "w") as f:
                pass
            print(Fore.GREEN + "✓ debug.txt created!")
            Lego.log_event("debug.txt created (debug=True)")

        with open("LeCache.json", "w"):
            print(Fore.CYAN + "LeCache был создан!")
            Lego.log_event("LeCache is was create!")

        Lego.log_event("Initialization complete.")
        print(Fore.BLUE + "#_# Initialization complete.")
        Lego.__initialized = True

    @staticmethod
    def add(file_name, value):
        Lego.__check_init()
        if os.path.exists(file_name):
            print(Fore.GREEN + f"✓ {file_name} найден! Записываю данные в него!")
        else:
            print(Fore.RED + f"Файл '{file_name}' не найден! Создаю!")
            Lego.log_event(f"File '{file_name}' is created!", level="INFO")
        with open(file_name, "w") as f:
            f.write(value)
        print(Fore.CYAN + "✓ Содержимое было успешно записано!")

    @staticmethod
    def remove_file(file_name):
        Lego.__check_init()
        if os.path.exists(file_name):
            os.remove(file_name)
            print(Fore.GREEN + f"✓ Файл '{file_name}' был успешно удалён!")
            Lego.log_event(f"File '{file_name}' was removed.", level="INFO")
        else:
            print(Fore.RED + f"× Файл '{file_name}' не найден!")
            Lego.log_event(f"File '{file_name}' not found!", level="ERROR")

    @staticmethod
    def copyring(first_file, double_file):
        Lego.__check_init()
        if os.path.exists(first_file) and os.path.exists(double_file):
            with open(first_file, "r") as f1:
                reador = f1.read()
                if not reador:
                    print(Fore.RED + f"Файл {first_file} пустой!")
                else:
                    print(Fore.CYAN + f"Идет копирование файла\n" +
                          Fore.YELLOW + f"первый файл: {first_file}\n" +
                          Fore.GREEN + f"второй файл: {double_file}")
                    with open(double_file, "w") as ff2:
                        ff2.write(reador)
                    print(Fore.GREEN + "✓ Копирование файлов успешно завершено!")
                    Lego.log_event(f"Копирование файла '{first_file}' в '{double_file}' завершено.")
        else:
            print(Fore.RED + f"Файлы '{first_file}' и/или '{double_file}' не найдены!")
            Lego.log_event(f"Ошибка: отсуствие файлов '{first_file}' или '{double_file}'", level="ERROR")

    @staticmethod
    def read_log(clear=False):
        Lego.__check_init()
        if os.path.exists("logs.txt"):
            with open("logs.txt", "r") as f:
                print("\n" + f.read())
            Lego.log_event("logs.txt прочитан")
            if clear:
                with open("logs.txt", "w") as f:
                    print(Fore.GREEN + "✓ logs.txt был очищен (clear=True)")
                    Lego.log_event("logs.txt очищен")

    @staticmethod
    def zip_load(storage_file):
        Lego.__check_init()
        if not os.path.exists(storage_file):
            print(Fore.RED + f"× Файл '{storage_file}' не найден!")
            Lego.log_event(f"Ошибка: файл '{storage_file}' не найден!", level="ERROR")
            return

        print(Fore.GREEN + f"✓ Файл '{storage_file}' найден! Идет сжатие...")
        Lego.log_event("Начало сжатия файла...")

        system = platform.system().lower()
        plat_str = platform.platform().lower()

        if "windows" in system or "darwin" in system:
            output_dir = os.path.join(os.path.expanduser("~"), "Documents")
        elif "linux" in system and "android" in plat_str:
            output_dir = "/storage/emulated/0/Download"
        else:
            output_dir = "."

        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, "zooper.zip")

        with zipfile.ZipFile(output_path, "w") as f:
            f.write(storage_file, arcname=os.path.basename(storage_file))

        print(Fore.CYAN + f"✓ Зипирование завершено! Файл сохранён в: {output_path}")
        Lego.log_event(f"Файл '{storage_file}' заархивирован в '{output_path}'")

    @staticmethod
    def set_array(file, array, setjoin=False):
        Lego.__check_init()
        if os.path.exists(file):
            print(Fore.GREEN + f"✓ Файл '{file}' найден. Проверка массива...")
            Lego.log_event(f"Проверка массива перед записью в '{file}'")

            if isinstance(array, list):
                print(Fore.CYAN + "✓ Массив подтверждён. Идёт запись...")
                with open(file, "a") as f:
                    if not setjoin:
                        f.write(str(array) + "\n")
                        print(Fore.GREEN + f"✓ Запись завершена. Тип: полный список.")
                    else:
                        f.write(", ".join(map(str, array)) + "\n")
                        print(Fore.GREEN + f"✓ Запись завершена. Тип: через запятую.")
                Lego.log_event(f"Массив записан в '{file}' (setjoin={setjoin})")
            else:
                print(Fore.RED + "× Ошибка: передан не список!")
                Lego.log_event("Ошибка: аргумент не является списком!", level="ERROR")
        else:
            print(Fore.RED + f"× Файл '{file}' не найден!")
            Lego.log_event(f"Файл '{file}' не найден при попытке записи массива", level="ERROR")
            
    def getsize(file_name):
        if os.path.exists(file_name):
            bite = os.path.getsize(file_name)
            return Fore.CYAN + f"размер файла (в байтах): {bite}"
        else:
            print(Fore.RED + f"файл {file} не найден, или имя было введено неправильно!")
