while True:
    print("\n--- SMART WASTE SORTING SYSTEM ---")
    print("1. Food Waste")
    print("2. Plastic")
    print("3. Paper")
    print("4. Metal")
    print("5. Hazardous Waste")
    print("6. Exit")

    choice = input("Enter waste type (1-6): ")

    if choice == "1":
        print("Category: Biodegradable")
        print("Bin: GREEN")

    elif choice == "2":
        print("Category: Plastic")
        print("Bin: BLUE")

    elif choice == "3":
        print("Category: Paper")
        print("Bin: YELLOW")

    elif choice == "4":
        print("Category: Metal")
        print("Bin: GREY")

    elif choice == "5":
        print("Category: Hazardous")
        print("Bin: RED")

    elif choice == "6":
        print("Waste Sorting System Stopped!")
        break

    else:
        print("Invalid Input! Please try again.")

