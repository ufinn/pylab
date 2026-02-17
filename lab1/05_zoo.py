#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# есть список животных в зоопарке

zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]

# посадите медведя (bear) между львом и кенгуру
#  и выведите список на консоль
# TODO здесь ваш код
zoo = zoo[:1] + ["bear"] + zoo[1:]
print(zoo)
# добавьте птиц из списка birds в последние клетки зоопарка
birds = ['rooster', 'ostrich', 'lark', ]
#  и выведите список на консоль
# TODO здесь ваш код
zoo = zoo + birds
print(zoo)
# уберите слона
#  и выведите список на консоль
# TODO здесь ваш код
zoo = zoo[:3] + zoo[4:]
print(zoo)
# выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
# Номера при выводе должны быть понятны простому человеку, не программисту.
# TODO здесь ваш код
for i in range(len(zoo)):
    if zoo[i] == "lion":
        k = i
    if zoo[i] == "lark":
        j = i
print(f"жаворонок в клетке ", j+1, f"\n лев в клетке ", k+1)


