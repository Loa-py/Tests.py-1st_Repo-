print("Welcome to the Daily Expense Tracker!")
print()
print("Menu:")
print("1. Add a new expense")
print("2. View all expenses")
print("3. Calculate total and average expense")
print("4. Clear all expenses")
print("5. Exit")

expenses = []

while True:
    choice = input()

    # Opción 1: Agregar gasto
    if choice == "1":
        amount = float(input())
        expenses.append(amount)
        print("Expense added successfully!")

    # Opción 2: Ver gastos
    elif choice == "2":
        if not expenses:
            print("No expenses recorded yet.")
        else:
            print("Your expenses:")
            for i, expense in enumerate(expenses, start=1):
                print(f"{i}. {expense}")

    # Opción 3: Total y promedio
    elif choice == "3":
        if not expenses:
            print("No expenses recorded yet.")
        else:
            total = sum(expenses)
            average = total / len(expenses)
            print(f"Total expense: {total}")
            print(f"Average expense: {average}")

    # Opción 4: Limpiar gastos
    elif choice == "4":
        expenses.clear()
        print("All expenses cleared.")

    # Opción 5: Salir
    elif choice == "5":
        print("Exiting the Daily Expense Tracker. Goodbye!")
        break
    
    else:
        print("Invalid choice. Please try again.")