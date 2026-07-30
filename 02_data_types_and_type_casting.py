#Conversion of data types

a = "289"
print(a)
print("type of 'a' before conversion : ",type(a))
a = int(a)
print("type of 'a' after conversion : ",type(a))


#-----------------------------------------------------------------------------------------
#Find ASCII value

char = input("Enter a character : ")
ascii_value = ord(char)
print(f"ASCII value of {char} is : {ascii_value}")

#---------------------------------------------------------------------------------------

#Convert days into years/months
days = int(input("Enter number of days : "))
year = days//365
remaining = days%365
month = remaining//30
remaining_days = remaining%30
print("YEARS : " ,year)
print("MONTHS : " ,month)
print("DAYS : " ,remaining_days)

#-------------------------------------------------------------------------------------------

#Time converter

# Smaller unit → Larger unit : Divide (/)
# Larger unit → Smaller unit : Multiply (*)

print("1. Hours to minutes ")
print("2. Minutes to seconds ")
print("3. Hours to seconds ")

choice = int(input("Enter your choice : "))
if choice == 1:
    hour = int(input("Enter hours : "))
    minutes = hour*60
    print("MINUTES : " , minutes)

elif choice == 2:
    minutes = int(input("Enter minutes : "))
    seconds = minutes*60
    print("SECONDS : " , seconds)

elif choice == 3:
    hour = int(input("Enter hours : "))
    seconds = hour*3600
    print("SECONDS : " , seconds)

else:
    print("Invalid choice")

#-------------------------------------------------------------------------------------------
#Decimal precision

# round(num, 4) -> Rounds the value but doesn't always display 4 decimal places.
# {num:.4f} -> Displays the value with exactly 4 decimal places.

num = float(input("Enter a decimal value : "))
print(f"Round the {num} to 4 decimal places  : {num:.4f}")
#or
num = float(input("enter a decimal value : "))
value = round(num,4)
print(f"Round the {num} to 4 decimal places : {value}")

#------------------------------------------------------------------------------------------

#Scientific Notation converter
num = float(input("Enter a number : "))
print(f"Scientific Notation : {num:e}")

#-------------------------------------------------------------------------------------------
#Binary to decimal conversion
remainder = []
num = int(input("Enter a number : "))
while num != 0:
    user = num%2
    remainder.append(user)
    num = num//2
print(remainder[::-1])
for i in remainder[::-1]:
    print(i , end = "")
print()

#-----------------------------------------------------------------------------------------

#Binary to decimal conversion:
binary = input("Enter a binary number : ")
decimal = 0
power = len(binary)-1
for num in binary:
    decimal += int(num)* (2**power)
    power -= 1
print("DECIMAL VALUE : " , decimal)
# Built-in method:
# decimal = int(binary, 2)
# Example:
# binary = "1010"
# decimal = int(binary, 2)   # Output: 10