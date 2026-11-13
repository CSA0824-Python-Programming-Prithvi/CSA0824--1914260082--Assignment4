
import os


# Automatically create sample input files
with open("day1.txt", "w") as file:
    file.write("Python Basics\n")
    file.write("Data Structures\n")

with open("day2.txt", "w") as file:
    file.write("Database Systems\n")
    file.write("Computer Networks\n")

with open("day3.txt", "w") as file:
    file.write("Operating Systems\n")
    file.write("Web Technology\n")


def save_returns(books):
    with open("returns.log", "a") as log:
        for book in books:
            log.write(book.strip() + "\n")


def process(filename):
    try:
        with open(filename, "r") as file:
            books = file.readlines()

        save_returns(books)
        print(filename, "processed successfully")

    except FileNotFoundError as error:
        with open("error.log", "a") as log:
            log.write(str(error) + "\n")

        print("Missing file:", filename)

    except OSError as error:
        with open("error.log", "a") as log:
            log.write(str(error) + "\n")

        print("File error:", error)


# Clear old logs before testing
for filename in ("returns.log", "error.log"):
    if os.path.exists(filename):
        os.remove(filename)


# Process three days
process("day1.txt")
process("day2.txt")
process("day3.txt")


# Display final returns log
print("\nRETURNED BOOKS LOG")

with open("returns.log", "r") as file:
    print(file.read())
