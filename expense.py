def calculate_expense(expenses):
    total = sum(expenses)
    return total

# Main program
no_of_expenses = int(input("Enter number of expenses: "))

expenses = []

for i in range(no_of_expenses):
    amount = float(input("Enter expense amount: "))
    expenses.append(amount)

total = calculate_expense(expenses)

print("EXPENSE TRACKER")
print("----------------------")
print("Total Expenses:", total)