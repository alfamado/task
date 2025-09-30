# Unique Name Collector
attendee_list = set()
for name in range(10):
    attending_name = input(f"Enter names of attendee {name+1}: ")
    attendee_list.add(attending_name)
print(attendee_list)
print(sorted(attendee_list))