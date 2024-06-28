"""
Author: Brenda Gutierrez
"""
from collections import defaultdict

"""
Book Class: Creates a Book object with the book's name, author, and optionally, status (Checked Out or On Shelf).

Attributes:
    name -- A string of the book's name
    author -- A string of the author's name
    status -- An optional boolean indicating the book's status, either "Checked Out" (False) or "On Shelf" (True). 
              If there is no third argument given when a Book object is created, it has a None value. If a third 
              argument is given, it has a default value of True, meaning that the book is by default "On Shelf." 
"""
class Book: 
    def __init__(self, name, author, status = None):
        """Initializes the Book object with the book's name, author, and optional status attributes."""
        self.name = name
        self.author = author
        self.status = status if status is not None else True

    def __repr__(self):
        """Returns the Book object as a readable string with each of the object's attribute values"""
        return f"Book: {self.name}, Author: {self.author}, Status: {self.status}"

    def returnDict(self):
        """Returns the Book object as a dictionary with "Book," Author" and "Status" as the keys, and the corresponding 
        attributes as the values. For "Status," a string of either "On Shelf" or "Checked Out" is put as the value
        depending on the value of the status attribute. 

        If there is a status for the object or if the status attribute is True, the status string outputs "On Shelf."
        If there is no status for the object or if the status attribute is False, the status string outputs "Checked Out.
        """

        statusM = ""
        if self.status:
            statusM = "On Shelf"
        elif not self.status: 
            statusM = "Checked Out"
        return {'Book': self.name, 'Author': self.author, 'Status': statusM}

    def changeStatus(self, statusMessage):
        """Changes the Book object's status attribute according to the user's input string and returns a string relating to the
        status attribute's value.

        Parameter:
            statusMessage -- An input string from the user at response option 3 that is either "Check out" or "On shelf"

        If the user inputs "Check Out" and the object's status is True, the status attribute of the object becomes False.
        If the user inputs "On Shelf" and the object's status is False, the status attribute of the object becomes True.
        If the user inputs "On Shelf" and the object's status is True, the status attribute is unchanged and the function
        prints out that the book is already "On Shelf."
        If the user inputs something other than "On Shelf" or "Check out," then the functions tells the user the response
        is not one of the options and to try again.
        """
        if (statusMessage == "Check out") and self.status:
            self.status = False
            print("Inventory updated! Please go back to view the new inventory.")

        elif (statusMessage == "On shelf") and not self.status:
            self.status = True
            print("Inventory updated! Please go back to view the new inventory.")

        elif (statusMessage == "On shelf") and self.status:
            print(f'This book is already on the shelf!')

        elif (statusMessage != "On shelf") or (statusMessage != "Check out"):
            print(f'Sorry, that does not match one of the options. Please try again.')
            

        return statusMessage

def checkInput(userInput, checkFlag):
    """Checks that the user input is appropriate and expected according to the menu prompts. Returns a boolean 
    indicating whether or not the input is correct. 

    Parameters:
            userInput -- User input retrieved at menu prompts, specifically before a response is chosen 
                         and at responses 2 and 3.
            checkFlag -- Indicates which check will be done on the userInput. 
                         If checkFlag is 1, then the function will check if the user input is a number between 1-4. 
                         If checkFlag is 2, then the function will check if the user input contains a special character or not. 
                         If the input is either not a number (checkFlag = 1) or contains a special character 
                         (checkFlag = 2), then a print statement will be shown to the user asking to type a valid input.
    """
    isInputCorrect = False

    if checkFlag == 1:
        idealInput = "1234"
        if userInput in idealInput:
            isInputCorrect = True
            pass
        else:
            print("Sorry, that does not match one of the available options. Please type a number that corresponds to what you would like to do.\n")
    
    if checkFlag == 2:
        notInput = "!@#$%^&*()-+?_=,<>/"
      
        if any(char in notInput for char in userInput):
            print("Sorry, that does not match a known response. Please type a response that corresponds to the prompt.")
        else:
            isInputCorrect = True
            pass
        
    return isInputCorrect
    
def createInventory(bookOne, bookTwo, newInventory = None):
    """Creates the inventory with two Book objects and optionally, a dictionary that contains new Book objects. Returns 
    a defaultdict(list) container that contains all Book objects in one dictionary.
    
    Parameters:
        bookOne -- A Book object
        bookTwo -- Another Book object
        newInventory -- An optional dictionary parameter. If no third argument is given, it has a value of None.
                        If a third argument is provided, it contains a dictionary with new user-created Book objects
                        according to response option "2."
    
    First, createInventory() calls the Book objects' class method returnDict() in order to get the objects
    in dictionary form. Then, a defaultdict(list) container is created to contain all of the Book objects in one place.
    The container creates a dictionary-like structure with the keys being the names of the Book object attributes and the keys
    being lists containing the attribute values. 

    The two Book objects' dictionaries are combined into one tuple in order to loop through their contents and add the 
    corresponding key, value pairs into the allBooksDict container. If a newInventory argument is provided, then the 
    function will loop through its key, value pairs and also add them into the allBooksDict container if they share the
    same key.
    """

    book1Dict = bookOne.returnDict()
    book2Dict = bookTwo.returnDict() 
   
    allBooksDict = defaultdict(list)
    for dict in (book1Dict, book2Dict):
            for key, value in dict.items():
                allBooksDict[key].append(value)

    if newInventory:
        for key, value in newInventory.items():
            if key in allBooksDict:
                for valElement in value:
                    allBooksDict[key].append(valElement)         

    return allBooksDict

