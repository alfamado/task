# Online Store Cart Calculation
items = ["book", "pen", "bag", "flask"]
prices =[500, 100, 5000, 10000]
pick_item = {}
cart_total=0

item1=int(input((f"how many {items[0]} do you want to buy: ")))
item2 =int(input((f"how many {items[1]} do you want to buy: ")))
item3=int(input((f"how many {items[2]} do you want to buy: ")))
item4 = int(input((f"how many {items[3]} do you want to buy: ")))
pick_item.update({"book" : item1*prices[0], "pen" : item2*prices[1], "bag" : item3*prices[2], "flask" : item4*prices[3]})
print(pick_item)
cart_total += pick_item["book"]
cart_total += pick_item["pen"]
cart_total += pick_item["bag"]
cart_total += pick_item["flask"]
print(f"you picked\n {item1}books\n{item2} pens\n{item3} bags\n{item4} flask\nTotal Price: {cart_total}")
