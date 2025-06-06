def display_menu():
    """Displays the main menu options to the user."""
    print("Shopping List Manager") # This was the missing line!
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    """
    Manages the shopping list, allowing users to add, remove, and view items.
    """
    shopping_list = [] # Initialize an empty list to store shopping items

    while True:
        display_menu() # Show the menu to the user
        choice = input("Enter your choice: ").strip() # Get user's choice and remove whitespace

        if choice == '1':
            # Add Item functionality
            item_to_add = input("Enter the item to add: ").strip()
            if item_to_add: # Ensure the input is not empty
                shopping_list.append(item_to_add)
                print(f"'{item_to_add}' has been added to your shopping list.")
            else:
                print("Item name cannot be empty. Please try again.")

        elif choice == '2':
            # Remove Item functionality
            if not shopping_list: # Check if the list is empty first
                print("Your shopping list is empty. Nothing to remove.")
                continue # Go back to the menu
            
            item_to_remove = input("Enter the item to remove: ").strip()
            if item_to_remove: # Ensure the input is not empty
                if item_to_remove in shopping_list:
                    shopping_list.remove(item_to_remove)
                    print(f"'{item_to_remove}' has been removed from your shopping list.")
                else:
                    print(f"'{item_to_remove}' was not found in your shopping list.")
            else:
                print("Item name cannot be empty. Please try again.")

        elif choice == '3':
            # View List functionality
            if shopping_list:
                print("\n--- Current Shopping List ---")
                for i, item in enumerate(shopping_list, 1): # Enumerate to get numbered list
                    print(f"{i}. {item}")
                print("-----------------------------")
            else:
                print("\nYour shopping list is empty.")

        elif choice == '4':
            # Exit functionality
            print("Goodbye! Your shopping list is saved for next time.") # A friendly exit message
            break # Exit the while loop, ending the program

        else:
            # Handle invalid choices
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()