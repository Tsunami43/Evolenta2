# python3.11.6

# Import the necessary packages
from consolemenu import *
from consolemenu.items import *


# Create the menu
title = "Калькулятор"
subtitle = "a [выберете действие] b :"
menu = ConsoleMenu(title=title, subtitle=subtitle)


# Input value(a) and value(b)
def custom_decorator(func):

    def input_a_b():
        try:
            a = float(input("Введите число a: "))
            b = float(input("Введите число b: "))
            # Operation calling
            return func(a, b)

        except Exception as ex:
            menu.subtitle = f"Ошибка ввода! Повторите попытку...\n{subtitle}"
            return ex

    return input_a_b


@custom_decorator
def summary(a, b):
    menu.subtitle = f"Последняя операция - {a} + {b} = {a+b}\n{subtitle}"


@custom_decorator
def difference(a, b):
    menu.subtitle = f"Последняя операция - {a} - {b} = {a-b}\n{subtitle}"


@custom_decorator
def multiplication(a, b):
    menu.subtitle = f"Последняя операция - {a} * {b} = {a*b}\n{subtitle}"


@custom_decorator
def division(a, b):
    menu.subtitle = f"Последняя операция - {a} / {b} = {a/b}\n{subtitle}"


# Create menu items
items = [
    FunctionItem("Сумма (+)", summary),
    FunctionItem("Разница (-)", difference),
    FunctionItem("Произведение (*)", multiplication),
    FunctionItem("Частное (/)", division),
]

# Append items in menu
[menu.append_item(item) for item in items]

# Show menu
menu.show()
