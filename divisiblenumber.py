# 1) Ask the user to enter the numerator and store it in `numn`.
numn = int(input ("enter numn"))
# 2) Ask the user to enter the denominator and store it in `numd`.
numd = int(input("enter numd"))
# 3) Check if `numn` is divisible by `numd`:
if numn%numd==0:
# - Find the remainder when `numn` is divided by `numd`.
 print("\n" +str(numn)+ " is divisible  by"+str(numd))
else:
 print("\n" +str(numn)+ " is not divisible  by"+str(numd))
# - If the remainder is 0, it means perfectly divisible.

# 4) If divisible, print that `numn` is divisible by `numd`.

# 5) Otherwise, print that `numn` is not divisible by `numd`.
