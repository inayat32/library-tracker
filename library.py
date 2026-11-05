
# A simple command-line library tracker.

books = {}  # title -> {"author": str, "available": bool}


def add_book():
    title = input("Enter book title: ").strip()
    author = input("Enter author name: ").strip()

    if not title or not author:
        print("Title and author cannot be empty.")
        return

    if title in books:
        print("This book already exists.")
        return

    books[title] = {
        "author": author,
        "available": True
    }

    print(f"Book '{title}' added successfully!")


def list_books():
    if not books:
        print("No books in the library.")
        return

    for title, details in books.items():
        status = "Available" if details["available"] else "Borrowed"
        print(f"{title} by {details['author']} - {status}")


# Borrow Book Feature
def borrow_book():
    title = input("Enter book title to borrow: ").strip()

    if title not in books:
        print("Book not found.")

    elif not books[title]["available"]:
        print("Book is already borrowed.")

    else:
        books[title]["available"] = False
        print("Book borrowed successfully.")


def return_book():
    title = input("Enter book title to return: ").strip()

    if title not in books:
        print("Book not found.")

    elif books[title]["available"]:
        print("Book is already available.")

    else:
        books[title]["available"] = True
        print("Book returned successfully.")


def show_menu():
    print("\n=== Library Tracker ===")
    print("1. Add Book")
    print("2. List Books")
    print("3. Borrow Book")
    print("4. Return Book")
    print("0. Exit")


def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_book()

        elif choice == "2":
            list_books()

        elif choice == "3":
            borrow_book()

        elif choice == "4":
            return_book()

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
