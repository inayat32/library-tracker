
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


def show_menu():
    print("\n=== Library Tracker ===")
    print("1. Add Book")
    print("0. Exit")


def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_book()

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
