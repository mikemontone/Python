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

class IceCreamStand(Restaurant):
    """A attempt to model a ice cream stand."""

    def __init__(self, name, cuisine='ice cream'):
        """
        initialize attributes specific to an ice cream stand.
        """
        super().__init__(name, cuisine)
        self.flavors = []

    def list_flavors(self):
        """Outputs the flavors available."""
        print("\nWe have the following flavors available: ")
        for flavor in self.flavors:
            print("- " + flavor.title())

big_one = IceCreamStand('The Big One')
big_one.flavors = ['vanilla', 'strawberry', 'chocolate','mint']

big_one.describe_restaurant()
big_one.list_flavors()   
