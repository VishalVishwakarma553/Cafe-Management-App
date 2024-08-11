#define menu
menu = {
    'Pasta': 40,
    'Pizza': 90,
    'Burger': 60,
    'Salad': 30,
    'Coffee': 80
}

#Greet
print("Welcome in our Restaurant where your taste is our responsibility!!!")
print("Here is our menu:")
print("Pizza : Rs90\nPasta : Rs40\nBurger : Rs60\nSalad : Rs30\nCoffee : Rs80")
customer_name = input("\nMay I have your good name, please! ")
order_total = 0
ordered_item = []
item1 = input("Enter your favourite item that you want to order = ")
if item1 in menu:
    order_total += menu[item1]
    print(f"your item {item1} has been added to your order")
    ordered_item.append((item1, menu[item1]))
else:
    print(f"Your item {item1} is not available right now")

while(True):
    another_order = input("Do you want to order something else! (Y/N)")
    if another_order.upper() == "Y":
        item2 = input("Enter Your second order = ")
        if(item2 in menu):
            order_total += menu[item2]
            print(f"item {item2} has been added")
            ordered_item.append((item2, menu[item2]))
        else:
            print(f"your item {item2} is not available right now")
    else:
        break
print(f"\nThank You, Dear {customer_name}, for your order!")
print("Here is your receipt:")
for item, price in ordered_item:
    print(f"{item} : Rs{price}")
print(f"The total amount to pay is {order_total}")
