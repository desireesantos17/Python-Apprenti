#Costco Food Court Ordering 

items = {
    "hot dog": 1,
    "chicken bake": 3,
    "sundae": 2
}

#Start and menu 
print("Welcome to the Costco's Foodcourt")
print("Menu:")
for item, price in items.items():
    print(f"{item} - ${price}")

#Insert Money 
balance = int(input("Enter your money"))

#Start order loop 
while balance > 0:
    print(f"\nBalance: ${balance}")
    choice = input("Order item: ").lower()

    if choice in items:
        price = items[choice]
        if balance >= price:
            balance -= price
            print(f"Dispensed: {choice}")
        else:
            print("Not enough money.")

    if input("Order again? (yes/no): ").lower()!= "yes":
        break

