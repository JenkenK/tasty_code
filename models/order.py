class Order():
    def __init__(self, order_timestamp, customer, restaurants, id=None):
        self.order_timestamp = order_timestamp
        self.customer = customer
        self.restaurant = restaurant
        self.id = id