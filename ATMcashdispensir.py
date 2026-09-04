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
     count = remaining // value
     if count > 0:
      print(" {count} x {value}-unit note(s) = {count * value}")
      remaining -= 
      customers_served += 1
    total_dispensed += amount
    print("transaction complete, {name}!\n")
    again = input("next customer? (yes/no): ").strip().lower()
    if again != "yes":
     serving = False
     print("\n=== Daily denomination report ===")
     for slot in range(1,7):
        if slot == 1: value, total = 100, total_100
        elif slot == 2: value, total = 50, total_50
        elif slot == 3: value, total = 20, total_20
        elif slot == 4: value, total = 10, total_10
        elif slot == 5: value, total = 5, total_5
        else: value, total = 1, total_1
        if total > 0:
           print("  {value}-unit notes dispensed : {total}", end="")
           for note in range (total):
              print("=", end="")
              print()
              print("\ncustomers served : {customers_served}")
              print("total dispensed : {total_dispensed} units")
              print("ATM session closed. goodbye!")
              
        

        
