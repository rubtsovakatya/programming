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

class Material:
    def __init__(self, material_name):
        self.material_name = material_name

class Jewelry(Product):
    def __init__(self, product_name, recommended_price, craftsman_id, material):
        super().__init__(product_name, recommended_price, craftsman_id)
        self.material = material

    def display_info(self):
        print(f"{self.product_name} (Material: {self.material.material_name}, Price: {self.recommended_price})")