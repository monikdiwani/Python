# Create a list by taking 5 inputs from the user
my_list = []
print("Enter 5 elements for the list:")
for i in range(5):
    element = input(f"Enter element {i + 1}: ")
    my_list.append(element)

print("\nYour List:", my_list)

# Perform operations: Insert or Delete
while True:
    print("\nChoose an option:")
    print("1. Insert a new element")
    print("2. Delete an element")
    print("3. Exit")
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        # Insert operation
        new_element = input("Enter the element to insert: ")
        my_list.append(new_element)
        print("Updated List:", my_list)
    elif choice == "2":
        # Delete operation
        del_element = input("Enter the element to delete: ")
        if del_element in my_list:
            my_list.remove(del_element)
            print("Updated List:", my_list)
        else:
            print("Element not found!")
    elif choice == "3":
        # Exit the loop
        print("Final List:", my_list)
        break
    else:
        print("Invalid choice! Please try again.")
