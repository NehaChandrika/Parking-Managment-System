parking = []
print("Welcome")
a = int(input("Enter the total number of parking slot that are available: "))
for k in range(a):
    parking.append(0)  

while True:
    op = str(input("Enter in for parking\nEnter out for moving out from the parking slot\nEnter exit to Exit the program\n: "))
    if op == "exit":
        print("EXIT")
        break
    vech = int(input("Please, Enter your vehicle number in terms of natural number only: "))

    if op == "in":
        for i in range(len(parking)):
            if parking[i] == 0:
                print("Please park your vehicle at parking slot: ", i + 1)
                parking[i] = vech
                break
        else:
            print("The slots are full, Sorry :)")
            

    elif op == "out":
        for j in range(len(parking)):
            if parking[j] == vech:
                print("The vehicle is free from the slot.", j + 1)
                parking[j] = 0
                break
        else:
            print("You did not park the vehicle.")


    else:
        print("Please Enter a valid input.")












        
