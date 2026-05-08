import json
import os


class Item:
    def __init__(self, item_id, item_name, category, location_found, status="Unclaimed"):
        self.item_id = item_id
        self.item_name = item_name
        self.category = category
        self.location_found = location_found
        self.status = status

    def to_dict(self):
        return {
            "item_id": self.item_id,
            "item_name": self.item_name,
            "category": self.category,
            "location_found": self.location_found,
            "status": self.status
        }


class LostAndFoundSystem:
    FILE_NAME = "items.json"

    def __init__(self):
        self.items = []
        self.load_data()

    def load_data(self):
        if os.path.exists(self.FILE_NAME):
            try:
                with open(self.FILE_NAME, "r") as file:
                    data = json.load(file)
                    self.items = [Item(**item) for item in data]
            except json.JSONDecodeError:
                print("Error reading JSON file.")
                self.items = []
        else:
            self.items = []

    def save_data(self):
        with open(self.FILE_NAME, "w") as file:
            json.dump([item.to_dict() for item in self.items], file, indent=4)

    def add_item(self):
        item_id = input("Enter Item ID: ")

        for item in self.items:
            if item.item_id == item_id:
                print("Item ID already exists.")
                return

        item_name = input("Enter Item Name: ")
        category = input("Enter Category: ")
        location_found = input("Enter Location Found: ")

        new_item = Item(item_id, item_name, category, location_found)
        self.items.append(new_item)
        self.save_data()

        print("Item added successfully.")

    def view_items(self):
        if not self.items:
            print("No items found.")
            return

        print("\n--- Lost & Found Items ---")
        for item in self.items:
            print(f"""
ID: {item.item_id}
Name: {item.item_name}
Category: {item.category}
Location: {item.location_found}
Status: {item.status}
--------------------------
""")

    def search_item(self):
        keyword = input("Enter item name or category: ").lower()

        found = False

        for item in self.items:
            if (keyword in item.item_name.lower() or
                    keyword in item.category.lower()):
                print(f"""
ID: {item.item_id}
Name: {item.item_name}
Category: {item.category}
Location: {item.location_found}
Status: {item.status}
--------------------------
""")
                found = True

        if not found:
            print("No matching items found.")

    def search_by_location(self):
        location = input("Enter location: ").lower()

        found = False

        for item in self.items:
            if location in item.location_found.lower():
                print(f"""
ID: {item.item_id}
Name: {item.item_name}
Category: {item.category}
Location: {item.location_found}
Status: {item.status}
--------------------------
""")
                found = True

        if not found:
            print("No items found at this location.")

    def mark_claimed(self):
        item_id = input("Enter Item ID to mark as claimed: ")

        for item in self.items:
            if item.item_id == item_id:
                item.status = "Claimed"
                self.save_data()
                print("Item marked as claimed.")
                return

        print("Item not found.")

    def delete_item(self):
        item_id = input("Enter Item ID to delete: ")

        for item in self.items:
            if item.item_id == item_id:
                self.items.remove(item)
                self.save_data()
                print("Item deleted successfully.")
                return

        print("Item not found.")

    def sort_by_category(self):
        sorted_items = sorted(self.items, key=lambda x: x.category.lower())

        print("\n--- Sorted Items by Category ---")
        for item in sorted_items:
            print(f"{item.category} - {item.item_name}")

    def count_items(self):
        claimed = 0
        unclaimed = 0

        for item in self.items:
            if item.status == "Claimed":
                claimed += 1
            else:
                unclaimed += 1

        print(f"Claimed Items: {claimed}")
        print(f"Unclaimed Items: {unclaimed}")

    # Main menu
    def menu(self):
        while True:
            print("""
====== Lost & Found System ======
1. Add Lost Item
2. View All Items
3. Search Item
4. Mark Item as Claimed
5. Delete Item
6. Sort Items by Category
7. Count Claimed/Unclaimed Items
8. Search Items by Location
9. Exit
""")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_item()

            elif choice == "2":
                self.view_items()

            elif choice == "3":
                self.search_item()

            elif choice == "4":
                self.mark_claimed()

            elif choice == "5":
                self.delete_item()

            elif choice == "6":
                self.sort_by_category()

            elif choice == "7":
                self.count_items()

            elif choice == "8":
                self.search_by_location()

            elif choice == "9":
                print("Exiting program...")
                break

            else:
                print("Invalid choice. Please try again.")


system = LostAndFoundSystem()
system.menu()
