# project/display.py

def menu():
    print("\n=== Phone Contact Manager ===")
    print("1. Create Contact")
    print("2. Update Contact")
    print("3. Delete Contact")
    print("4. Read Contacts")
    print("5. Search Contact")
    print("6. Save to CSV")
    print("7. Load from CSV")
    print("8. Exit")

def show_contacts(contacts):
    if not contacts:
        print("📭 No contacts found.\n")
        return
    print("\n=== All Contacts ===")
    for i, c in enumerate(contacts, start=1):
        print(f"{i}. Name: {c[0]}, Phone: {c[1]}, Age: {c[2]}, Job: {c[3]}")
    print()

def show_search_results(results):
    if not results:
        print("❌ No matching contact found.\n")
        return
    print("\n🔎 Search Results:")
    for i, c in results:
        print(f"{i}. Name: {c[0]}, Phone: {c[1]}, Age: {c[2]}, Job: {c[3]}")
    print()
