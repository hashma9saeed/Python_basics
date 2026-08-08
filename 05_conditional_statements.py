#Profit/Loss
cost_price = int(input("Enter the cost price of product : "))
selling_price = int(input("Enter the selling price of product : "))
profit = selling_price - cost_price
loss = cost_price - selling_price
if selling_price > cost_price:
    profit = selling_price - cost_price
    print(f"You have a profit of {profit}")
elif cost_price > selling_price:
    loss = cost_price - selling_price
    print(f"You have a loss of {loss}")
else:
    print("No profit, no loss")

#-----------------------------------------------------------------------------------------
#Voting eligibility
age = int(input("Enter your age : "))
if age >= 18:
    print("you are eligible to vote")
else:
    print("you are not eligible")

#-----------------------------------------------------------------------------------------
#Shipping charges
shipping_charges = 300
amount = int(input("Enter the total shopping amount : "))
quantity = int(input("Enter the quantity of items you bought : "))
if amount >= 20000 and quantity >= 10:
    print("No shipping charges")
else:
    bill = amount+shipping_charges
    print("Your bill is : ",bill)
print("**************Thanks for shopping*****************")

#-----------------------------------------------------------------------------------------
#Hotel reservation
room = input("Enter room type (single/double/suite): ").lower()
nights = int(input("Enter number of nights: "))
if room == "single":
    price = 2000
elif room == "double":
    price = 3500
elif room == "suite":
    price = 6000
else:
    print("Invalid room type")
    price = 0
if price > 0:
    total = price * nights
    print("Total reservation cost:", total)

#-----------------------------------------------------------------------------------------
#ATM simulation
balance = 60000
user = input("Enter valid PIN: ")
if user.isdigit() and len(user) == 6:
    print("*****WELCOME*****")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Your current balance is:", balance)

    elif choice == 2:
        deposit = int(input("Enter the amount you deposited: "))
        new_balance = balance + deposit
        print("Your balance after deposit is:", new_balance)

    elif choice == 3:
        amount = int(input("Enter the withdrawn amount: "))

        if amount <= balance:
            new_balance = balance - amount
            print("Your balance is:", new_balance)
        else:
            print("Insufficient balance")

    elif choice == 4:
        print("Exit")

    else:
        print("Invalid choice")
else:
    print("Invalid PIN")

#--------------------------------------------------------------------------------------