#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import pi


def cylinder(rad, h):
    circle = lambda rad: pi * rad**2
    command = input("Найти площадь боковой поверхности или полную? (боковой/полную) ").lower()

    match command:
        case "боковой":
            return 2 * pi * rad * h
        case "полную":
            return 2 * circle(rad) + 2 * pi * rad * h


if __name__ == "__main__":
    print(cylinder(float(input("Введите радиус: ")), float(input("Введите высоту: "))))
