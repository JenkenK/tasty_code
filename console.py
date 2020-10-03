import pdb 
from models.customer import Customer

import repositories.customer_repositories as customer_repositories

# customer_repositories.delete_all()

customer1 = Customer("Jenken", "1 Street Name", "Card", "07123456789", "Delivery")
customer_repositories.save(customer1)