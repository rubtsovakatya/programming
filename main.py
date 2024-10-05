from product import Product, Material, Jewelry
from inventory import Inventory
from order import Order, OrderDetails
from user import User, Worker, WorkerCustomer

registered_workers = [
    Worker("101", "Craftsman"),
    Worker("102", "Designer"),
    Worker("103", "Salesperson"),
]

print("Welcome to our jewelry store!")

user_name = input("Please enter your name: ")
user_phone = input("Please enter your phone number: ")

is_worker = input("Are you a worker in our workshop? (yes/no): ").strip().lower()

if is_worker == "yes":
    worker_id = input("Please enter your worker ID: ")
    position = input("Please enter your position: ")

    if Worker.is_registered_worker(worker_id, position, registered_workers):
        user = WorkerCustomer(user_name, user_phone, worker_id, position)
    else:
        print("You are not a registered worker. No discount will be applied.")
        user = User(user_name, user_phone)
else:
    user = User(user_name, user_phone)

order = Order()
order_details = OrderDetails(user, order)

gold = Material("Gold")
silver = Material("Silver")
diamond = Material("Diamond")

ring = Jewelry("Golden Ring", 500, 101, gold)
necklace = Jewelry("Silver Necklace", 250, 102, silver)
bracelet = Jewelry("Diamond Bracelet", 1500, 103, diamond)

inventory = Inventory()
inventory.add_product(ring, 10)
inventory.add_product(necklace, 5)
inventory.add_product(bracelet, 3)

inventory.display_inventory()

while True:
    index_input = input("Enter the index of the jewelry you want to order (or -1 to finish): ")

    if not index_input.isdigit() and index_input != "-1":
        print("Invalid input. Please enter a valid index.")
        continue

    index = int(index_input)

    if index == -1:
        break

    if index < 1 or index > len(inventory.stock):
        print("Invalid index. Please try again.")
        continue

    product_name = list(inventory.stock.keys())[index - 1]
    quantity_input = input(f"Enter the quantity of {product_name} you want to order: ")

    quantity = int(quantity_input)
    product = inventory.stock[product_name]["product"]
    available_quantity = inventory.stock[product_name]["quantity"]

    if quantity > available_quantity:
        print(f"Sorry, we only have {available_quantity} of {product_name}.")
    else:
        order.add_product(product, quantity)
        inventory.update_stock(product_name, -quantity)
        print(f"{quantity} of {product_name} added to your order.")

if isinstance(user, WorkerCustomer):
    total_price_with_discount = user.apply_discount(order.total_price)
    print(f"You received a {user.discount_percentage}% discount as an employee!")
    print(f"Price after discount: {total_price_with_discount}")
    order.total_price = total_price_with_discount

order_details.display_order_details()
