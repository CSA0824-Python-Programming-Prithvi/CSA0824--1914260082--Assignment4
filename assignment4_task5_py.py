
import os

# Automatically create input file
data = [
    "101,2026-10-01,P,Arun",
    "101,2026-10-02,A,Arun",
    "101,2026-10-03,A,Arun",
    "102,2026-10-01,A,Bala",
    "102,2026-10-02,A,Bala",
    "102,2026-10-03,A,Bala",
    "103,2026-10-01,P,Charan",
    "103,2026-10-02,P,Charan",
    "103,2026-10-03,P,Charan"
]

with open("attendance_data.txt", "w") as file:
    for line in data:
        file.write(line + "\n")


def read_data(filename):
    records = []

    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().split(",")

            if len(parts) == 4:
                records.append(parts)

    return records


def calculate_stats(records):
    students = {}

    for reg, date, status, name in records:
        if reg not in students:
            students[reg] = {
                "name": name,
                "present": 0,
                "absent": 0,
                "statuses": []
            }

        if status == "P":
            students[reg]["present"] += 1
        elif status == "A":
            students[reg]["absent"] += 1

        students[reg]["statuses"].append(status)

    return students


def generate_report(students):
    with open("attendance_report.txt", "w") as report:
        report.write("REGISTER NO,NAME,PERCENTAGE\n")

        for reg, details in students.items():
            total = details["present"] + details["absent"]
            percentage = details["present"] / total * 100

            report.write(
                f"{reg},{details['name']},{percentage:.2f}%\n"
            )

    with open("three_day_absentees.txt", "w") as report:
        for reg, details in students.items():
            if len(details["statuses"]) >= 3:
                if all(status == "A" for status in details["statuses"][-3:]):
                    report.write(
                        f"{reg},{details['name']}\n"
                    )


# Main program
try:
    records = read_data("attendance_data.txt")
    students = calculate_stats(records)
    generate_report(students)

    print("ATTENDANCE REPORT")
    with open("attendance_report.txt", "r") as file:
        print(file.read())

    print("STUDENTS ABSENT FOR THREE CONSECUTIVE DAYS")
    with open("three_day_absentees.txt", "r") as file:
        result = file.read()
        print(result if result else "No students found.")

except FileNotFoundError:
    print("Input file not found.")

