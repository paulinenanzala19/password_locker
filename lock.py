import random
import string

class User:
    """
    Creating a class that generates new instances of a user

    """
    user_list=[]

    def __init__(self,username,password):

      """
      method that defines properties of a user
      """
      self.username=username
      self.password=password

    def save_user(self):
      """
      method that saves a new user into the user list
      """  
      User.user_list.append(self)


    

