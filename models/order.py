class Order():
    def __init__(self, order_timestamp, customer_id, restaurant_id, order_id=None):
        self.order_timestamp = order_timestamp
        self.customer_id = customer_id
        self.restaurant_id = restaurant_id
        self.id = order_id