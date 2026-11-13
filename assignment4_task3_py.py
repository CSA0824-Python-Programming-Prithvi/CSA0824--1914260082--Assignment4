
class InvalidRecord(Exception):
    pass


def parse_line(line):
    parts = line.strip().split(",")

    if len(parts) != 3:
        raise InvalidRecord(
            f"expected 3 fields, found {len(parts)}"
        )

    if parts[2] not in ("P", "A"):
        raise InvalidRecord(
            f"invalid status '{parts[2]}'"
        )

    return parts


def summarise(filename):
    present = 0
    absent = 0
    errors = []

    try:
        with open(filename, "r") as file:
            for line_no, line in enumerate(file, 1):
                try:
                    record = parse_line(line)

                    if record[2] == "P":
                        present += 1
                    else:
                        absent += 1

                except InvalidRecord as error:
                    errors.append((line_no, str(error)))

    except FileNotFoundError as error:
        raise RuntimeError("Attendance file is missing") from error

    else:
        print("File processed successfully.")

    finally:
        print("Processing completed.")

    return present, absent, errors


# Automatically create sample input file
with open("attendance_q3.txt", "w") as file:
    file.write("192311001,2026-10-08,P\n")
    file.write("192311002,2026-10-08,A\n")
    file.write("192311003,2026-10-08\n")
    file.write("192311004,2026-10-08,L\n")


try:
    result = summarise("attendance_q3.txt")
    print(result)

except RuntimeError as error:
    print(error)

