from LibraryManagmentSystem import LibraryFunctions as libfunctions


def start():
    running = True
    while running:
        entryChoice = int(input("What task would you like to perform?\n"
                                "1: Check book out\n"
                                "2: Check book In\n"
                                "3: Check all stock\n"
                                "4: Register with the library\n"
                                "5: Return to account selection\n"
                                "Enter the digit for the entry you want\n"))
        if entryChoice == 1:
            libfunctions.checkOutItem(int(input("Enter item you would like to check out\n")))
        elif entryChoice == 2:
            libfunctions.checkInItem(int(input("Enter item you would like to check in\n")))
        elif entryChoice == 3:
            libfunctions.checkStock()
        elif entryChoice == 4:
            libfunctions.registerUser(input("Enter first name\n"), input("Enter second name\n"))
        elif entryChoice == 5:
            running = False
            print("Program Terminated\n")
        else:
            print("Invalid input please use a valid digit\n")