import json
import os
from datetime import datetime

# File to store expense data
EXPENSE_FILE = "expenses.json"

# Load existing expenses or initialize an empty list
def load_expenses():
    if os.path.exists(EXPENSE_FILE):
        with open(EXPENSE_FILE, "r") as file:
            return json.load(file)
    return []

# Save expenses to the file
def save_expenses(expenses):
    with open(EXPENSE_FILE, "w") as file:
        json.dump(expenses, file, indent=4)

# Add a new expense
def add_expense(expenses):
    try:
        amount = float(input("Enter the amount spent: "))
        description = input("Enter a brief description: ")
        category = input("Enter the category (e.g., food, transportation, entertainment): ")

        expense = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "amount": amount,
            "description": description,
            "category": category
        }

        expenses.append(expense)
        save_expenses(expenses)
        print("Expense added successfully!")
    except ValueError:
        print("Invalid input. Please enter a valid amount.")

# View all expenses
def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded yet.")
    else:
        for expense in expenses:
            print(f"Date: {expense['date']}, Amount: ${expense['amount']:.2f}, "
                  f"Category: {expense['category']}, Description: {expense['description']}")

# View monthly summary
def monthly_summary(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return

    monthly_expenses = {}
    for expense in expenses:
        month = expense["date"][:7]  # Extract year and month (e.g., "2023-10")
        if month not in monthly_expenses:
            monthly_expenses[month] = 0
        monthly_expenses[month] += expense["amount"]

    print("\nMonthly Summary:")
    for month, total in monthly_expenses.items():
        print(f"{month}: ${total:.2f}")

# View category-wise expenditure
def category_summary(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return

    category_expenses = {}
    for expense in expenses:
        category = expense["category"]
        if category not in category_expenses:
            category_expenses[category] = 0
        category_expenses[category] += expense["amount"]

    print("\nCategory-wise Expenditure:")
    for category, total in category_expenses.items():
        print(f"{category}: ${total:.2f}")

# Main function to run the Expense Tracker
def main():
    expenses = load_expenses()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Monthly Summary")
        print("4. View Category-wise Expenditure")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            monthly_summary(expenses)
        elif choice == "4":
            category_summary(expenses)
        elif choice == "5":
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()