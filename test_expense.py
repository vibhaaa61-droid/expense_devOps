from expense import calculate_expense

def test_calculate_expense():
    expenses = [500, 300, 200]
    assert calculate_expense(expenses) == 1000

def test_empty_expense():
    expenses = []
    assert calculate_expense(expenses) == 0