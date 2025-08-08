def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            add = input("Enter the item to add: ").lower()
            pass
        elif choice == '2':
            # Prompt for and remove an item
            remove = input("choose an item to remove from the list: ").lower()
            if remove in shopping_list:
                shopping_list.remove(remove)
            else:
                print("your input is invalid")
        elif choice == '3':
            # Display the shopping list
            print(shopping_list)
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

