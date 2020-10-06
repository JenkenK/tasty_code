import pdb 
from models.customer import Customer
from models.cuisine import Cuisine
from models.restaurant import Restaurant
from models.order import Order
from models.dish import Dish
from models.order_dish import OrderDish

import repositories.customer_repository as customer_repository
import repositories.cuisine_repository as cuisine_repository
import repositories.restaurant_repository as restaurant_repository
import repositories.order_repository as order_repository
import repositories.dish_repository as dish_repository
import repositories.order_dish_repository as order_dish_repository

order_dish_repository.delete_all()
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
kfc = Restaurant("KFC", "36 Nicolson St", "01316629524", True, fast_food)
restaurant_repository.save(kfc)

cheeseburger = Dish("Cheeseburger", 0.99, "A burger with cheese", mcdonalds)
dish_repository.save(cheeseburger)
doublecheeseburger = Dish("Double Cheeseburger", 1.99, "A double burger with cheese", mcdonalds)
dish_repository.save(doublecheeseburger)
triplecheeseburger = Dish("Triple Cheeseburger", 2.99, "A triple burger with cheese", mcdonalds)
dish_repository.save(triplecheeseburger)
quarterpounder = Dish("Quarter Punder", 1.99, "A burger that is a quarter of a pound", mcdonalds)
dish_repository.save(quarterpounder)
chickenlegend = Dish("Chicken Legend", 1.99, "A chicken burger", mcdonalds)
dish_repository.save(chickenlegend)

hotwings = Dish("Hot Wing", 0.50, "Hot and spicy chicken wings", kfc)
dish_repository.save(hotwings)
bucket = Dish("10 Piece Bucket", 9.99, "Bucket 10 of original piece", kfc)
dish_repository.save(bucket)
chips = Dish("Chips", 0.99, "Regular chips", kfc)
dish_repository.save(chips)
burgermeal = Dish("Fillet Burger Meal", 3.99, "Fillet burger meal with chips and drink", kfc)
dish_repository.save(burgermeal)
fanta = Dish("Fanta", 0.99, "Fanta", kfc)
dish_repository.save(fanta)

order1 = Order("2020-10-05 10:54:40", customer1, mcdonalds)
order_repository.save(order1)

order2 = Order("2020-10-05 11:12:20", customer1, kfc )
order_repository.save(order2)

order_dishes1 = OrderDish(order1, cheeseburger)
order_dish_repository.save(order_dishes1)
order_dishes2 = OrderDish(order1, doublecheeseburger)
order_dish_repository.save(order_dishes2)
