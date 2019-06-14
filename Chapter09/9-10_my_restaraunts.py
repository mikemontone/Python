#!/opt/bb/bin/python3.6

from restaurant import Restaurant

restaurant1 = Restaurant('mcdonalds','burgers')
joes = Restaurant('Joes', 'steakhouse')

restaurant1.describe_restaurant()

restaurant1.describe_restaurant()
restaurant1.open_restaurant()
restaurant1.customers_served()
restaurant1.number_served = 30
restaurant1.customers_served()
restaurant1.increment_customers(50)
restaurant1.customers_served()

