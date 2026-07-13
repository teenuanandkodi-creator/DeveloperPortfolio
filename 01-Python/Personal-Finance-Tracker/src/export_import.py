import csv
import json
import shutil
from datetime import datetime

def export_to_csv(transactions):

    if not transactions:
        print("\nNo transactions available.")
        return

    filename = "data/transactions.csv"

    with open(filename, "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow(
            [
                "Type",
                "Category",
                "Amount",
                "Date"
            ]
        )

        for transaction in transactions:

            writer.writerow(
                [
                    transaction["type"],
                    transaction["category"],
                    transaction["amount"],
                    transaction["date"]
                ]
            )

    print(f"\nTransactions exported to {filename}")

def import_from_csv(transactions):

    filename = "data/transactions.csv"

    try:

        with open(filename, "r") as file:

            reader = csv.DictReader(file)

            transactions.clear()

            for row in reader:

                transactions.append(
                    {
                        "type": row["Type"],
                        "category": row["Category"],
                        "amount": float(row["Amount"]),
                        "date": row["Date"]
                    }
                )

        with open(
            "data/transactions.json",
            "w"
        ) as json_file:

            json.dump(
                transactions,
                json_file,
                indent=4
            )

        print("\nTransactions imported successfully.")

    except FileNotFoundError:

        print("\nCSV file not found.")

def create_backup():

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    backup_file = (
        f"data/backups/transactions_{timestamp}.json"
    )

    shutil.copy(
        "data/transactions.json",
        backup_file
    )

    print("\nBackup created successfully.")

    print(backup_file)