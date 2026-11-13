
import os

folder = "attendance"
os.makedirs(folder, exist_ok=True)

# Automatically create input files
with open(folder + "/day1.txt", "w") as f:
    f.write("101,2026-10-01,P\n")
    f.write("102,2026-10-01,A\n")
    f.write("103,2026-10-01,P\n")

with open(folder + "/day2.txt", "w") as f:
    f.write("101,2026-10-02,P\n")
    f.write("102,2026-10-02,P\n")
    f.write("103,2026-10-02\n")

attendance = {}
errors = []

for filename in os.listdir(folder):
    if filename.endswith(".txt"):
        with open(os.path.join(folder, filename), "r") as file:
            for line_no, line in enumerate(file, 1):
                parts = line.strip().split(",")

                if len(parts) != 3 or parts[2] not in ("P", "A"):
                    errors.append((filename, line_no, "Invalid fields"))
                    continue

                reg = parts[0]

                if reg not in attendance:
                    attendance[reg] = [0, 0]

                if parts[2] == "P":
                    attendance[reg][0] += 1
                else:
                    attendance[reg][1] += 1

print("ATTENDANCE REPORT")
print("Register No, Present, Absent, Percentage")

for reg, values in attendance.items():
    total = sum(values)
    percentage = values[0] / total * 100

    print(reg, values[0], values[1], f"{percentage:.2f}%")

print("\nStudents Below 75%:")

for reg, values in attendance.items():
    percentage = values[0] / sum(values) * 100
    if percentage < 75:
        print(reg, f"{percentage:.2f}%")

print("\nErrors:")
for error in errors:
    print(error)
