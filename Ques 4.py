def display_menu():
    print("Menu:")
    print("1. Insert Element")
    print("2. Delete Element")
    print("3. Display List")
    print("4. Exit")

def delete_submenu():
    print("Delete Options:")
    print("1. Delete by Value")
    print("2. Delete by Position")
    print("3. Delete by Slice")
    print("4. Back to Main Menu")

# Initialize an empty list
my_list = []

while True:
    display_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        # Insert Element
        element = input("Enter the element to insert: ")
        my_list.append(element)
        print(f"{element} has been inserted into the list.")

    elif choice == "2":
        # Delete Element
        delete_submenu()
        delete_choice = input("Enter your delete choice: ")

        if delete_choice == "1":
            # Delete by Value
            value_to_delete = input("Enter the value to delete: ")
            if value_to_delete in my_list:
                my_list.remove(value_to_delete)
                print(f"{value_to_delete} has been deleted from the list.")
            else:
                print(f"{value_to_delete} not found in the list.")

        elif delete_choice == "2":
            # Delete by Position
            position_to_delete = int(input("Enter the position to delete: "))
            if 1 <= position_to_delete <= len(my_list):
                deleted_element = my_list.pop(position_to_delete - 1)
                print(f"Element at position {position_to_delete} ({deleted_element}) has been deleted.")
            else:
                print("Invalid position.")

        elif delete_choice == "3":
            # Delete by Slice
            start = int(input("Enter the start index of the slice: "))
            end = int(input("Enter the end index of the slice: "))
            if 1 <= start <= end <= len(my_list):
                deleted_slice = my_list[start - 1:end]
                del my_list[start - 1:end]
                print(f"Slice {deleted_slice} has been deleted.")
            else:
                print("Invalid slice indices.")

    elif choice == "3":
        # Display List
        print("Current List:", my_list)

    elif choice == "4":
        # Exit
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please try again.")