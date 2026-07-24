#swapping of two variables
"""a = 24
b = 1234
print("values of a,b before swapping : " ,"a :", a, " b : " ,b)
a,b = b,a
print("values of a,b after swapping : " ,"a :", a, " b : " ,b)"""


#conversion of data types
"""user = int(input("enter an integer : "))
print(type(user))
user = float(user)
print(user)
print(type(user))"""


#finding area of rectange
"""len = float(input("enter a length of rectangle : "))
width = float(input("enter a width of rectangle : "))
area = len*width
print("Area of rectangle is : ",area)"""



#calculate BMI
"""print("CALCULATING BODY MASS INDEX")
weight  = int(input("enter your weight in kg : "))
height = float(input("enter your height in meters : "))
hei = height*2
bmi = weight/hei
print(bmi)
if bmi < 18.5:
    print("you are underweight")
elif  18.5 >= bmi < 24.9:
    print("you are healthy")
else:
    print("you are obese")"""


#finding average of five numbers                               
"""num = [1,2,67,5,12]                                      
sum=0                                                                
for i in num:                                                       
    sum = sum+i
print("average of five numbers is : ",sum/len(num))"""


#in case you want user to give numbers seprately
"""num = []
for i in range(5):
    numbers = int(input("enter a number : "))
    num.append(numbers)
print(num)"""


#calculating simple interest(SI = (P*R*T)/100)
"""principle = float(input("enter a original amount : "))
rate = int(input("enter rate of interet per year : "))
time = float(input("enter time in years"))
mul = principle*rate*time
si = mul/100
print(si)"""


#convert temperature(C__F)
"""c = int(input("enter a temperature in celcius : "))
print("CELCIUS : ",c)
f = c*(9/5)+32
print("temperature after converting in farenheit : ",f)"""


#time conversion
#second__minutes
"""sec = int(input("enter a seconds you want to convert into minutes : "))
minutes = sec/60
print(minutes)
#seconds__hours
hours = sec/3600
print(hours)"""


#salary after tax deduction
"""salary = int(input("enter your current salary : "))
tax_rate = 10
if salary > 50000:
    deduc = (salary*10)/100
else:
    deduc = 0
print("your current salary is : ",salary-deduc)"""


#currency conversion
"""exchange_rate = 285
#PKR__USD
USD = int(input("enter USD : "))
PKR = USD*exchange_rate
print(PKR)
#PKR__USD
PKR = int(input("enter PKR : "))
USD = PKR/exchange_rate
print(USD)"""


#discount calculator
"""discount_percentage = 15
amount = int(input("enter the amount customer shopped of : "))
if amount > 500000:
    discount = (amount*discount_percentage)/100
else:
    discount = 0

final = amount - discount
print("yuor final price after discount is : ",final)"""


#finding ASCCI value (order())
"""character = input("enter a character : ")
value = ord(character)
print(value)"""


#convert days into months/years
#1 year = 365 days
#1 month = 30 days
"""days = int(input("enter number of days : "))
year = days//365
remaining_days = days%365
month = remaining_days//30
remain_days = remaining_days%30
print("years : ",year)
print("months : ",month)
print("days : ",remain_days)"""



#EMI calculator
"""interest_rate = 20
user = int(input("enter a loan amount : "))
annual_interest_rate = interest_rate/100               #incase of monthly(interest_rate/12/100)
payment = int(input("enter number of monthly payments : "))
formula = (1+annual_interest_rate)**payment
calcula = (user*annual_interest_rate*formula)/(formula-1)
print("your EMI is : ",calcula)"""


#compound interest calculator
"""interest_rate = 10
P = int(input("enter the starting amount : "))
T = int(input("enter time in years : "))
A = P*(1+interest_rate/100)**T
C = A-P
print("compound interest is : ",C)"""


#time converter 
#use division while going to larger value from smaller one.
#use multiplication while goimg to smaller from larger one.
"""print("1. Hours to minutes")
print("2. Minutes to seconds")
print("3. Hours to seconds")

choice = input("Enter your choice: ")

if choice == "1":
    hours = int(input("Enter hours: "))
    minutes = hours * 60
    print("Minutes:", minutes)

elif choice == "2":
    minutes = int(input("Enter minutes: "))
    seconds = minutes * 60
    print("Seconds:", seconds)

elif choice == "3":
    hours = int(input("Enter hours: "))
    seconds = hours * 3600
    print("Seconds:", seconds)

else:
    print("Invalid choice")"""



#decimal precision       (how many digits you want after a decimal)
"""num = float(input("enter a number : "))
a  = round(num,3)
print(a)"""


#binary decimal
"""remainder = []
user = int(input("enter a decimal number : "))

while user != 0:
    num = user%2
    remainder.append(num)
    nume = user//2
print(remainder[::-1])
for i in remainder[::-1]:
    print(i,end = "")"""

#scientific notation calculator
"""num = float(input("enter a number : "))
n = int(input("enter an integer : "))
if num <= 10:
    res = num*(10**n)
    print(f"{num} X 10^{n} = {res}")
else:
    print("invalid input")"""



#arthimetic calculator
"""a = int(input("enter a number : "))
b = int(input("enter a second number : "))
#print("1. addition")
#print("2.subtraction")
#print("3.multiplication")
#print("4.floor division")_____// gives quotient
#print("5.modulus division")____% gives remainder
choice = int(input("choose operation : "))
if choice == 1:
    print(a+b)
elif choice == 2:
    print(a-b)
elif choice ==3:
    print(a*b)
elif choice == 4:
    print(a//b)
elif choice == 4:
    print(a%b)
else:
    print("invalid choice")"""


#even/odd
"""user = int (input("enter a number : "))
if user%2==0:                                   
    print("its an even number")
else:
    print("it is an odd number")"""

#divisible by 5
"""num = int(input("enter a number : "))
if num%5==0:
    print("yes! the number is divisible by 5")
else:
    print("no! its not divisible by 5")"""

#positive number, negative number, zero
"""num = int(input("enter a number : "))
if num > 0:
    print(*"positive number")
elif num < 0:
    print("negative number")
else:
    print("zero , neither positive nor negative")"""


#square
"""num = int(input("enter a number : "))
sq = num**2
print(f"square of {num} is : ",sq)"""

#cube
"""num = int(input("enter a number : "))
sq = num**3
print(f"cube of {num} is : ",sq)"""

#power
"""num = int(input("enter a number : "))
user = int(input(f"how many time you want to multiply {num} : "))
power = num**user
print(power)"""



#greatest of two
a = 4
b = 5
if a > b:
    print(a)
else:
    print(b)


#leap year
"""year = int(input("enter year you want to check for leap year : "))
if (year%4==0 and year%100!=0) or (year%400==0):
    print("its a leap year")
else:
    print("its not a leap year")"""

#age calculator
"""year  = int(input("enter the year you were born in : "))
current_year = int(input("enter the current year : "))
age = current_year-year
print("your current age is : ",age)"""

#bitwise operations
#a = 10
#b = 6
#print(a&b) ___and
#print(a|b)____or
#print(a^b)___xor
#print(a>>2)___left shift
#print(b<<3)__right shift

#swapping two varaibles
a  = 10
b = 68
print("before conversion : ",a,b)
a,b = b,a
print("after conversion : ",a,b)































































