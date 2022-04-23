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







    

