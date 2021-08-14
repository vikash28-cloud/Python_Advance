class Library:

    def __init__(self, listOfBooks):
        self.books = listOfBooks

    def displayAvailableBooks(self):
        print("Books present in this library are: ")
        for book in self.books:
            #print("\t")
            print(" *\t"+book)
    
    def borrowBook(self,requestedbook):
        if requestedbook in self.books:
            print(f"you have been issued {requestedbook}. please keep it safe")
            self.books.remove(requestedbook)
            return True

        else:
            print("book is not available")
            return False
        
    def returnBook(self,returnedbook):
        self.books.append(returnedbook)

        print("thanks for returning this book")

class Student:
    
    def requestBook(self):
        self.book = input("enter the book name you want to borrow: ")
        return self.book

    def returnBook(self):
        self.book = input("enter the name of the book you want to return: ")
        return self.book
     

if __name__ == "__main__":
    centralLibrary = Library(["Algorithms", "DataScience", "MachineLearning", "A.I", "Python"])
    student = Student()

    while(True):
        welcomeMsg = '''***********welcome to centralLibrary*****************
        please choose an option:
            1. Show all books
            2. Request a book
            3. Return a book
            4. Exit the library
        '''
        print(welcomeMsg)
        a = int(input("enter a choice: "))
        if a ==1:
            centralLibrary.displayAvailableBooks()
        elif a == 2:
            centralLibrary.borrowBook(student.requestBook())
        elif a == 3:
            centralLibrary.returnBook(student.returnBook())
        elif a == 4:
            print("thanks for choosing central library")
            exit()
        else:
            print("invalid choice")

        
        

    

