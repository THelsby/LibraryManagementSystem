from LibraryManagmentSystem import LibraryObjects as LO

itemStock = []
users = []


def checkStock():
    if not itemStock:
        print("Currently no stock\n")
    else:
        for item in itemStock:
            print("ID - {}\nType - {}\nTitle - {} \n".format(item.id, item.type, item.title))


def checkOutItem(id):
    if not itemStock:
        print("Currently no stock to remove\n")
    else:
        for item in itemStock:
            if item.id == id:
                if item.checkedIn:
                    item.checkedOutItem()
                    print(item.checkedIn)
                else:
                    print("Item already checked out\n")


def checkInItem(id):
    if not itemStock:
        print("Currently no stock to remove\n")
    else:
        for item in itemStock:
            if item.id == id:
                item.checkedInItem()
                print(item.checkedIn)


def registerUser(fName, sName):
    id = 1
    users.append(LO.Person(id, fName, sName))
    id = id + 1
    print("Account successfully created")
