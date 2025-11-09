class Item:
    def __init__(self, title, author, item_id):
        self.title = title
        self.author = author
        self.item_id = item_id
        self.status = "available"

    def check_out(self):
        if self.status == "available":
            self.status = "checked out"
            return True
        return False

    def check_in(self):
        if self.status == "checked out":
            self.status = "available"
            return True
        return False

    def summary(self):
        return f"ID: {self.item_id} | Title: {self.title} | Author: {self.author} | Status: {self.status}"

    def __str__(self):
        return self.summary()


class Book(Item):
    def __init__(self, title, author, item_id, pages):
        super().__init__(title, author, item_id)
        self.pages = pages

    def summary(self):
        base = super().summary()
        return f"{base} | Pages: {self.pages}"


class DVD(Item):
    def __init__(self, title, director, item_id, runtime):
        super().__init__(title, director, item_id)
        self.runtime = runtime

    def summary(self):
        base = super().summary()
        return f"{base} | Runtime: {self.runtime} mins"


class LibraryCatalog:
    def __init__(self):
        self.items = {}

    def add_item(self, item):
        if item.item_id in self.items:
            print("Error: Item ID already exists.")
            return False
        self.items[item.item_id] = item
        print(f"Added '{item.title}' to catalog.")
        return True

    def checkout_item(self, item_id):
        item = self.items.get(item_id)
        if not item:
            print("Item not found.")
            return False
        if item.check_out():
            print(f"'{item.title}' checked out successfully.")
            return True
        print("Item is already checked out.")
        return False

    def checkin_item(self, item_id):
        item = self.items.get(item_id)
        if not item:
            print("Item not found.")
            return False
        if item.check_in():
            print(f"'{item.title}' checked in successfully.")
            return True
        print("Item is already available.")
        return False

    def list_items(self):
        if not self.items:
            print("No items in the catalog.")
        else:
            for item in self.items.values():
                print(item.summary())

def run_library_app():
    catalog = LibraryCatalog()

    while True:
        print("Library Menu:")
        print("1. Add Book")
        print("2. Add DVD")
        print("3. Check Out Item")
        print("4. Check In Item")
        print("5. List All Items")
        print("6. Exit")

        choice = input("Select an option (1-6): ").strip()

        if choice == "1":
            item_id = input("Enter Book ID: ").strip()
            title = input("Enter Book Title: ").strip()
            author = input("Enter Book Author: ").strip()
            pages_input = input("Enter number of pages: ").strip()
            try:
                pages = int(pages_input)
            except ValueError:
                pages = pages_input  
            book = Book(title, author, item_id, pages)
            catalog.add_item(book)

        elif choice == "2":
            item_id = input("Enter DVD ID: ").strip()
            title = input("Enter DVD Title: ").strip()
            director = input("Enter DVD Director: ").strip()
            runtime_input = input("Enter runtime in minutes: ").strip()
            try:
                runtime = int(runtime_input)
            except ValueError:
                runtime = runtime_input
            dvd = DVD(title, director, item_id, runtime)
            catalog.add_item(dvd)

        elif choice == "3":
            item_id = input("Enter the ID of the item to check out: ").strip()
            catalog.checkout_item(item_id)

        elif choice == "4":
            item_id = input("Enter the ID of the item to check in: ").strip()
            catalog.checkin_item(item_id)

        elif choice == "5":
            catalog.list_items()

        elif choice == "6":
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    run_library_app()
        

