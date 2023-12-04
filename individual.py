# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from datetime import datetime


def get_person():
    """
    Запросить данные о человеке.
    """
    person = {}
    person["surname"] = input("Введите фамилию: ")
    person["name"] = input("Введите имя: ")
    person["zodiac"] = input("Введите знак зодиака: ")
    person["birthday"] = input("Дата рождения (число.месяц.год):").split(".")
    return person


def display_people(people):
    """
    Отобразить список людей.
    """
    if people:
        line = "+-{}-+-{}-+-{}-+-{}-+-{}-+".format(
            "-" * 4, "-" * 30, "-" * 30, "-" * 20, "-" * 20
        )
        print(line)
        print(
            "| {:^4} | {:^30} | {:^30} | {:^20} | {:^20} |".format(
                "№", "Фамилия", "Имя", "Знак зодиака", "Дата рождения"
            )
        )
        print(line)

        for idx, person in enumerate(people, 1):
            print(
                "| {:>4} | {:<30} | {:<30} | {:<20} | {:>20} |".format(
                    idx,
                    person.get("surname", ""),
                    person.get("name", ""),
                    person.get("zodiac", ""),
                    ".".join(person.get("birthday", "")),
                )
            )
        print(line)
    else:
        print("Список пуст")


def select_people(surname, people):
    """
    Выбрать людей с заданной фамилией.
    """
    result = []
    for i in people:
        if i.get("surname", "") == surname:
            result.append(i)
    return result


def get_instructions():
    print("add - добавление нового человека")
    print("info - данные о человеке по его фамилии")
    print("exti - завершение программы")
    print("list - вывод информации о всех людях")


def main():
    """
    Главная функция программы.
    """
    people = []

    while True:
        command = input("Введите команду (add, info, list, exit, help): ").strip().lower()

        match command:
            case "exit":
                break
            
            case "add":
                person = get_person()
                people.append(person)
                people.sort(
                    key=lambda x: datetime.strptime(".".join(x["birthday"]), "%d.%m.%Y")
                )

            case "info":
                surname = input("Введите фамилию: ")
                selected = select_people(surname, people)
                display_people(selected)

            case "list":
                display_people(people)

            case "help":
                get_instructions()

            case _:
                print(f"Неизвестная команда {command}", file=sys.stderr)

if __name__ == "__main__":
    main()