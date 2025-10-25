import sqlite3

conn = sqlite3.connect('expenses.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    catergory TEXT,
    amount REAL,
    description TEXT
)
""")
print("Database and table created successfully.")

conn.commit()
conn.close()


def add_expense(date, category, amount, description):
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO expenses (date, catergory, amount, description)
    VALUES (?, ?, ?, ?)
    """, (date, category, amount, description))
    conn.commit()
    conn.close()
    print("Expense added successfully.")


print("Adding an expense...")
date = input("Enter date (YYYY-MM-DD): ")
catergory = input("Enter category: ")
amount = float(input("Enter amount: "))
description = input("Enter description: ")

add_expense(date, catergory, amount, description)


def view_expenses():
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()
    conn.close()

    print("\n All Expenses:")
    print("-" * 50)
    for rows in rows:
        print(
            f"ID: {rows[0]}, Date: {rows[1]}, Category: {rows[2]}, Amount: {rows[3]}, Description: {rows[4]}")
    print("-" * 50)

    conn.close()


def summary_by_category():
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    cursor.execute("""
    SELECT catergory, SUM(amount)
    FROM expenses
    GROUP BY catergory
    """)
    rows = cursor.fetchall()

    print("\n Total Expenses by Category:")
    print("-" * 50)
    for rows in rows:
        print(f"{rows[0]}: Rs. {rows[1]}")
    print("-" * 50)

    conn.close()


while True:
    print("\n📊 Expense Tracker Menu")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Summary by Category")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        date = input("Enter date (YYYY-MM-DD): ")
        category = input("Enter category: ")
        amount = float(input("Enter amount: "))
        description = input("Enter description: ")
        add_expense(date, category, amount, description)

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        summary_by_category()

    elif choice == "4":
        print("👋 Exiting... Goodbye!")
        break

    else:
        print("❌ Invalid choice. Please try again.")
