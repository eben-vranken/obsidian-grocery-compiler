groceries = []

def main():
    print_menu()
    user_input = input("Enter your choice: ")
    while user_input != "0":
	options = {
"1": view_groceries,
"2": add_groceries
	}
        options.get(user_input,default)()
            

def print_menu():
    print("1. View groceries")
    print("2. Add groceries")
    print("3. Confirm groceries")
    print("0. Quit")

def view_groceries():
    print(groceries)

def add_groceries():
    print("Add groceries")

if __name__ == "__main__":
    main()
