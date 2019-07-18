class LibraryItem():
    def __init__(self, id, type, title, checkedIn=True):
        self.id = id
        self.type = type
        self.title = title
        self.checkedIn = checkedIn

    def checkedOutItem(self):
        self.checkedIn = False

    def checkedInItem(self):
        self.checkedIn = True


class Book(LibraryItem):

    def __init__(self, id, title, author):
        super().__init__(id, "Book", title)
        self.author = author


class Map(LibraryItem):

    def __init__(self, id, title, age):
        super().__init__(id, "Map", title)
        self.age = age


class NewsPaper(LibraryItem):

    def __init__(self, id, title, date):
        super().__init__(id, "NewsPaper", title)
        self.age = date


class Person:
    def __init__(self, id, fName, sName):
        self.id = id
        self.fName = fName
        self.sName = sName
