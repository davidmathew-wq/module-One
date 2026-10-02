def  cube (number):
    total = number**3
    print("cube of", number,":",total)
    if  total % 2 == 0:
        print(total,"even number")
    else:
        print(total,"odd number")


cube(6)