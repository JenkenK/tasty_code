import pdb 
from models.customer import Customer
from models.cuisine import Cuisine

import repositories.customer_repository as customer_repository
import repositories.cuisine_repository as cuisine_repository

# customer_repository.delete_all()

customer1 = Customer("Jenken", "1 Street Name", "Card", "07123456789", "Delivery")
customer_repository.save(customer1)

chinese = Cuisine("Chinese")
cuisine_repository.save(chinese)
japanese = Cuisine("Japanese")
cuisine_repository.save(japanese)

