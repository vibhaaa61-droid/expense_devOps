
import sys

def calculate_expense(expenses):
    return sum(expenses)

if __name__ == "__main__":

    expenses = [float(x) for x in sys.argv[1:]]

    total = calculate_expense(expenses)

    print("EXPENSE TRACKER")
    print("-------------------")
    print("Expenses:", expenses)
    print("Total Expenses:", total)
