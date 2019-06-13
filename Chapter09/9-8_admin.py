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
        print("\n Name: " + self.f_name.title() + ' ' + self.l_name.title())
        print("Age: " + str(self.age)) 
        print("Birthplace: " + self.birthplace.title())

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
        

class Admin(User):
    """Defines the admin user."""

    def __init__(self, f_name, l_name, age, birthplace):
        """Initialize attributes of parent class User, then the ones specific to admin."""
        super().__init__(f_name, l_name, age, birthplace)

        #initialize an empty set of privileges.
        self.privileges = Privileges()
        
class Privileges():
    """ Models the privileges of a user."""

    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        """Shows the privileges of a user."""
        print("\nPrivileges:")
        if self.privileges:
            for privilege in self.privileges:
                print("- " + privilege)
        else:
            print("- This user has no privileges.")


mike = Admin('mike', 'smith', 22, 'philadelphia') 
mike.describe_user()

mike.privileges.show_privileges()

print("\nAdding privileges...")
mike_privileges = [ 
    'can add post' ,
    'can delete post' ,
    'can ban user',
    'can get funky',
    'can ban other users',
    'can moderate chatrooms'
    ]
mike.privileges.privileges = mike_privileges
mike.privileges.show_privileges()

