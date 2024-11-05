# TEST_README.md

## Overview

This document describes the test cases developed for the Library Management System, focusing on verifying key functionalities, handling edge cases, and ensuring the reliability of operations within the system. The test suite is implemented using Python's built-in `unittest` module, which allows for structured and modular testing of each core feature of the system.

## Test Suite Description

The test suite covers the following functionalities of the Library Management System:

1. **Book Borrowing**: Valid and invalid scenarios for borrowing books.
2. **Book Returning**: Valid and invalid scenarios for returning books.
3. **Admin Operations**: Testing the admin-specific functionality of adding books to the library.
4. **Boundary and Edge Cases**: Handling special cases, such as borrowing or returning all books, and handling non-existent books.

Each test is written in a modular fashion, targeting specific functionality and designed to check for both expected success and failure scenarios.

## Resources Used

1. **Python’s `unittest` Module**: The `unittest` framework, a part of Python’s standard library, is used for structuring and organizing the tests. It provides a range of assertion methods to verify that each function behaves as expected, making it ideal for validating core functionality and edge cases.
   - **Justification**: `unittest` is widely used for unit testing in Python, offering a robust and flexible testing environment that requires no additional setup or third-party installations. Its structured approach allows for clear test reporting, setup, and teardown capabilities, which facilitate testing complex systems like the Library Management System.

2. **Mocking of User Interactions**: Although limited user interaction is required, we simulate user names directly within the tests to verify borrowing and returning actions without requiring interactive input during test execution.
   - **Justification**: Directly providing user names in test cases allows for predictable and repeatable results, ensuring that each test runs without manual input and produces consistent results for verification.

3. **Boundary and Edge Case Analysis**: Special attention was given to boundary cases, such as:
   - **Borrowing All Books**: Ensures that the system handles cases where all books are borrowed, confirming correct status updates and borrower tracking.
   - **Returning All Books**: Tests if the system resets availability correctly when all books are returned.
   - **Nonexistent Books**: Attempts to borrow or return books that do not exist, checking for proper handling of invalid inputs.
   - **Justification**: Edge cases ensure that the system behaves as expected even in uncommon or extreme situations, improving robustness and user experience.

## Test Coverage

The following scenarios are covered by individual test cases within the test suite:

1. **Valid Book Borrowing** (`test_valid_borrow_book`): Verifies that a user can borrow an available book and that its availability status changes.

2. **Invalid Book Borrowing** (`test_invalid_borrow_book_already_borrowed`): Tests attempting to borrow a book that is already borrowed by another user.

3. **Valid Book Returning** (`test_valid_return_book`): Confirms that a user can return a book they borrowed, restoring the book's availability.

4. **Invalid Book Returning** (`test_invalid_return_book_not_borrowed`): Checks the system’s response when a user attempts to return a book that was not borrowed.

5. **Admin Adding Books** (`test_admin_add_book`): Verifies that only an admin can add books and ensures that the new book appears in the library’s collection.

6. **Boundary Case: Borrow All Books** (`test_borrow_all_books_and_check_availability`): Tests that the system correctly handles borrowing all books in the library, marking each book as unavailable.

7. **Boundary Case: Return All Books** (`test_return_all_books_and_check_availability`): Ensures that the system updates each book’s status when all books are returned.

8. **Invalid Borrow of Nonexistent Book** (`test_invalid_borrow_nonexistent_book`): Verifies the system’s behavior when a user tries to borrow a book that doesn’t exist.

9. **Invalid Return of Nonexistent Book** (`test_invalid_return_nonexistent_book`): Ensures that the system responds correctly when attempting to return a nonexistent book.

## Running the Tests

To run the tests, use the following command:

```bash
python -m unittest test_library_management_system.py
