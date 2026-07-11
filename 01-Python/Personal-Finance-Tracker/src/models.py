class Transaction:

    def __init__(self, transaction_type, amount):

        self.transaction_type = transaction_type
        self.amount = amount

    def display(self):

        print(
            f"{self.transaction_type:<8} ₹{self.amount:.2f}"
        )

    def to_dictionary(self):

        return {
            "type": self.transaction_type,
            "amount": self.amount
        }