parking = []
print("Welcome")
rows = int(input("Enter no.of Rows : "))
column = int(input("Enter no.of Column : "))
for i in range(rows):
    temp = []
    for j in range(column):
        temp.append("Empty")
    parking.append(temp)

print(
    "\nEnter 'in' for parking"
    "\nEnter 'out' for moving out"
    "\nEnter 'display' for to see the parking slots" 
    "\nEnter 'Exit' to Exit"
)

while True:
    op = input("\nYour choice: ")

    if op == "exit":
        print("EXIT")
        break
    elif op == "display":
        for el in parking:
            print(el)
    
    elif op == "in":
        full = True
        for i in range(rows):
            for j in range(column):
                if parking[i][j] == "Empty":
                    full  = False
                    break
        if full :            
            print("The slots are full, Sorry :)")
            continue
    
        while True:
            vehicle = input(" \n    Enter your vehicle number (natural number): ")
            if vehicle.isdigit() and int(vehicle) > 0:
                vehicle = int(vehicle)
                break
            else:
                print("Enter valid number only")

        already_parked = False
        for i in range(rows):
            for j in range(column):
                if parking[i][j] == vehicle:
                    already_parked  = True
                    break
        if already_parked :            
            print("Vehicle is already parked")
            continue
        
        park = False
        for i in range(rows):
            for j in range(column):
                if parking[i][j]== "Empty" :
                    print(f"\n Vehicle parked at Row {i + 1}, Column {j + 1}")
                    parking[i][j] = vehicle
                    park = True
                    break
            if park :
                break

    elif op == "out":
        
        while True:
            vehicle = input("\n    Enter your vehicle number (natural number): ")
            if vehicle.isdigit() and int(vehicle) > 0:
                vehicle = int(vehicle)
                break
            else:
                print("Enter valid number only")

        remove = False
        for i in range(rows):
            for j in range(column):
                if parking[i][j]== vehicle :
                    print(f"\n Vehicle removed from Row {i + 1}, Column {j + 1}")
                    parking[i][j] = "Empty"
                    remove = True
                    break
            if remove:
                break
        else:
            print("This vehicle is not parked here.")

    else:
        print("Please enter a valid input.")