n=int (input("Enter n: "))
mylist=[]
sum =0

for a in range(1,n+1):
    elem=round ((1+(1/a))**a,2)
    mylist.append(elem)
    sum+=elem
print (mylist)
print (sum)
