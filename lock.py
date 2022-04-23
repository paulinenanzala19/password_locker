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

    @classmethod
    def verify_user(cls,username,password):
        """
        method to verify whether the user is in our contact list or not
        """
        the_user=""
        for user in user_list:
            if(user.username=username and user.password=password):
                the_user== user.username
        return the_user

    def delete_user(self):
        """
        method that removes a user from the user list
        """
        User.user_list.remove(self)



class Credentials:
    """
    creating a class that generates new instances of credentials
    """

    credentials_list=[]

    def __init__(self,account,username,password):
        """
        method that defines properties of credentials
        
        """
        self.account=account
        self.username=username
        self.password=password

    def save_credentials(self):
        """
        method that saves new credentials into the credential list
        """
        Credentials.credentials_list.append(self)

    def save_multiple_credentials(self):
        """
        method that can save multiple credentials into the credential list
        """
        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        """
        method that deletes a saved credential from credential list
        """
        Credentials.credentials_list.remove(self)

    @classmethod
    def search_credential(cls,username):
        """
        method tht takes in the user name and returns credentials that matches the username
        """

        for credential in cls.credentials_list:
            if credential.username == username:
                 return credential

    @classmethod
    def credential_exist(cls,username):
        """
        method that checks if credentials exist in the credential list
        """

        for credential in cls.credentials_list:
           if credential.username ==username:
                 return True

        return False

    @classmethod
    def display_credentials(cls):
        """
        method that returns all items in the credential list
        """
        return cls.credentials_list







    

