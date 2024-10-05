from product import Product

class User:
    def __init__(self, user_name, user_phone):
        self.user_name = user_name
        self.user_phone = user_phone

class Worker:
    def __init__(self, worker_id, position):
        self.worker_id = worker_id
        self.position = position

    @staticmethod
    def is_registered_worker(worker_id, position, registered_workers):
        return any(worker.worker_id == worker_id and worker.position == position for worker in registered_workers)

class WorkerCustomer(User, Worker):
    def __init__(self, user_name, user_phone, worker_id, position):
        User.__init__(self, user_name, user_phone)
        Worker.__init__(self, worker_id, position)
        self.discount_percentage = 20

    def apply_discount(self, total_price):
        return Product.calculate_discount(total_price, self.discount_percentage)