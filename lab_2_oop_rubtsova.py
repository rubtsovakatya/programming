class Product:
    __price = 0

    def __init__(self, product_name, recommended_price, craftsman_id):
        self.product_name = product_name
        self.recommended_price = recommended_price
        self.craftsman_id = craftsman_id
        Product.__price = recommended_price

    def set_product_data(self, product_name, craftsman_id):
        self.product_name = product_name
        self.craftsman_id = craftsman_id

    def display_info(self):
        print(f"Product: {self.product_name}, Price: {self.recommended_price}, Craftsman: {self.craftsman_id}")

    @staticmethod
    def calculate_discount(price, discount_percentage):
        return price - (price * discount_percentage / 100)

class Jewelry(Product):
    def __init__(self, product_name, recommended_price, craftsman_id, material):
        super().__init__(product_name, recommended_price, craftsman_id)
        self.material = material

    def display_info(self):
        print(f"Jewelry: {self.product_name}, Material: {self.material}, Price: {self.recommended_price}, Craftsman: {self.craftsman_id}")

class WorkshopInventory:
    def __init__(self, stock_quantity):
        self.stock_quantity = stock_quantity

    def update_stock(self, quantity):
        self.stock_quantity += quantity


class JewelryInventory(Jewelry, WorkshopInventory):
    def __init__(self, product_name, recommended_price, craftsman_id, material, stock_quantity):
        Jewelry.__init__(self, product_name, recommended_price, craftsman_id, material)
        WorkshopInventory.__init__(self, stock_quantity)

    def display_full_info(self):
        print(f"Jewelry: {self.product_name}, Material: {self.material}, Price: {self.recommended_price}, Craftsman: {self.craftsman_id}, Stock: {self.stock_quantity}")


ring = Jewelry("Sliver Ring", 500, 101, "Gold")
necklace = JewelryInventory("Silver Necklace", 250, 102, "Silver", 10)

ring.display_info()
necklace.display_full_info()

discounted_price = Product.calculate_discount(500, 10)
print(f"Discounted price: {discounted_price}")

ring.set_product_data("Golden Ring", 202)

for item in [ring, necklace]:
    item.display_info()

necklace.update_stock(5)
print(f"Updated stock: {necklace.stock_quantity}")

