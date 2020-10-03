import pdb 
from models.customer import Customer
from models.cuisine import Cuisine

import repositories.customer_repositories as customer_repositories
import repositories.cuisine_repositories as cuisine_repositories

# customer_repositories.delete_all()

customer1 = Customer("Jenken", "1 Street Name", "Card", "07123456789", "Delivery")
customer_repositories.save(customer1)

chinese = Cuisine("Chinese")
cuisine_repositories.save(chinese)
japanese = Cuisine("Japanese")
cuisine_repositories.save(japanese)