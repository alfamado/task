# Contact quick lookup
name = ("Abdulmalik", "Rofiat", "Jubril")
contact = ("07056789123", "08087654321", "0812345679")
name_contact = dict(zip(name, contact))
print(name_contact)
ask = input("ask for a name: ")
print(name_contact.get(ask))