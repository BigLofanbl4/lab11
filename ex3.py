#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def multiply():
    num = int(input("Введите число не равное 0: "))
    res = 1

    while num != 0:
        res *= num
        num = int(input("Введите число или 0, чтобы закончить: "))
    return res


if __name__ == "__main__":
    print(multiply())
