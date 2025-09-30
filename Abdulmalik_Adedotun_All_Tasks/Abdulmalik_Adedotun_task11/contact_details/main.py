# project/main.py
# If your files aren't in a "project" package, adjust imports accordingly:
from contact_details import contact, contact_csv, display


def handle_create():
    print("\n👉 Enter contact details (type 'exit' at any prompt to stop)\n")
    while True:
        name = input("Name: ").strip()
        if name.lower() == "exit":
            break

        phone = input("Phone (11 digits, starts with 0): ").strip()
        if phone.lower() == "exit":
            break

        age = input("Age: ").strip()
        if age.lower() == "exit":
            break

        job = input("Job Title: ").strip()
        if job.lower() == "exit":
            break

        ok, msg = contact.create(name, phone, age, job)
        print(("✅ " if ok else "❌ ") + msg + "\n")
        # keep looping to allow multiple entries; user types 'exit' to stop


def handle_update():
    contacts = contact.read()
    if not contacts:
        print("📭 No contacts to update.\n")
        return

    display.show_contacts(contacts)
    try:
        index = int(input("Enter contact number to update: ")) - 1
    except ValueError:
        print("❌ Please enter a valid number.\n")
        return

    if not (0 <= index < len(contacts)):
        print("❌ Invalid contact number.\n")
        return

    print("\nWhat do you want to update?")
    print("1. Name")
    print("2. Phone")
    print("3. Age")
    print("4. Job Title")
    try:
        field_choice = int(input("Choose (1-4): ").strip())
    except ValueError:
        print("❌ Please enter a valid number.\n")
        return

    field_map = {1: "name", 2: "phone", 3: "age", 4: "job"}
    field = field_map.get(field_choice)
    if not field:
        print("❌ Invalid choice.\n")
        return

    new_value = input(f"Enter new {field}: ").strip()
    if new_value.lower() == "exit":
        print("❌ Update cancelled.\n")
        return

    ok, msg = contact.update(index, field, new_value)
    print(("✅ " if ok else "❌ ") + msg + "\n")


def handle_delete():
    contacts = contact.read()
    if not contacts:
        print("📭 No contacts to delete.\n")
        return

    display.show_contacts(contacts)
    try:
        index = int(input("Enter contact number to delete: ")) - 1
    except ValueError:
        print("❌ Please enter a valid number.\n")
        return

    if not (0 <= index < len(contacts)):
        print("❌ Invalid contact number.\n")
        return

    confirm = input("Are you sure? (y/n): ").strip().lower()
    if confirm != "y":
        print("❌ Deletion cancelled.\n")
        return

    ok, msg = contact.delete(index)
    print(("✅ " if ok else "❌ ") + msg + "\n")


def handle_read():
    display.show_contacts(contact.read())


def handle_search():
    if not contact.read():
        print("📭 No contacts to search.\n")
        return
    keyword = input("Enter name or phone to search: ").strip()
    results = contact.search(keyword)
    display.show_search_results(results)


def handle_save():
    contact_csv.save_to_csv(contact.read())
    print("✅ Saved to contacts.csv\n")


def handle_load():
    loaded = contact_csv.load_from_csv()
    # Replace in-memory list with loaded data
    contact.contacts.clear()
    contact.contacts.extend(loaded)
    print(f"✅ Loaded {len(loaded)} contact(s) from contacts.csv\n")


def main():
    while True:
        display.menu()
        choice_str = input("Choose (1-8): ").strip()
        if not choice_str.isdigit():
            print("❌ Please enter a number.\n")
            continue

        choice = int(choice_str)
        if choice == 1:
            handle_create()
        elif choice == 2:
            handle_update()
        elif choice == 3:
            handle_delete()
        elif choice == 4:
            handle_read()
        elif choice == 5:
            handle_search()
        elif choice == 6:
            handle_save()
        elif choice == 7:
            handle_load()
        elif choice == 8:
            print("👋 Goodbye")
            break
        else:
            print("❌ Invalid choice, pick 1–8.\n")


if __name__ == "__main__":
    main()


# ---

# Why this meets your requirements

# Validations live in contact.py (single source of truth).

# Every public method returns (ok, message) so main.py can display feedback without duplicating logic.

# Phone rules: digits only, 11 digits, starts with 0, unique (including on update).

# Name & Job: alphabets only, not empty.

# Age: digits only; stored as int.

# Search: by partial name (case-insensitive) or exact phone.

# CSV: separate, clean persistence layer (contact_csv.py).

# Display: menus and pretty prints (display.py).

# Main: collects input, supports multiple creates with “exit” at any prompt, and orchestrates everything.


# If you want different validation for names/jobs (e.g., allow spaces like “Mary Jane” or roles like “Data Scientist”), I can relax isalpha() to allow spaces/hyphens.
