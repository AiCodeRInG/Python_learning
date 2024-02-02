import os
def add_new_user(name: str, phone: str, filename: str):
    """
    Добавляет нового пользователя
    :param name: Имя пользователя
    :param phone: Номер телефона
    :param filename: Название файла
    """
    with open(filename, 'a+', encoding='utf-8') as file:
        file.seek(0)
        line_count = len(file.readlines())
        file.write(f"{'\n' if line_count > 0 else ''}{line_count+1};{name};{phone}")


def read_all(filename) -> str:
    """
    Выводит все данные
    :param filename: название файла
    :return: Возвращает все содержимое телефонной книги
    """

    with open(filename, 'r', encoding="utf-8") as file:
        result = file.read()
    return result

def search_user(data: str, filename) -> str:
    """
    Поиск записи по критерию data.
    :param data:
    :return: запись
    """
    with open(filename, 'r', encoding='utf-8') as file:
        result = [line for line in file.readlines() if data.lower() in line.lower()]
        return ''.join(result) if result else 'Вхождений не найдено'


def check_file(filename):
    if not (filename in os.listdir()):
        with open(filename, 'w') as file:
            file.write("")


def copy_line_to_file(filename, to_filename, line_number) -> str:
    """
    Копирование записи в сторонний файл
    :param filename: Файл источник
    :param to_filename: Файл приемник
    :param line_number: Номер строки
    :return: Текстовый результат работы
    """
    with open(filename, 'r', encoding='utf-8') as source_file:
        lines = source_file.readlines()
        if line_number > len(lines):
            return 'Введенный номер строки отсутствует.'
        open_mode = 'a+' if to_filename in os.listdir() else 'w+'
        with open(to_filename, open_mode, encoding='utf-8') as target_file:
            line = lines[line_number-1]
            target_file.write(line)
            return 'Запись скопирована.'


def get_file_content(filename) -> str:
    if filename in os.listdir():
        with open (filename, 'r', encoding='utf-8') as file:
            return ''.join(file.readlines())
    else:
        return 'Файл не найден'

INFO_STRING = """
Выберите режим работы
1 - Вывести все данные
2 - Добавление нового пользователя
3 - Поиск
4 - Копировать строку в файл
5 - Просмотр содержимого файла
0 - Выход
"""

FILENAME = 'phonebook.txt'

check_file(FILENAME)

while True:
    mode = int(input(f'{INFO_STRING}Ваш выбор: '))
    if mode == 1:
        print(read_all(FILENAME))
    elif mode == 2:
        add_new_user(input('Имя пользователя: '), input('Номер телефона: '), FILENAME)
    elif mode == 3:
        print(search_user(input('Введите строку для поиска: '), FILENAME))
    elif mode == 4:
        line_number = input('Номер копируемой записи: ')
        if not line_number.isnumeric():
            print('Ошибка ввода номера строки')
            continue
        print(copy_line_to_file(FILENAME, input('Целевой файл: '), int(line_number)))
    elif mode == 5:
        print(get_file_content(input('Введите название файла: ')))
    elif mode == 0:
        break
