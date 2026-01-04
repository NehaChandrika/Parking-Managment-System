parking = []
print("Welcome")

a = int(input("Enter the total number of parking slots available: "))
for k in range(a):
    parking.append(0)

print(
    "\nEnter 'in' for parking"
    "\nEnter 'out' for moving out"
    "\nEnter 'Exit' to Exit"
)

while True:
    op = input("\nYour choice: ")

    if op == "Exit":
        print("EXIT")
        break

    elif op == "in":
        if 0 not in parking:
            print("The slots are full, Sorry :)")
            continue

        while True:
            vehicle = input("Enter your vehicle number (natural number): ")
            if vehicle.isdigit() and int(vehicle) > 0:
                vehicle = int(vehicle)
                break
            else:
                print("Enter valid number only")

        if vehicle in parking:
            print("Vehicle already parked!")
            continue

        for i in range(len(parking)):
            if parking[i] == 0:
                print("Please park your vehicle at slot:", i + 1)
                parking[i] = vehicle
                break

    elif op == "out":
        if all(x == 0 for x in parking):
            print("No vehicles are parked currently.")
            continue

        while True:
            vehicle = input("Enter your vehicle number (natural number): ")
            if vehicle.isdigit() and int(vehicle) > 0:
                vehicle = int(vehicle)
                break
            else:
                print("Enter valid number only")

        for j in range(len(parking)):
            if parking[j] == vehicle:
                print("Vehicle removed from slot:", j + 1)
                parking[j] = 0
                break
        else:
            print("This vehicle is not parked here.")

    else:
        print("Please enter a valid input.")







        
