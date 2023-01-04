# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

def split(s):
    return [int(item) for item in s]

def read_file():
    file = open("text.txt", "r")
    array = file.read()
    b = split(array)
    file.close()
    return b

b = read_file()

def rezult_array_multi(ar):
    try:
        array = []
        number = int(input("Введите  число N: "))
        multi = 1
        if number < 0:
            print("Введите целое положительное число!")
        for n in range(-number, number+1):
            array.append(n)
        print(f"Содержание файла = {ar}")
        print(f"Созданный список от -N до N = {array}")
        for item in range(len(ar)):
            for j in range(len(array)):

                if ar[item] == j:
                    multi *= array[j]

    except ValueError:
        print("Вы ввели не то, введите целое число")
        rezult_array_multi(ar)
    return multi

print(f"Наш результат = {rezult_array_multi(b)}")