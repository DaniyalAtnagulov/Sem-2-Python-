# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

def sum():
    number=input("Enter your number: ")
    result=0
    for digit_in_num in number:
        if digit_in_num.isdigit():
            result+=int(digit_in_num)
    print (result)

sum()

