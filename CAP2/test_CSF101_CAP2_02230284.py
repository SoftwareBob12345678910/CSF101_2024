#REFERENCES:
#https://www.youtube.com/watch?v=JJ9zZ8cyaEk
#https://www.youtube.com/watch?v=v1MtwCPTmBI
#https://www.youtube.com/watch?v=96mDQrlceEk
#https://www.youtube.com/watch?v=mzlH8lp4ISA


import unittest
# The library code is saved in a file called `library_management_system.py`
# Importing Library, User, Admin from Library_management_system
from CSF101_CAP2_02230284 import Library, User, Admin

class TestLibraryManagementSystem(unittest.TestCase):
    
    def setUp(self):
        #Setting up a library instance with some initial data for each test case.
        #Creating a User and an Admin for testing purposes and adding initial books to the library.
        
        self.library = Library()
        self.user = User("Bob")
        self.admin = Admin("AdminUser")
        
        # Adding two initial books to the library
        self.library.add_book("Love Yourself", "K.Karma")
        self.library.add_book("Dawa Koto", "Dorji")
    
    def test_valid_borrow_book(self):
        #Testing a valid book borrowing scenario where a user borrows an available book.
        #Checking if the availability status changes and the borrower is set correctly.
        
        result = self.library.borrow_book("Love Yourself", self.user.name)
        self.assertTrue(result)  # Expecting borrow to succeed
        self.assertFalse(self.library.books[0].available)  # Book should now be unavailable
        self.assertEqual(self.library.books[0].borrower, "Bob")  # Borrower should be "Bob"

    def test_invalid_borrow_book_already_borrowed(self):
        #Testing an invalid scenario where a user tries to borrow a book that is already borrowed.
        #Checking if the system prevents double-borrowing and keeps the original borrower.
        
        # First, borrow the book
        self.library.borrow_book("Love Yourself", self.user.name)
        # Try borrowing it again while it is already borrowed by "Alice"
        result = self.library.borrow_book("Love Yourself", "AnotherUser")
        self.assertFalse(result)  # Expecting the borrow attempt to fail
        self.assertEqual(self.library.books[0].borrower, "Bob")  # Borrower should still be "Bob"

    def test_valid_return_book(self):
        #Testing a valid book returning scenario where a user returns a book they borrowed.
        #Checking if the availability status resets and the borrower is cleared.
        
        # First, borrow the book to set it as unavailable
        self.library.borrow_book("Dawa Koto", self.user.name)
        # Now, return the book
        result = self.library.return_book("Dawa Koto", self.user.name)
        self.assertTrue(result)  # Expecting return to succeed
        self.assertTrue(self.library.books[1].available)  # Book should now be available
        self.assertIsNone(self.library.books[1].borrower)  # Borrower should be cleared

    def test_invalid_return_book_not_borrowed(self):
        #Testing an invalid scenario where a user tries to return a book that hasn't been borrowed.
        #Confirming that the system does not allow this action.
        
        result = self.library.return_book("Dawa Koto", self.user.name)
        self.assertFalse(result)  # Expecting return attempt to fail
        self.assertTrue(self.library.books[1].available)  # Book should still be available
        self.assertIsNone(self.library.books[1].borrower)  # Borrower should still be None

    def test_admin_add_book(self):
        #Testing if an admin can successfully add a book to the library.
        #Verifying that the new book appears in the collection with the correct details.
        
        # Admin adds a new book to the library
        self.admin.add_book(self.library, "Empty Chair", "Lhamo")
        
        # Checking if the book was added at the end of the book list
        added_book = self.library.books[-1]
        self.assertEqual(added_book.title, "Empty Chair")
        self.assertEqual(added_book.author, "Lhamo")
        self.assertTrue(added_book.available)  # Book should be available
        self.assertIsNone(added_book.borrower)  # No borrower should be assigned

    def test_borrow_all_books_and_check_availability(self):
        #Testing the scenario where a user borrows all books in the library.
        #Ensuring that all books are marked as unavailable after being borrowed.
        
        # Borrow each book in the library
        for book in self.library.books:
            self.library.borrow_book(book.title, self.user.name)
        
        # To verify that each book is now unavailable and has "Bob" as the borrower
        for book in self.library.books:
            self.assertFalse(book.available)  # Book should be unavailable
            self.assertEqual(book.borrower, self.user.name)  # Borrower should be "Bob"

    def test_return_all_books_and_check_availability(self):
        #Testing the scenario where a user returns all books in the library.
        #Ensuring that all books are available after being returned.
        
        # First, borrow each book to make them unavailable
        for book in self.library.books:
            self.library.borrow_book(book.title, self.user.name)
        
        # Now return each book
        for book in self.library.books:
            self.library.return_book(book.title, self.user.name)
        
        # To verify that each book is now available and has no borrower
        for book in self.library.books:
            self.assertTrue(book.available)  # Book should be available
            self.assertIsNone(book.borrower)  # No borrower should be assigned

    def test_invalid_borrow_nonexistent_book(self):
        #Testing an invalid borrowing attempt for a book that does not exist in the library.
        #Confirming that the system prevents this action.
        
        result = self.library.borrow_book("Nonexistent Book", self.user.name)
        self.assertFalse(result)  # Expecting borrow attempt to fail

    def test_invalid_return_nonexistent_book(self):
        #Testing an invalid return attempt for a book that does not exist in the library.
        #Confirming that the system prevents this action.
        
        result = self.library.return_book("Nonexistent Book", self.user.name)
        self.assertFalse(result)  # Expecting return attempt to fail

if __name__ == "__main__":
    unittest.main()
