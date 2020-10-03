import pdb 
from models.customer import Customer
from models.cuisine import Cuisine
from models.restaurant import Restaurant

import repositories.customer_repository as customer_repository
import repositories.cuisine_repository as cuisine_repository
import repositories.restaurant_repository as restaurant_repository

# customer_repository.delete_all()

customer1 = Customer("Jenken", "1 Street Name", "Card", "07123456789", "Delivery")
customer_repository.save(customer1)

chinese = Cuisine("Chinese")
cuisine_repository.save(chinese)
japanese = Cuisine("Japanese")
cuisine_repository.save(japanese)
fast_food = Cuisine("Fast Food")
cuisine_repository.save(fast_food)

mcdonalds = Restaurant("McDonalds", "137 Princes St", "01312263872", True, fast_food)
restaurant_repository.save(mcdonalds)