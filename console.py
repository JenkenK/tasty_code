import pdb 
from models.customer import Customer
from models.cuisine import Cuisine
from models.restaurant import Restaurant
from models.order import Order
from models.dish import Dish

import repositories.customer_repository as customer_repository
import repositories.cuisine_repository as cuisine_repository
import repositories.restaurant_repository as restaurant_repository
import repositories.order_repository as order_repository
import repositories.dish_repository as dish_repository

customer_repository.delete_all()
cuisine_repository.delete_all()
restaurant_repository.delete_all()
order_repository.delete_all()
dish_repository.delete_all()

customer1 = Customer("Jenken", "1 Street Name", "Card", "07123456789", "Delivery")
customer_repository.save(customer1)
customer1 = Customer("Jenken2", "2 Street Name", "Card", "07123456789", "Delivery")
customer_repository.save(customer1)

chinese = Cuisine("Chinese")
cuisine_repository.save(chinese)
japanese = Cuisine("Japanese")
cuisine_repository.save(japanese)
fast_food = Cuisine("Fast Food")
cuisine_repository.save(fast_food)

mcdonalds = Restaurant("McDonalds", "137 Princes St", "01312263872", True, fast_food)
restaurant_repository.save(mcdonalds)

order1 = Order("2020-10-05 10:54:40", customer1, mcdonalds)
order_repository.save(order1)

order2 = Order("2020-10-05 11:12:20", customer1, mcdonalds )
order_repository.save(order2)

burger = Dish("Cheeseburger", 0.99, "A burger with cheese", mcdonalds)
dish_repository.save(burger)