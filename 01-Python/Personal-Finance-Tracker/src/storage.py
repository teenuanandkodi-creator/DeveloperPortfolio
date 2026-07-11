import json
import os

DATA_FILE = "data/transactions.json"


def load_transactions():

    if os.path.exists(DATA_FILE):

        try:

            with open(DATA_FILE, "r") as file:
                return json.load(file)

        except json.JSONDecodeError:
            return []

    return []


def save_transactions(transactions):

    with open(DATA_FILE, "w") as file:

        json.dump(transactions, file, indent=4)