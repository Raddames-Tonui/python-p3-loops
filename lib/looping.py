#!/usr/bin/env python3

def happy_new_year():
    i = 10;
    while i > 0:
        print(i)
        i -= 1
    if i == 0:
        print("Happy New Year!")
    return i 
happy_new_year()


def square_integers(int_list):
    squared_int = [squared * squared for squared in int_list]
    return squared_int

y = square_integers([1, 2, 3, 4, 5])
print(y)

def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 ==0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
    return i

fizzbuzz()
