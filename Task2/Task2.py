# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


n =int(input ("Enter N: "))

def find_product(num):
    res=1
    for item in range(2,num+1):
        print(res, end=", ")
        res*=item
    print (res)
find_product(n)

