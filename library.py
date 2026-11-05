def borrow_book():
    title = input("Enter book title to borrow: ")

    if title not in books:
        print("Book not found.")
    elif not books[title]["available"]:
        print("Book is already borrowed.")
    else:
        books[title]["available"] = False
        print("Book borrowed successfully.")


def return_book():
    title = input("Enter book title to return: ")

    if title not in books:
        print("Book not found.")
    elif books[title]["available"]:
        print("Book is already available.")
    else:
        books[title]["available"] = True
        print("Book returned successfully.")
