#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Разработать терминал, принимающий команды от пользователя.
Использовать модуль os.
"""

import os


def show_list():
    print("/version - узнать версию Python")
    print("/browser or /internet - открыть браузер")
    print("/findfile - прочитать файл")
    print("/size - узнать размер файла")
    print("/dir - узнать текущую директорию")


def main():
    # запуск цикла для выполнения команд
    while True:

        request = input("Введите /help: ")

        if request == "/help":
            show_list()

        # завершить работу терминала
        if request == "exit":
            exit()

        # узнаем версию нашего python
        elif request == "/version":
            command = "Python --version"
            os.system(command)

        # открываем браузер
        elif request in ["/browser", "/internet"]:
            os.startfile(r"C:\Users\DNS\AppData\Local\Yandex\YandexBrowser\Application\browser.exe")
            input()

        # делаем поиск файла, указав путь, если путь неверный - вывести ошибку
        elif request == "/findfile":
            filename = input("Введите путь к файлу: ")
            if os.path.exists(filename):
                print("Указанный файл существует")
            else:
                print("Файл не существует")

        # узнаем размер нашего файла
        elif request == "/size":
            print(os.path.getsize(r"C:\Users\DNS\laba17\tasks\individual1.txt"))

        # узнаем текущий каталог
        elif request == "/dir":
            print(os.getcwd())


if __name__ == "__main__":
    print("TerminalOS 1.0")
    main()