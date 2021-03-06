#!/opt/bb/bin/python3.6

class Restaurant():
    """A simple attempt to model a restaurant."""

    def __init__(self, name, cuisine):
        """Initialize name and type attributes."""
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0

    def describe_restaurant(self):
        """Describe the restaurant name and type."""
        print("The name of the restaurant is " + self.name.title() + ".")
        print("The type of cuisine served is " + self.cuisine.title() + ".")

    def open_restaurant(self):
        """ States that the restaurant is open."""
        print(self.name.title() + " is currently open.")

    def customers_served(self):
        """ States the number of customers served today."""
        print("This restaurant has served " + str(self.number_served) + " customers today.")
        print("\n")

    def increment_customers(self, customers):
        """Add the given amount to the number of customer's served."""
        self.number_served += customers

restaurant = Restaurant('mcdonalds','burgers')
restaurant1 = Restaurant('Joes', 'steakhouse')
restaurant2 = Restaurant('Chipotle','mexican')

restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.customers_served()
restaurant.number_served = 30
restaurant.customers_served()
restaurant.increment_customers(50)
restaurant.customers_served()

restaurant1.describe_restaurant()
restaurant1.open_restaurant()
restaurant1.customers_served()

restaurant2.describe_restaurant()
restaurant2.open_restaurant()
restaurant2.customers_served()
