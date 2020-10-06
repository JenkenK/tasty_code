class Order():
    def __init__(self, order_timestamp, customer, restaurant, dishes, id=None):
        self.order_timestamp = order_timestamp
        self.customer = customer
        self.restaurant = restaurant
        self.dishes = dishes
        self.id = id