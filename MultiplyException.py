try:
    num1 = int(input("enter the first number:"))
    num2 = int(input("enter the second number:"))
    result = num1 / num2
    print("result is", result)
except ZeroDivisionError:
    print("division by zero is error ||")
except ValueError:
    print("please enter valid whole numbers")
except:
    print("wrong input")
else:
    print("no exceptions")
finally:
    print("this will excute no matter what")