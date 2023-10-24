#!/usr/bin/env python3

import math


def happy_new_year():
    counter = 10
    while counter > 0:
        print(counter)
        counter -=1
    print("Happy New Year!")

def fizzbuzz_printer():
    for num in range(100):
        print(fizzbuzz(num))


def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num

def reverse_string(str):
    reversed_str = ""
    for char in str:
        reversed_str = char + reversed_str
    return reversed_str

def square_integers(int_list):
    return [num**2 for num in int_list]

