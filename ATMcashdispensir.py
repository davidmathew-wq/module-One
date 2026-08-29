print("ATM cash Dispenser ===\n")
total_100 = total_50 = total_20 = total_10 =total_5 =total_1 = 0
customers_served = 0
total_dispensed = 0

serving =True
while serving: 

    name = input("enter customer name: ")
amount = int(input("hello {name}! Enter withdrawal amount:"))
if amount <= 0:
    print("invalid amount.please enter a positive number.\n")
print("\nDispensing{amount} units for {name}:")
remaining = amount
idx = 1
while idx <= 6:
    if idx == 1: value = 100
    elif idx == 1 : value = 50
    elif idx == 1 : value = 20
    elif idx == 1 : value = 10
    elif idx == 1 : value = 5
    else: value = 1
    coun
        
