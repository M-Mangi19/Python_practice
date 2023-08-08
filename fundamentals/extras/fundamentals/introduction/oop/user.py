# ATTRIBUTES
class User:

    def __init__(self, first_name, last_name, email, age, is_rewards_memeber, gold_card_points):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0


    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print(self.gold_card_points)
        self = self
        return self

    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points = 200
        self = self
        return self


    def spend_points(self, amount):
        self.gold_card_points = self.gold_card_points - amount
        self.amount = amount
        return self

matt = User("Matt", "Mangiaracina", "matt@email.com", 41, False, 0)
katrina = User("Katrina", "Mangiaracina", "trina@email.com", 41, False, 0)
ripley = User("Ellen", "Ripley", "rips@email.com", 6, False, 0)
talula = User("Talula", "Bear", "chonks@email.com", 4, False, 0)

matt.enroll().spend_points(50).display_info()
katrina.enroll().spend_points(80).display_info()
ripley.display_info()
talula.display_info()




# methods
# display_info(self) - Have this method print all of the users' details on separate lines.
# enroll(self) - Have this method change the user's member status to True and set their gold card points to 200.
# spend_points(self, amount) - have this method decrease the user's points by the amount specified.

# Ninja Bonuses:

# Add logic in the enroll method to check if they are a member already, and if they are, print "User already a member." and return False, otherwise return True.
# Add logic in the spend points method to be sure they have enough points to spend that amount and handle appropriately.

# challenges

# Create a file with the User class, including the __init__ with all the attributes, parameters and default values.

# Add the display_info(self) method to the User class

# In the outer scope, create a user instance and call the display_info method to test.

# Add the enroll method to the User class, implement and test by calling the method on the user in the outer scope.

# Make 2 more instances of the User class.

# Implement the spend_points(self, amount) method

# Have the first user spend 50 points

# Have the second user enroll.

# Have the second user spend 80 points

# Call the display method on all the users.

# BONUS: Implement the logic for testing if already a member and try to re-enroll the first user.

# BONUS: Implement the logic to prevent over-spending and call the spend_points method with 40 points on the 3rd user.