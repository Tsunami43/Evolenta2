# python3.11.6

# Import the necessary packages
from consolemenu import *
from consolemenu.items import *


# Create the menu
title = "Калькулятор"
subtitle = "a [выберете действие] b :"
menu = ConsoleMenu(
    title=title,
    subtitle=subtitle
)


def input_a_b():
    try:
        a = float(input("Введите число a:"))
        b = float(input("Введите число b:"))
    except Exception as ex:
        return ex


# Create menu items
items = [
    FunctionItem(
        "Сумма (+)",
        input_a_b
    ),
    FunctionItem(
        "Разница (-)",
        input_a_b
    ),
    FunctionItem(
        "Произведение (*)",
        input_a_b
    ),
    FunctionItem(
        "Частное (/)",
        input_a_b
    )
]

# Append items in menu
[menu.append_item(item) for item in items]

# Show menu
menu.show()
