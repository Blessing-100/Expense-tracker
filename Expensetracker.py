expenses = []

def add_expense():
    description = input("Enter expense description: ")
    amount = float(input("Enter amount: "))
    date = input("Enter date (DD-MM-YYYY): ")

    expense = {
        "description": description,
        "amount": amount,
        "date": date
    }

    expenses.append(expense)
    print("Expense added successfully.\n")


def view_expenses():
    if not expenses:
        print("No expenses recorded.\n")
        return

    print("\n--- Expense List ---")
    for index, expense in enumerate(expenses, start=1):
        print(
            index,
            expense["description"],
            expense["amount"],
            expense["date"]
        )
    print()


def calculate_total():
    total = 0
    for expense in expenses:
        total += expense["amount"]

    print("Total expenses:", total, "\n")


def main_menu():
    while True:
        print("Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Total Expenses")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            calculate_total()
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.\n")
       
main_menu()
