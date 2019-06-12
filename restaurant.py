#!/opt/bb/bin/python3.6

class Restaurant():
    """A simple attempt to model a restaurant."""

    def __init__(self, name, cuisine):
        """Initialize name and type attributes."""
        self.name = name
        self.cuisine = cuisine

    def describe_restaurant(self):
        """Describe the restaurant name and type."""
        print("The name of the restaurant is " + self.name.title() + ".")
        print("The type of cuisine served is " + self.cuisine.title() + ".")

    def open_restaurant(self):
        """ States that the restaurant is open."""
        print(self.name.title() + " is currently open.")

restaurant = Restaurant('mcdonalds','burgers')
restaurant1 = Restaurant('Joes', 'steakhouse')
restaurant2 = Restaurant('Chipotle','mexican')

restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant1.describe_restaurant()
restaurant1.open_restaurant()

restaurant2.describe_restaurant()
restaurant2.open_restaurant()
