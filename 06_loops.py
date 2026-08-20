#multiplicaion table
"""n = int(input("Enter the digit you want : "))
for i in range(1,11):
    print(n , "X" , i , "=" ,n*i)

#******************************using while loop*********************************
n = int(input("Enter the digit you want : "))
num = 0
while num<=10:
    print(n , "X" , num , "=" ,n*num)
    num += 1

#---------------------------------------------------------------------------------------------
#guess secret number
secret_num = 67
for i in str(secret_num):
    i = int(i)
while True:
    n = int(input("Guess the secret number : "))
    if n != secret_num:
        print("TRY AGAIN")
    else:
        print("YOU GUESSED IT RIGHT")
        break

#-------------------------------------------------------------------------------------------------
#cube of numbers----------->>>>let the user decides
numbers = []
cubes = []
n = int(input("enter how many numbers you want to add in list : "))
for i in range(n):
    num = int(input("enter a number : "))
    cube = num**3
    numbers.append(num)
    cubes.append(cube)
print(numbers)
print(f"cube of {numbers} is : ",cubes)

#------------------------------------------------------------------------------------------------
#perfect number
num = int(input("Enter a number : "))
total = 0
for i in range(1,num):
    if num % i == 0:
        total = total+i

if num == total:
    print("perfect number")
else:
    print("not a perfect number")

#-------------------------------------------------------------------------------------------------
#LCM
res = []
res2 = []
n1 = int(input("enter a number : "))
n2 = int(input("enter a second number : "))
multiples = int(input(f"Enter how many multiples of {n1} and {n2} you want : "))
for i in range(1,multiples+1):
    res.append(n1*i)
    res2.append(n2*i)
print(f"multiples of {n1} are : ",res)
print(f"multiples of {n2} are : ",res2)

for i in res:
    if i in res2:
        print(f"LCM of {n1} and {n2} is : ",i)
        break

#----------------------------------------------------------------------------------------------------
#factorial
product = 1
n = int(input("Enter a number : "))
for i in range(n,0,-1):
    product = product*i
print(f"factorial of {n} is : ",product)

#---------------------------------------------------------------------------------------------------
#spy number ____________sum of digits is equal to product of digits
number = 1124
total = 0
for i in str(number):
    i = int(i)
    total += i
print(f"sum of {number} is : ",total)

product = 1
for i in str(number):
    i = int(i)
    product = product*i
print(f"product of {number} is : ",product)
if total == product:
    print(f"{number} is a spy number")
else:
    print(f"{number} is not a spy number")"""
