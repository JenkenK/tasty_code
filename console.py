import pdb 
from models.customer import Customer
from models.restaurant_category import RestaurantCategory

import repositories.customer_repositories as customer_repositories
import repositories.restaurant_category_repo as restaurant_category_repo

# customer_repositories.delete_all()

customer1 = Customer("Jenken", "1 Street Name", "Card", "07123456789", "Delivery")
customer_repositories.save(customer1)

chinese = RestaurantCategory("Chinese")
restaurant_category_repo.save(chinese)
chinese = RestaurantCategory("Japanese")
restaurant_category_repo.save(chinese)