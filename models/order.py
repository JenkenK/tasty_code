class Order():
    def __init__(self, order_timestamp, customer, restaurant, order_id=None):
        self.order_timestamp = order_timestamp
        self.customer = customer
        self.restaurant = restaurant
        self.id = order_id