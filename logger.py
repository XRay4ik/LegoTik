import os

class Logger:
    @staticmethod
    def send_debug(debugger, message):
        debugger = debugger.lower()

        if os.path.exists("debug.txt"):
            with open("debug.txt", "a") as f:
                print("Отладчик был записан в файл debug.txt")
                if debugger == "error":
                    f.write(f"ERROR! An error occurred! Reason: {message}\n")
                elif debugger == "warning":
                    f.write(f"WARNING! {message}\n")
                elif debugger == "notice":
                    f.write(f"NOTICE! {message}\n")
                else:
                    f.write(f"UNKNOWN TYPE [{debugger}]: {message}\n")
        else:
            print("Файл 'debug.txt' не найден или не существует!")
            
    @staticmethod
    def send_in_console(debugger, message):
        debugger = debugger.lower()
        if debugger == "error":
            print(f"ERROR! An error occurred! Reason: {message}")
        elif debugger == "warning":
            print(f"WARNING! {message}")
        elif debugger == "notice":
            print(f"NOTICE! {message}")
        else:
            print(f"{debugger.upper()}! {message}")