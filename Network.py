import requests
from colorama import Fore, init
from ftplib import FTP
import socket
from LegoTik import Lego
from io import BytesIO

init(autoreset=True)

class Network:
    @staticmethod
    def download(url, file, stream=True):
        try:
            response = requests.get(url, stream=stream)
            if response.status_code == 200:
                total_size = int(response.headers.get('Content-Length', 0))
                downloaded = 0
                chunk_size = 8192
                print(Fore.CYAN + "Скачивание началось!")
                print(Fore.YELLOW + "Загрузка содержимого будет постепенной!")
                with open(file, "wb") as f:
                    for chunk in response.iter_content(chunk_size=chunk_size):
                        if chunk:
                            f.write(chunk)
                            downloaded += len(chunk)
                            if total_size:
                                percent = (downloaded / total_size) * 100
                                print(Fore.BLUE + f"Размер: {total_size} байт | Скачано: {downloaded} байт ({percent:.2f}%)", end='\r')
                print()
                print(Fore.GREEN + f"\nСодержимое источника '{url}' было успешно загружено в файл '{file}'!")
            else:
                print(Fore.RED + f"Ошибка: получен статус-код {response.status_code}")
        except FileNotFoundError:
            print(Fore.RED + f"Файл '{file}' не найден!")
        except requests.exceptions.RequestException as e:
            print(Fore.RED + f"Ошибка при загрузке: {e}")

class FTPS:
    @staticmethod
    def connect(addr, user="anonymous", passw="anonymous@"):
        try:
            ftp = FTP()
            ftp.connect(host=addr, port=21, timeout=10)
            print(Fore.YELLOW + f"Соединение установлено с {addr}, отправляем логин...")
            Lego.log_event("Sending login to FTP-server...", level="NOTICE")
            ftp.login(user=user, passwd=passw)
            print(Fore.GREEN + "Успешный вход! Отправка команды NOOP...")
            Lego.log_event("Successfully! Sending command NOOP...", level="NOTICE")
            response = ftp.voidcmd("NOOP")
            print(Fore.CYAN + f"Сервер ответил: {response}")
            Lego.log_event(f"Reply from FTP-server: {response}")
            print(Fore.GREEN + "Соединение активно. Используйте возвращённый объект для работы.")
            Lego.log_event("Connect successfully!")
            return ftp
        except socket.gaierror as e:
            print(Fore.RED + f"[gaierror] Код: {e.errno}, Сообщение: {e.strerror}")
        except socket.error as e:
            print(Fore.RED + f"[socket error] Код: {e.errno}, Сообщение: {e.strerror}")
        except Exception as e:
            print(Fore.RED + f"[ошибка] {e}")
        return None

    @staticmethod
    def complete(con):
        try:
            if con:
                print(Fore.YELLOW + "Объект FTP-сервера найден! Завершаем соединение...")
                Lego.log_event("Wait complete...")
                response = con.quit()
                print(Fore.GREEN + "Работа с FTP-сервером завершена!")
                Lego.log_event("Working is complete!")
                Lego.log_event(f"Ответ сервера: {response}")
            else:
                print(Fore.RED + "Ошибка: объект подключения не передан!")
                Lego.log_event("error: no FTP object")
        except Exception as e:
            print(Fore.RED + f"Произошла ошибка завершения!\n{e}")
            Lego.log_event(f"Exception in complete(): {e}")
            
    @staticmethod
    def read_file(file, direct, ftp):
        try:
            looncil = ftp.voidcmd("NOOP")
            print(Fore.CYAN + f"Сервер ответил: {looncil}")
            ftp.cwd(direct)
            chose = input("Загрузить текст в файл? (Y/n): ").lower()
            if chose == "y":
                with open(file, "wb") as f:
                    ftp.retrbinary(f"RETR {file}", f.write)
                print(Fore.GREEN + f"Текст был успешно записан в файл '{file}'")
            elif chose == "n":
                buffer = BytesIO()
                ftp.retrbinary(f"RETR {file}", buffer.write)
                buffer.seek(0)
                content = buffer.read().decode(errors="ignore")
                print(Fore.YELLOW + "\nВот содержимое файла:\n")
                print(content)
            else:
                print(Fore.RED + "Выбор не распознан! Отменено.")
        except Exception as e:
            print(Fore.RED + f"Произошла ошибка при чтении файла!\n{e}")