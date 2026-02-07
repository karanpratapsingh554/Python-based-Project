import read
import operation

def main_menu():
    """ Display the main menu and handle user choices. """
    while True:
        print("\n" + "*" * 40)
        print("Furniture Management System")
        print("*" * 40)
        print("1. Show Furniture")
        print("2. Sell Furniture")
        print("3. Exit")
        print("*" * 40)
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            # Show furniture
            dic = read.getFileContent()
            operation.show_furniture(dic)
        elif choice == '2':
            # Sell furniture
            operation.sell_furniture()
        elif choice == '3':
            # Exit the application
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

# Entry point of the application
if __name__ == "__main__":
    main_menu()
