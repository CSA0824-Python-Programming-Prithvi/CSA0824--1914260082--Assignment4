

from decimal import Decimal, InvalidOperation
from pathlib import Path

def calculate_bill(filename):
    total = Decimal("0.00")
    rejected = []

    try:
        file_path = Path(__file__).resolve().parent / filename

        with open(file_path, "r", encoding="utf-8") as file:
            for line_no, line in enumerate(file, start=1):
                try:
                    reg_no, name, amount = line.strip().split(",")

                    bill = Decimal(amount)
                    total += bill

                except (ValueError, InvalidOperation):
                    rejected.append((line_no, line.strip()))

        print("MESS BILL SUMMARY")
        print("-----------------")
        print("Total Bill Amount: Rs.", total)
        print("Rejected Records:")

        for record in rejected:
            print(record)

    except FileNotFoundError:
        print("Error: Input file not found.")
        print("Please save mess_oct.txt in the same folder as this Python file.")

calculate_bill("mess_oct.txt")
