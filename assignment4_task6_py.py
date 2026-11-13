
import os

# Create input and output folders
os.makedirs("input", exist_ok=True)
os.makedirs("output", exist_ok=True)

# Automatically create sample department files
files_data = {
    "dept1.txt": [
        "101,Arun,CSE,arun@gmail.com,Singing;Dancing",
        "102,Bala,IT,bala@gmail.com,Dancing"
    ],
    "dept2.txt": [
        "101,Arun,CSE,arun@gmail.com,Singing",
        "103,Charan,ECE,charanmail.com,Drama",
        "104,David,EEE,david@gmail.com"
    ],
    "dept3.txt": [
        "105,Elan,MECH,elan@gmail.com,Music;Drama"
    ],
    "dept4.txt": [
        "106,Fahad,CSE,fahad@gmail.com,Singing"
    ]
}

for filename, records in files_data.items():
    with open(os.path.join("input", filename), "w") as file:
        for record in records:
            file.write(record + "\n")


# Read and process department files
valid_records = []
errors = []
seen_registers = set()
missing_files = 0

for i in range(1, 6):
    filename = "dept" + str(i) + ".txt"
    path = os.path.join("input", filename)

    try:
        with open(path, "r") as file:
            for line_no, line in enumerate(file, 1):
                parts = line.strip().split(",")

                if len(parts) != 5:
                    errors.append(
                        f"{filename}, line {line_no}: Damaged record"
                    )
                    continue

                reg, name, dept, email, events = parts

                if reg in seen_registers:
                    errors.append(
                        f"{filename}, line {line_no}: Duplicate register number {reg}"
                    )
                    continue

                if "@" not in email or "." not in email.split("@")[-1]:
                    errors.append(
                        f"{filename}, line {line_no}: Invalid email"
                    )
                    continue

                seen_registers.add(reg)
                valid_records.append(parts)

    except FileNotFoundError:
        missing_files += 1
        errors.append(filename + ": File not found")


# Create master list
with open("output/master_list.txt", "w") as file:
    for record in valid_records:
        file.write(",".join(record) + "\n")


# Create event-wise files
event_counts = {}

for record in valid_records:
    reg, name, dept, email, events = record

    for event in events.split(";"):
        event = event.strip()

        if event:
            event_counts[event] = event_counts.get(event, 0) + 1

            with open("output/" + event + ".txt", "a") as file:
                file.write(reg + "," + name + "," + dept + "\n")


# Create summary report
with open("output/summary.txt", "w") as file:
    file.write("COLLEGE FEST SUMMARY\n")
    file.write("Valid registrations: " + str(len(valid_records)) + "\n")
    file.write("Rejected records: " + str(len(errors) - missing_files) + "\n")
    file.write("Missing files: " + str(missing_files) + "\n")
    file.write("\nEVENT COUNTS\n")

    for event, count in event_counts.items():
        file.write(event + ": " + str(count) + "\n")


# Create error log
with open("output/error_log.txt", "w") as file:
    for error in errors:
        file.write(error + "\n")


# Display results
print("COLLEGE FEST REGISTRATION REPORT")
print("--------------------------------")
print("Valid registrations:", len(valid_records))
print("Rejected records:", len(errors) - missing_files)
print("Missing files:", missing_files)

print("\nEVENT COUNTS")
for event, count in event_counts.items():
    print(event, ":", count)

print("\nERROR LOG")
for error in errors:
    print(error)

print("\nAll output files created successfully in the output folder.")


