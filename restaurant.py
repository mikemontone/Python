#!/opt/bb/bin/python3.6

class Restaurant():
    """A simple attempt to model a restaurant."""

    def __init__(self, rest_name, cuisine_type):
        """Initialize name and type attributes."""
        self.rest_name = rest_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Describe the restaurant name and type."""
        print("The name of the restaurant is " + self.rest_name.title() + ".")
        print("The type of cuisine served at is " + self.cuisine_type() + ".")

    def open_restaurant(self):
        """ States that the restaurant is open."""
        print(self.rest_name.title() + " is currently open.")

restaurant = Restaurant('mcdonalds','burgers')
#restaurant1 = Restaurant('Joes', 'steakhouse')

restaurant.describe_restaurant()
restaurant.open_restaurant()

#restaurant1.describe_restaurant()
#restaurant1.open_restaurant()
