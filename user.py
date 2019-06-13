#!/opt/bb/bin/python3.6

class User():
    """ A attempt to model a user."""

    def __init__(self, f_name, l_name, age, birthplace):
        """Initialize the name and age attributes."""
        self.f_name = f_name
        self.l_name = l_name
        self.age = age
        self.birthplace = birthplace
        self.login_attempts = 0

    def describe_user(self):
        """Prints a summary of the user."""
        print("\nThe user's name is " + self.f_name.title() + ' ' + self.l_name.title() + ".")
        print("The user is " + str(self.age) + " and was born in " + self.birthplace.title())

    def greet_user(self):
        """Prints a personalized greeting to user."""
        print("Hello " + self.f_name.title() + "!, hope you're well today!")

#    def read_login_attempts(self):
#        "States current amounts of login attempts."""
#        print("The current number of login attempts is: " + str(self.login_attempts) + ".")

    def increment_login_attempts(self):
        """ increments the login attempts by 1."""
        self.login_attempts += 1 

    def reset_login_attempts(self):
        """ resets login attempts to 0."""
        self.login_attempts = 0
        print("\nLogin attempts have been reset. Current number of attempts: " + str(self.login_attempts))
        

mike = User('mike' , 'smith' , 23 , 'philadelphia')        

mike.describe_user()
mike.greet_user()

print("\nMaking 3 login attmepts...")
mike.increment_login_attempts()
mike.increment_login_attempts()
mike.increment_login_attempts()
print("     Login Attempts:  " + str(mike.login_attempts))
mike.reset_login_attempts()

tony = User('tony' , 'castro' , 24 , 'nyc' )
tony.describe_user()
tony.greet_user()

print("\nMaking 2 login attmepts...")
tony.increment_login_attempts()
tony.increment_login_attempts()
print("     Login Attempts:  " + str(tony.login_attempts))

