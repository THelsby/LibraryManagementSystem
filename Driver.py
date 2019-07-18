running = True
itemStock = []
users = []

while running:
    userType = int(input("Select the option from the table below\n"
                         "1: Admin\n"
                         "2: User\n"
                         "3: Terminate Program\n"))

    if userType == 1:
        from LibraryManagmentSystem import AdminFunctions as AF
        AF.start()
    elif userType == 2:
        from LibraryManagmentSystem import UserFunctions as UF
        UF.start()
    elif userType == 3:
        print("Program Terminated\n")
        running = False
    else:
        print("Invalid input type a correct digit\n")
