
even_list=[]
a=int(input("Please Enter First Number : "))
b=int(input("Please Enter Second Number : "))
for i in range(a,b+1):
    if i%2==0:
        even_list.append(i)
print(even_list)
