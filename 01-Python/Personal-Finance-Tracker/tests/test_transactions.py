import unittest


class TestFinanceTracker(unittest.TestCase):

    def test_income_balance(self):

        transactions = [
            {
                "type": "Income",
                "amount": 5000
            }
        ]

        income = sum(
            t["amount"]
            for t in transactions
            if t["type"] == "Income"
        )

        self.assertEqual(income, 5000)

    def test_expense_balance(self):

        transactions = [
            {
                "type": "Expense",
                "amount": 1000
            }
        ]

        expense = sum(
            t["amount"]
            for t in transactions
            if t["type"] == "Expense"
        )

        self.assertEqual(expense, 1000)


if __name__ == "__main__":
    unittest.main()