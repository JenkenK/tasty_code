class Customer:
    def __init__(self, name, address, payment, phone_number, service, id=None):
        self.name = name
        self.address = address
        self.payment = payment
        self.phone_number = phone_number
        self.service = service
        self.id = id