class Restaurant():
    def __init__(self, name, address, phone_number, availability, customer, cuisine, id=None):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.availability = availability
        self.customer = customer
        self.cuisine = cuisine
        self.id = id