import random

n=int(input("Enter the size: "))

my_list=list(range(0,n))

for el in range(0,n):
    j=random.randint(0,n-1)
    my_list[j],my_list[el]=my_list[el],my_list[j]
print(my_list)