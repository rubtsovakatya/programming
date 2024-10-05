class Order:
    def __init__(self):
        self.products = {}
        self.total_price = 0

    def add_product(self, product, quantity):
        if product.product_name in self.products:
            self.products[product.product_name]["quantity"] += quantity
        else:
            self.products[product.product_name] = {
                "product": product,
                "quantity": quantity
            }
        self.total_price += product.recommended_price * quantity

class OrderDetails:
    def __init__(self, user, order):
        self.user = user
        self.order = order

    def display_order_details(self):
        print(f"\nCustomer Name: {self.user.user_name}")
        print(f"Customer Phone: {self.user.user_phone}")
        print(f"Total Items Ordered: {len(self.order.products)}")
        print(f"Total Price: {self.order.total_price}")
        for product_info in self.order.products.values():
            product = product_info["product"]
            quantity = product_info["quantity"]
            print(f"Product: {product.product_name}, Quantity: {quantity}, Subtotal: {product.recommended_price * quantity}")