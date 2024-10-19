#  REFERENCES
#https://www.geeksforgeeks.org/python-oops-concepts/
#https://k4y0x13.github.io/CSF101-Programming-Methodology/unit2/7.functions-scope.html
#https://www.datacamp.com/tutorial/python-oop-tutorial?utm_source=google&utm_medium=paid_search&utm_campaignid=19589720824&utm_adgroupid=157156376311&utm_device=c&utm_keyword=&utm_matchtype=&utm_network=g&utm_adpostion=&utm_creative=716160943561&utm_targetid=dsa-2218886984100&utm_loc_interest_ms=&utm_loc_physical_ms=9075448&utm_content=&utm_campaign=230119_1-sea~dsa~tofu_2-b2c_3-row-p2_4-prc_5-na_6-na_7-le_8-pdsh-go_9-nb-e_10-na_11-na-oct24&gad_source=1&gclid=CjwKCAjwjsi4BhB5EiwAFAL0YAG8pHxDA-ohBYKUxH7omAQfWFc2i8rH8NXhxKETHX00wo99YrbEvRoCjDEQAvD_BwE
#https://www.w3schools.com/python/python_for_loops.asp
#https://www.youtube.com/watch?v=o5uJrvQDrvU&list=PLcArXHK8v0la_bTQ-HpNo_eAfj4FVc5HD
#https://www.youtube.com/watch?v=Gz6u8JA1Vk8&list=PLjiKFad_N7K1n4r2EpyC-6N4IePgTjBW2



# To represent a book in the library with attributes like title, author, and availability status.
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True  # Indicates if the book is available for borrowing
        self.borrower = None  # Will track the user who borrowed the book

    def __str__(self):
        # To return a string representation of the book's status whether it is available or borrowed by someone.
        status = "Available" if self.available else f"Borrowed by {self.borrower}"
        return f"'{self.title}' by {self.author} - {status}"


# It will manage the collection of books and handles borrowing, returning, and displaying books.
class Library:
    def __init__(self):
        self.books = []  # List to store all books in the library

    def add_book(self, title, author):
        # To add a new book to the library's collection
        new_book = Book(title, author)
        self.books.append(new_book)
        print(f"Book '{title}' by {author} added to the library.")

    def display_books(self):
        # To display all books in the library along with their status
        if not self.books:
            print("The library has no books.")
        else:
            print("\nLibrary Books:")
            for i, book in enumerate(self.books, start=1):
                print(f"{i}. {book}")

    def borrow_book(self, title, borrower_name):
        # To allow the user to borrow a book if it is available
        for book in self.books:
            if book.title.lower() == title.lower() and book.available:
                book.available = False
                book.borrower = borrower_name
                print(f"'{book.title}' has been borrowed by {borrower_name}.")
                return True
        print(f"Sorry, the book '{title}' is either not available or already borrowed.")
        return False

    def return_book(self, title, borrower_name):
        # To allow the user to return a borrowed book
        for book in self.books:
            if book.title.lower() == title.lower() and not book.available and book.borrower == borrower_name:
                book.available = True
                book.borrower = None
                print(f"'{book.title}' has been returned by {borrower_name}.")
                return True
        print(f"The book '{title}' was not borrowed by {borrower_name} or does not exist in the library.")
        return False


# To represent the user in the library system with basic operations to borrow and return books.
class User:
    def __init__(self, name):
        self.name = name  # Stores the user's name

    def borrow_book(self, library, title):
        # To allow the user to borrow a book from the library
        library.borrow_book(title, self.name)

    def return_book(self, library, title):
        # To allow the user to return a book to the library
        library.return_book(title, self.name)


# It will represent an admin user with additional privilege to add books to the library.
class Admin(User):
    def __init__(self, name):
        super().__init__(name)  # Calls the constructor of the User class

    def add_book(self, library, title, author):
        # To allow the admin to add a new book to the library
        library.add_book(title, author)


# Main function to run the library application.
def main():
    library = Library()  # Create an instance of the Library
    users = {}  # Dictionary to store registered users and admins

    while True:
        # Will display the menu for the library system.
        print("\nLibrary System Menu:")
        print("1. Register as User")
        print("2. Register as Admin")
        print("3. View Books")
        print("4. Borrow a Book")
        print("5. Return a Book")
        print("6. Admin: Add a Book")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            # Register a new user
            name = input("Enter your name to register as a user: ")
            users[name] = User(name)
            print(f"User '{name}' has been registered.")

        elif choice == "2":
            # Register a new admin
            name = input("Enter your name to register as an admin: ")
            users[name] = Admin(name)
            print(f"Admin '{name}' has been registered.")

        elif choice == "3":
            # To display all books in the library
            library.display_books()

        elif choice == "4":
            # Borrow a book from the library
            name = input("Enter your name: ")
            if name in users:
                title = input("Enter the title of the book you want to borrow: ")
                users[name].borrow_book(library, title)
            else:
                print("Please register as a user before borrowing a book.")

        elif choice == "5":
            # Return a book to the library
            name = input("Enter your name: ")
            if name in users:
                title = input("Enter the title of the book you want to return: ")
                users[name].return_book(library, title)
            else:
                print("Please register as a user before returning a book.")

        elif choice == "6":
            # admin privilege to add a book in the library. (only admin can add a book in the library).
            name = input("Enter your name: ")
            if name in users and isinstance(users[name], Admin):
                title = input("Enter the title of the book to add: ")
                author = input("Enter the author of the book: ")
                users[name].add_book(library, title, author)
            else:
                print("You need to be an admin to add a book.")

        elif choice == "7":
            # To exit from the application
            print("Exiting the library system. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 7.")


# Entry point of the application
if __name__ == "__main__":
    main()
