def main():
    print_menu()
    user_input = input("Enter your choice: ")
    print(user_input)

def print_menu():
    print("1. View groceries")
    print("2. Add groceries")
    print("3. Confirm groceries")
    print("0. Exit")

if __name__ == "__main__":
    main()
