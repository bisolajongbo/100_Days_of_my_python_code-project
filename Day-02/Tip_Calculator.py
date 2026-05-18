print("Welcome to tip calculator")
bill = float(input("What is your bill?\n"))
tip = int(input("What is your tip?\n"))
people = int(input("How many people  want to split the bill?\n"))
total= (bill*(tip/100)+bill)/people
Amount_to_pay= round(total,2)
print(f"Your split bill is:${Amount_to_pay}")
