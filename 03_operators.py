
# Even/odd

num = int(input("Enter a number : "))
if num%2 == 0:
    print("This is an even number")
else:
    print("This is an odd number")

#----------------------------------------------------------------------------------------
#Check for positive, negative and zero

num = int(input("Enter a number : "))
if num < 0:
    print("Negative number")
elif num == 0:
    print("Zero")
else:
    print("Positive number")

#-----------------------------------------------------------------------------------------
#Age calculator

birth_year = int(input("Enter your year of birth : "))
current_year = int(input("Enter the current year : "))
if birth_year > current_year:
    print("invalid birth year")
else:
    age = current_year-birth_year
    print("Your current age is : ",age)


#----------------------------------------------------------------------------------------
#Leap year formula

year = int(input("Enter year you want to check : "))
if (year%4 == 0 and year%100 != 0) or (year%400 == 0):
    print("It is a leap year")
else:
    print("Not a leap year")

#----------------------------------------------------------------------------------------
#Square,cube and power

num = int(input("enter a number : "))
power_value = int(input(f"Enter the power for {num}: "))
square = num**2
cube = num**3
power = num**power_value
print(f"square of {num} is : ",square)
print(f"cube of {num} is : ",cube)
print(f"power of {num} is : ",power)

#------------------------------------------------------------------------------------------

#Bitwise operations
a = 10
b = 6
print(a&b)           #AND
print(a|b)           #OR
print(a^b)           #XOR
print(a>>2)          #RIGHT SHIFT
print(b<<3)          #LEFT SHIFT

#----------------------------------------------------------------------------------------

#Greatest of two numbers
#Built-in method: print(max(num1, num2))

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
    print("Greatest number is:", num1)
else:
    print("Greatest number is:", num2)

#--------------------------------------------------------------------------------------

#Smallest of two numbers
# Built-in method: print(min(num1, num2))
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 < num2:
    print("Smallest number is:", num1)
else:
    print("Smallest number is:", num2)


#------------------------------------------------------------------------------------------

