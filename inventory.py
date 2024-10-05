class Inventory:
    def __init__(self):
        self.stock = {}

    def add_product(self, product, quantity):
        if product.product_name in self.stock:
            self.stock[product.product_name]["quantity"] += quantity
        else:
            self.stock[product.product_name] = {
                "product": product,
                "quantity": quantity
            }

    def update_stock(self, product_name, quantity):
        if product_name in self.stock:
            self.stock[product_name]["quantity"] += quantity
        else:
            print(f"Product {product_name} is not in the inventory.")

    def display_inventory(self):
        print("\nAvailable Jewelry:")
        for index, (product_name, details) in enumerate(self.stock.items(), start=1):
            product = details["product"]
            quantity = details["quantity"]
            print(f"{index}: {product_name} (Quantity: {quantity}, Price: {product.recommended_price})")