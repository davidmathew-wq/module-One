secret_number = 37
hearts = 5
print(" Number Guessing Game")
print("You have 5 hearts ")
print()
while hearts > 0:
    guess = int(input("Enter your guess: "))
    if guess < 1 or guess > 50:
        print("Please enter a number from 1 to 50.")
        continue
    if guess == secret_number:
        print(" You got it! You win")
        break
    hearts -= 1
    difference = abs(secret_number - guess)
    if difference <= 2:
        print(" Hot")
    elif difference <= 5:
        print(" Warm")
    elif difference <= 10:
        print(" Cold")
    else:
        print("Very cold")
    print("Wrong guess You lost heart ")
    print("Hearts left:", hearts)
    print()
else:
    print(" Game over")
    
  
   