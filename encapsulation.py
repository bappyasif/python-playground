# in oop encapsulation is a fundamental concept that describes wrapping variables and methods in a single unit

# encapsulation is a mechanism of hiding internal details and showing only essential information to the outside world

# class variables
# a class contain variables that can only be accessed by an object of class.

class UserInfo:
    def __init__(self, username, email_address):
        self.username = username
        self.email_address = email_address
    
user = UserInfo("bappy", "bappy@com")
print(user.username)
print(user.email_address)

# class methods
# a class can  also contain methods that can be accessed by object of that class its been instantiated from.

class UserInfo2:
    def __init__(self, username, email_address):
        self.username = username
        self.email_address = email_address

    def check_username(self, username_to_check):
        if self.username == username_to_check:
            print("valid username")            
        else:
            print("invalid username")

user = UserInfo2("bappy", "bappy@com")
user.check_username("bapp2y")

class UserInfo3:
   def __init__(self, username, email_address):
      self.username = username
      self.email_address = email_address

   def check_username(self, username_to_check):
       if username_to_check == self.username:
           return True
       else:
           return False

user3 = UserInfo3('user123', 'abc@edf.ghi')

print(user3.check_username('user123')) # returns True
print(user3.check_username('user456')) # returns False