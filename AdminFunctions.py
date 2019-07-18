from LibraryManagmentSystem import LibraryFunctions as libfunctions
from LibraryManagmentSystem import LibraryObjects as LO
from enum import Enum
import json

idCounter = 1


class LibraryItem(Enum):
    book = createBook()
    map = LO.Map(2, "World", "14-09-1994")
    newspaper = LO.NewsPaper(3, "The Sun", "14-09-1993")
    idCounter = idCounter + 1


def start():
    adminRunning = True
    while adminRunning:
        startInput = int(input("What task would you like to perform?\n"
                               "1: Add items to stock\n"
                               "2: Add users to system\n"
                               "3: Check all stock\n"
                               "4: Check all users\n"
                               "5: Update item\n"
                               "6: Remove item\n"
                               "7: Update user\n"
                               "8: Remove user\n"
                               "9: Print items to file\n"
                               "10: Read in items from file\n"
                               "11: Return to account selection\n"
                               "Enter the digit for the entry you want\n"))
        if startInput == 1:
            addItems()
        elif startInput == 2:
            print("Add user function\n")
        elif startInput == 3:
            libfunctions.checkStock()
        elif startInput == 4:
            checkUsers()
        elif startInput == 5:
            updateItem(int(input("Enter id of item you want to update\n")), input("Enter new title you want to set\n"))
        elif startInput == 6:
            removeItem(int(input("Enter the id of the item you want to remove\n")))
        elif startInput == 7:
            updateUser(int(input("Enter the id of the user you want to update\n")), input("Enter the new first name "
                                                                                          "of the user"))
        elif startInput == 8:
            removeUser(int(input("Enter the id of the user you want to remove\n")))
        elif startInput == 9:
            printItemsToFile()
        elif startInput == 10:
            readItemsFromFile()
        elif startInput == 11:
            adminRunning = False
        else:
            print("Invalid input please use a valid digit\n")


def addItems():
    running = True
    while running:
        addItemInput = input("What item would you like to add to the system?\n"
                             "---------------------Options--------------------\n"
                             " - Book\n"
                             " - Map\n"
                             " - Newspaper\n"
                             " - Press 1 to go back to main menu\n"
                             "Enter which item you want to add to the system\n")
        if addItemInput.lower() == "book" or "map" or "newspaper":
            libfunctions.itemStock.append(LibraryItemEnum[addItemInput.lower()].value)
            running = False
        elif addItemInput == "1":
            running = False
        else:
            print("Invalid input was entered\n")


def removeItem(id):
    if not libfunctions.itemStock:
        print("Currently no stock to remove\n")
    else:
        for item in libfunctions.itemStock:
            if item.id == id:
                libfunctions.itemStock.remove(item)


def updateItem(id, title):
    if not libfunctions.itemStock:
        print("Currently no stock to update\n")
    else:
        for item in libfunctions.itemStock:
            if item.id == id:
                item.title = title


def removeUser(id):
    if not libfunctions.users:
        print("Currently no users to remove")
    else:
        for user in libfunctions.users:
            if user.id == id:
                libfunctions.users.remove(user)


def updateUser(id, fName):
    if not libfunctions.users:
        print("Currently no users to update")
    else:
        for user in libfunctions.users:
            if user.id == id:
                libfunctions.users.fName = fName


def checkUsers():
    if not libfunctions.users:
        print("Currently no users\n")
    else:
        for user in libfunctions.users:
            print("ID - {}\nFirst name - {}\nSecond Name - {} \n".format(user.id, user.fName, user.sName))


def printItemsToFile():
    if not libfunctions.itemStock:
        print("Currently no stock to print\n")
    else:
        with open('items.txt', 'w') as file:
            for item in libfunctions.itemStock:
                file.write(json.dumps(convert_to_dict(item)))


def convert_to_dict(obj):
    obj_dict = {}
    obj_dict.update(obj.__dict__)
    return obj_dict


def readItemsFromFile():
    with open("items.txt") as json_file:
        libfunctions.itemStock = json.load(json_file)