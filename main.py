import sqlite3

# Connect to database
conn = sqlite3.connect("expenses.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category TEXT,
    amount REAL,
    description TEXT
)
""")

def add_expense():
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")

    cursor.execute("INSERT INTO expenses (category, amount, description) VALUES (?, ?, ?)",
                   (category, amount, description))
    conn.commit()
    print("Expense added successfully!\n")

def view_expenses():
    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()

    for row in rows:
        print(row)
    print()

def total_expense():
    cursor.execute("SELECT SUM(amount) FROM expenses")
    total = cursor.fetchone()[0]
    print(f"Total Expense: {total}\n")

def menu():
    while True:
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expense")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expense()
        elif choice == "4":
            break
        else:
            print("Invalid choice\n")

menu()
conn.close()
