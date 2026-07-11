print("welcome to ride biker")
print("step_1 chose your vehicle")
print("1.bike 2.car")
ch= int(input("enter 1 or 2: "))
if ch == 1:
    print("step_2 chose your bike type")
    print("1. scooty 2. mountain bike ")
    bike_types= int(input("enter 1 or 2: "))
    if bike_types==1:
        print("you pick scooty")
    else:
        print("you pick mountain bike")
else:
      print("step_2 chose your car type")
      print("1. land cruiser 2. tesla ")
      car_types= int(input("enter 1 or 2: "))
      if car_types==1:
        print("you pick land cruiser")
      else:
        print("you pick tesla")