def addInventory(bookEntered, newInventory):
    """Returns a defaultdict(list) structure containing the information of a user-generated book in response 2.

    Parameters:
        bookEntered -- Book object created by the user in response 2
        newInventory -- A defaultdict(list) structure that contains the book name, author, and status of 
                        user-generated books.
    """
    #Book object's class method returnDict() gets the new Book object into dictionary form
    newBookDict = bookEntered.returnDict()
  
    #Book object's dictionary is looped through to append to the newInventory container
    for key, value in newBookDict.items():
        newInventory[key].append(value)

    return newInventory

def main():
    """Runs main functionality of the program, including the user-facing menu of options to interact with the inventory through the terminal. 
    The user can choose the following options: 
        1) Print out the current book inventory 
        2) Add a new book into the inventory 
        3) Check out or return a book to the shelf
        4) Exit the program
    """

    #Creates the container that will hold any new user-generated Book objects as dictionary-like structure.
    updatedInventory = defaultdict(list)
    #Creates the list that will contain all hard-coded and user-generated Book objects.
    allBookObjects = []


    #The first two Book objects are hard-coded and added to the allBookObjects list
    book1 = Book("Their Eyes Were Watching God", "Zora Neale Hurston")
    allBookObjects.append(book1)
    book2 = Book("Barracoon", "Zora Neale Hurston")
    allBookObjects.append(book2)
 
    print("Welcome to the Bookworm library! What would you like to do today? \nPlease type the corresponding number for what you would like to do:\n")
    
    #Loop runs as long as running is True, which can be turned False through response 4 (Exit)
    running = True
    while running: 

        """If the updatedInventory dictionary is not empty (thus True), then createInventory() will be called and create an inventory with the two
        generated Book objects and updatedInventory. If updatedInventory is empty (thus False), createInventory() will be called and create an inventory 
        with only the two Book objects. 
        """
        if updatedInventory:
            allBooks = createInventory(book1, book2, updatedInventory)
           # allBooks = createInventory(book1, book2, addBook)     
        if not updatedInventory:
            allBooks = createInventory(book1, book2)

        #Offers the 4 response options to the user
        response = input("1 - Print out the current book inventory.\n2 - Add a new book into the inventory.\n3 - Check out or return a book to the shelf.\n4 - Exit\n")
        
        #Checks if the user input is a number between 1-4
        checkInput(response, 1)

        """Response 1: Loops through the allBooks dictionary to print out the keys (strings indicating the Book object attribute names)
        and unpacked values (lists containing Book object attributes values) in readable rows for the user."""

        if response == "1":
            valS = ""
            for key, value in allBooks.items():
                #Contains the key and adds them to the beginning of each row
                titleS = "".join("{:<7}".format(key)) + "|"
                spaceS = ""

                for i in range(0, len(value)):
                    spaceS += "{:<30}"
                #Contains the list value, unpacks their elements, and formats them with spacing
                valS = spaceS.format(*value)

                #Combines the key and value's elements on one line
                print(titleS, valS)

            
        """Response 2: Obtains the user's input for a book name and author that they would like to add to the inventory. Checks the user input
        to see if it has a special character or not. If it does, the user will keep being prompted to add a book name or author until it passes
        the check. If it does not contain a special character, a Book object is created based on the user input and appended to the allBooksObjects 
        list. Then, the object is converted into a dictionary in order to add its information into the updatedInventory dictionary through the
        addInventory() function."""
        if response == "2":
            bookName = input("Please enter the name of the book:\n")

            #Both the book name and author are checked to see if they have a special character or not. 
            while not checkInput(bookName, 2):
                bookName = input("Please enter the name of the book:\n")
            
            bookAuthor = input("Please enter the full name of the author:\n")
            while not checkInput(bookAuthor, 2):
                 bookAuthor = input("Please enter the full name of the author:\n")


            bookEntry = Book(bookName, bookAuthor)
            allBookObjects.append(bookEntry)
            addInventory(bookEntry, updatedInventory)

            print("Book added! Feel free to go back and look at the new inventory.")

        """Response 3: Obtains the user's input for a book name, author, and requested status change based on which book they would
        like to check out or return to the library. Checks the user input to see if it has a special character or not. If it does, 
        the user will keep being prompted to add a book name, author, or response until it passes the check.

        The Book objects in the allBookObjects list are then looped through in order to get their respective attribute values for the
        book name and author.

        If the name of the user-inputted book and the object's name attribute value match, along with the author of the user-inputted book 
        matching the object's author attribute value, then changeBook() is called to change the status of the object according to user input."""
        if response == "3":

            statusBook = input("Type the name of the book you want to check out or put back on the shelf.\n")
            while not checkInput(statusBook, 2):
                statusBook = input("Type the name of the book you want to check out or put back on the shelf.\n")

            statusAuthor = input("Type the name of the author whose book you want to check out or put back on the shelf.\n")
            while not checkInput(statusAuthor, 2):
                 statusAuthor = input("Type the name of the author whose book you want to check out or put back on the shelf.\n")

            statusResponse = input("Type 'Check out' to check out the book or 'On shelf' to return the book back to the shelf.\n")
            while not checkInput(statusResponse, 2):
                statusResponse = input("Type 'Check out' to check out the book or 'On shelf' to return the book back to the shelf.\n")
            
            for obj in allBookObjects:
                objName = getattr(obj, "name")
                objAuthor = getattr(obj, "author")

                if (objName == statusBook) and (objAuthor == statusAuthor):
                    obj.changeStatus(statusResponse)
                    
        """Response 4: Ends the while loop to exit the menu and program overall."""
        if response == "4":
            running = False



if __name__ == "__main__":
    main()


