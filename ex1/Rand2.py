
import random
a = int(input("Enter First Number:"))
b = int(input("Enter second Number:"))
evenList = []
if(a%2==1):
 num = random.choice(range(a+1,b,2))
if (a%2==0):
 num = random.choice(range(a,b,2))
 
evenList.append(num)

    
print(evenList)
