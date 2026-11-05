# library.py
# A simple command-line library tracker.

books = {}  # title -> {"author": str, "available": bool}
def list_books():
    if not books:
        print("No books in the library.")
        return

    for title, details in books.items():
        status = "Available" if details["available"] else "Borrowed"
        print(f"{title} by {details['author']} - {status}")

def show_menu():
    print("\n=== Library Tracker ===")
    print("1. Add book")
    print("2. List books")
    print("3. Borrow book")
    print("4. Return book")
    print("0. Exit")

def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()