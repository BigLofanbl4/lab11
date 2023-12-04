#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def get_input():
    return input()


def test_input(n):
    try:
        if int(n):
            return True
    except ValueError:
        return False


def str_to_int(string):
    return int(string)


def print_int(num):
    print(num)


if __name__ == "__main__":
    inp = get_input()
    if test_input(inp):
        print_int(str_to_int(inp))
    else:
        print("Incorrect input")
