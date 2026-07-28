#Temperature conversion
celsius = float(input("enter the temperature in celsius : "))
fahrenheit = (celsius*9/5)+32
print("Temperature after conversion : ",fahrenheit)

#----------------------------------------------------------------------------------------

#Calculate Simple Interest
rate = float(input("enter the annual interest_rate : "))
principal = float(input("enter the principal amount : "))
time = int(input("enter time in years : "))
res = (principal*rate*time)
si = res/100
print("SIMPLE INTEREST : ", si)

#--------------------------------------------------------------------------------------

#Calculate BMI
weight = int(input("enter your weight in kg : "))
height = float(input("enter your height in meters : "))
bmi = weight/(height**2)
print("your BMI is : ",bmi)

#---------------------------------------------------------------------------------------

#find out the average of five numbers
total = 0
num = [1,67,16,50,77]
for i in num:
    total= total+i
print("Average of five numbers is : ",total/len(num))
#let the user decides
num = []
total = 0
for i in range(5):
    numbers = int(input("enter a numbers you want for finding average : "))
    num.append(numbers)
    total = total+numbers
print(num)
print(total)
print("average of five numbers is : " , total/len(num))

#---------------------------------------------------------------------------------------

#second conversion
sec = int(input("enter a seconds you want to convert : "))
minutes = sec/60
hours = sec/3600
print("MINUTES : ",minutes)
print("HOURS : ",hours)

#---------------------------------------------------------------------------------------

#salary after tax deduction
tax = 10
salary  = int(input("enter your salary : "))
if salary > 50000:
    deduc = (salary*tax)/100
else:
    deduc = 0
print("your current salary is : ",salary-deduc)

#--------------------------------------------------------------------------------------

#currency converter
exc_rate = 285
#PKR__USD
pkr = int(input("enter an amount in pkr : "))
usd = pkr/exc_rate
print("After converting to USD : ",usd)
#USD___PKR
usd = int(input("enter an amount in usd : "))
pkr = usd*exc_rate
print("After converting to PKR: ",pkr)

#---------------------------------------------------------------------------------------
 
