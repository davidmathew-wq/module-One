# 1) Ask the user to enter marks for 4 subjects: math, english, science, and hindi.
math=int(input("enter math mark "))
science=int(input("enter science mark "))
english=int(input("enter english mark "))
hindi=int(input("enter hindi mark "))
# Store each mark in its own variable.

# 2) Add all 4 subject marks and store the total in `sum`.
sum=math+science+hindi+english
# 3) Print the total marks stored in `sum`.
print("total sum",sum)
# 4) Calculate the percentage:
P=(sum/400)*100
# - Divide `sum` by 400 (total maximum marks for 4 subjects, assuming each is out of 100)

# - Multiply the result by 100

# Store the final value in `perc`.

# 5) Print the percentage stored in `perc`.
print("PERCENTAGE",P)