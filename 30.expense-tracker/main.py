import sqlite3
import datetime

conn = sqlite3.connect("expense.db")
cur=conn.cursor()

while True:
    print("Select an option")
    print("1 Enter a new expense")
    print("2 View Expense Summary")

    choice = int(input())

    if choice==1:
        date = input("Enter the date of the expense (YYYY-MM-DD)")
        description = input("Enter the description of the expense")
        cur.execute("SELECT DISTINCT category FROM expenses")
        catagories = cur.fetchall()
        print("Select a category by number:")
        for idx,category in enumerate(catagories):
            print(f"{idx+1}. {category[0]}")
        print(f"{len(catagories+1)}. Create a new category")
        category_choice= input
        if category_choice == (len(catagories)+1):
            category = input("Enter the new category name: ")
        else:
            category = catagories[category_choice-1][0]

        price = input("Enter the price of the expense")

        cur.execute("INSERT INTO expenses (Date,description,category,price) VALUES (?,?,?,?), (date,)")
    elif choice==2:
        print("Select an opetion")
        print("View all expenses")
        print("View Monthly expenses by category")

        view_choice = int(input())
        if view_choice ==1:
            cur.execute("SELECT * FROM expenses")
            expenses = cur.fetchall() 
            for expense in expenses:
                print(expense)
        elif view_choice==2:
            month = input("Enter the month(MM)")
            year = input("Enter the year (YYYY)")
            cur.execute("SELECT category,SUM(price) FROM expenses WHERE strftime('%m,Date' = ? AND strftime(%Y,Date)= ? GROUP BY category)",(month,year))
            expense = cur.fetchall()
            for expense in expenses:
                print(f"Category: {expense[0]} , Total: {expense[1]}")
        else:
            exit()
    else:
        exit()
    
    repeat = input("Would You like to do something else (y/n)\n")

    if repeat.lower() != "y":
        break