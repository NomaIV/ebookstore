# ebookstore

Capstone Project: Database program for a bookstore.

Program allows a bookstore clerk to enter new books, update book information, delete books, and search the availability of books in the database.

## Technologies Used:
- SQL
- SQLite
- Python
- VSCode

## Repository
[Link to repository](https://github.com/NomaIV/ebookstore)

## Features
- Add new books to the database
- Update book information
- Delete books from the database
- Search the database to find a specific book

## Prerequisites

Before you begin, ensure you have the following installed:
- Visual Studio Code (VSCode)
- SQLite
- Python

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/NomaIV/ebookstore.git
    ```
2. Navigate to the project directory:
    ```sh
    cd ebookstore
    ```
3. Create and activate a virtual environment (optional):
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```


## Usage
1. **Setup the Database:**
   - Ensure SQLite is installed and available in your PATH.
   - The database will be created and populated with initial data when you run the main script.

2. **Running the Program:**
   - To start the program, run the main script:
     ```sh
     python3 book.py
     ```
   - Follow the on-screen prompts to add, update, delete, or search for books in the database.

3. **Using the Program:**
   - **Add New Books:**
     - Select option 1.
     - Enter the required information: book ID, title, author, and quantity.
   - **Update Book Quantity:**
     - Select option 2.
     - Enter the author of the book to update and the new quantity.
   - **Delete Books:**
     - Select option 3.
     - Enter the ID of the book to delete.
   - **Search for Books:**
     - Select option 4.
     - Enter the author to search for books by that author.

4. **Exiting the Program:**
   - Select option 0 to exit the program.

## Project Structure
- `book.py`: The main script to run the program.
- `README.md`: Project documentation.


