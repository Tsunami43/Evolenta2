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

# Create menu items
items = [
    FunctionItem(
        "Сумма (+)",
        input,
        ["Введите число a:"]
    ),
    FunctionItem(
        "Разница (-)",
        input,
        ["Введите число a:"]
    ),
    FunctionItem(
        "Произведение (*)",
        input,
        ["Введите число a:"]
    ),
    FunctionItem(
        "Частное (/)",
        input,
        ["Введите число a:"]
    )
]

# Append items in menu
[menu.append_item(item) for item in items]

# Show menu
menu.show()
