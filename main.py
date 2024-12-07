"""Mini Project on OOPS LIBRARY SYSTEM usinG PYTHON
Authors :- Bikas Verma  """


class Library:
    #This is use as a cunstructor in claaa abject
    def __init__(self,list,name):
        self.bookList =list
        self.libraryname =name
        self.lendDict= {}
    def DisplayBooks(self):#it use for display book available in library
        print(f" we have following books :")
        for book in self.bookList:
            print(book)
    def LendBook(self,user,book):#we use this function to issue book from library
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print(f"Book has landed by {self.lendDict[book]} \n lender book updated")
        else:
            print(f"book is already being use by {self.lendDict[book]} \n choose any other option ")
    def AddBook(self,book):#it's for add any book in library
        self.bookList.append(book)
        print(f"book has been added in library")
        #self.booklist.update(book)
    
    def ReturnBook(self,book):#return the book
        if book in self.lendDict.keys():
            self.lendDict.pop(book)
            print(f"book has been returned")
        else:
            print("there is no book to Return")
if __name__=="__main__":
    LU = Library(['python','java','c++','c','Algorithm','Web Technology'],'OOPS' )
    while True:
        print(f"Welcome to the {LU.libraryname} library.")

        print(f"1.Display Books.")
        print(f"2.Lend a Book.")
        print(f"3.Add a Books.")
        print(f"4.Return a Books.")
        print(" Please Enter your choice:-")
        user_choice =input()
        if user_choice not in ['1','2','3','4']:
            continue
        else:
            user_choice= int(user_choice)
        
        if user_choice == 1:
            LU.DisplayBooks()
        elif user_choice ==2:
            user = input("Enter your Name:-")
            book = input("Enter the Book Name:-")
            LU.LendBook(user,book)
        elif user_choice== 3:
            book = input("Enter the Book Name to add:-")
            LU.AddBook(book)
        elif user_choice ==4:
            book =input("Enter the the Book to Return:-")
            LU.ReturnBook(book)
        else:
            print(f"not a valid option")
        
        print(f"press 'C' to Continue and 'Q' for Quit ")
        user_choice2 =" "
        while(user_choice2!= "C" and user_choice2!= "Q"):

            user_choice2 = input()
            if user_choice2 == "Q":
                exit()
            elif user_choice2 == "C":
                continue
