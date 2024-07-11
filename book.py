import sqlite3

db = sqlite3.connect('ebookstore')
cursor = db.cursor()

# Create the table "book"
cursor.execute('''
    CREATE TABLE IF NOT EXISTS book (
        id INTEGER PRIMARY KEY,
        title TEXT,
        author TEXT,
        qty INTEGER
    )
''')

db.commit()

# Define bookstore data
bookstore_data = [
    (3001, 'A Tale of Two Cities', 'Charles Dickens', 90),
    (3002, 'Harry Potter and the Philosopher\'s Stone', 'J.K Rowling', 40),
    (3003, 'The Lion, the Witch and the Wardrobe', 'C.S. Lewis', 25),
    (3004, 'The Lord of the Rings', 'J.R.R Tolkien', 37),
    (3005, 'Alice in Wonderland', 'Lewis Carroll', 12)
]

# Insert bookstore data
cursor.executemany('''
    INSERT OR REPLACE INTO book (id, title, author, qty) VALUES (?, ?, ?, ?)
''', bookstore_data)

while True:
    print('\nMain Menu:')
    print('1. Enter book')
    print('2. Update book quantity')
    print('3. Delete book')
    print('4. Search books')
    print('0. Exit')

    choice = input('Enter your choice: ')

    if choice == '1':
        # Enter book
        id = int(input('Enter a book ID: '))
        title = input('Enter book title: ')
        author = input('Enter book author: ')
        qty = int(input('Enter book quantity: '))

        cursor.execute('''
            INSERT INTO book (id, title, author, qty) VALUES (?, ?, ?, ?)
        ''', (id, title, author, qty))
        print(f'Book "{title}" added successfully.')

    elif choice == '2':
        # Update book quantity
        author = input('Enter the author of the book to update quantity: ')
        new_qty = int(input('Enter the new quantity: '))

        cursor.execute('''
            UPDATE book SET qty = ? WHERE author = ?
        ''', (new_qty, author))
        print(f'Quantity for books by {author} updated to {new_qty}.')

    elif choice == '3':
        # Delete book
        id_to_delete = int(input('Enter ID of book to delete: '))

        cursor.execute('''
            DELETE FROM book WHERE id = ?
        ''', (id_to_delete,))
        print(f'Book with ID {id_to_delete} deleted successfully.')

    elif choice == '4':
        # Search books
        author = input('Enter author to search for: ')

        cursor.execute('''
            SELECT * FROM book WHERE author = ?
        ''', (author,))

        books = cursor.fetchall()

        if books:
            for book in books:
                print(book)
        else:
            print(f'No books found for author: {author}')

    elif choice == '0':
        # Exit
        break

    else:
        print('Invalid choice. Please try again.')

db.commit()
db.close()
