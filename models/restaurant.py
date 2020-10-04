class Restaurant():
    def __init__(self, name, address, phone_number, availability, cuisine_id, restaurant_id=None):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.availability = availability
        self.cuisine_id = cuisine_id
        self.id = restaurant_id