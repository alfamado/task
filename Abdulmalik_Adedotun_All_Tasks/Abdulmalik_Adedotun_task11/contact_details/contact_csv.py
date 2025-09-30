# project/contact_csv.py
import csv
import os

FILENAME = "contacts.csv"
HEADER = ["Name", "Phone", "Age", "Job Title"]


def init_file():
    if not os.path.exists(FILENAME):
        with open(FILENAME, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(HEADER)


def save_to_csv(contacts):
    """Overwrite CSV with current contacts."""
    init_file()
    with open(FILENAME, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(HEADER)
        for c in contacts:
            # c = [name, phone, age(int), job]
            writer.writerow([c[0], c[1], c[2], c[3]])


def load_from_csv():
    """
    Read CSV (skips header); returns a list of contacts as [name, phone, age(int), job].
    If Age is not digits, row is skipped for safety.
    """
    init_file()
    loaded = []
    with open(FILENAME, "r") as f:
        reader = csv.reader(f)
        header = next(reader, None)
        for row in reader:
            if not row or len(row) < 4:
                continue
            name, phone, age_str, job = row[0].strip(), row[1].strip(), row[2].strip(), row[3].strip()
            if not age_str.isdigit():
                continue # skip bad rows
            loaded.append([name, phone, int(age_str), job])
    return loaded