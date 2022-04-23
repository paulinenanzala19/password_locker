#!/usr/bin/env python3.8

from lock import User, Credentials

def create_user(username,password):
    """
    Function that creates a new user
    """
    new_user= User(username,password)
    return new_user

def save_users(user):
    """
    Function that saves the new users
    """
    user.save_user()

def verify_users():
    """
    Function that verifies incoming new users
    """
    user.verify_user()

def login_new_user():
    """
    Function that check if a user exits and logs them in
    """
    login_user=user.User.verify_user(username,password)
    return login_user

def generate_new_credentials(account,username,password):
    """
    Function that generates new credentials
    """
    new_credential=Credentials(account,username,password)
    return new_credential

def save_new_credentials(Credentials):
    """
    Function to save the new credentials
    """
    Credentials.save_credentials()

def display_new_credentials():
    """
    Function to display the new saved credentials
    """
    Credentials.display_credentials()

def find_credentials():
    """
    Function to display the if the account created matches with username and password
    """
    return Credentials.search_credential(username)

def check_exist_credentials():
    """
    Function to display existing credentials
    """
    return Credentials.credential_exist(username)

def delete_existing_credentials(Credentials):
    """
    Function to delete the credential
    """
    Credentials.delete_credentials()

def gen_random_password():
    """
    Function to generate a random password
    """
    default_password= Credentials.generate_password()
    return default_password

def copy_passwords(username):
    """
    Function that uses the pyperclip module to copy the password 
    """
    return Credentials.copy_password(username)


def main():
    print("Hello, welcome to password locker..\n To proceed, use the following short codes.\n CA ---create an account.\n SI ---sign in an existing account")
    short_code=input().lower().strip()
    if short_code =="ca":
      print("register")
      print("-"*30)
      username=input("user_name:")

      while True:
          print("TP- Type password.\n GP- Generate password")
          password_selected=input().lower().strip()
          if password_selected=="tp":
            password=input("Enter password.\n")
            break
            

          elif password_selected=="gp":
            password=gen_random_password()
            break

          else:
            print("Invalid password try again")


    save_users(create_user(username,password))
    print("-"*30)
    print(f"Hello {username}, your registration was successful! Your password is:{password} ")
    print("-"*40)

    







if __name__ == '__main__':

    main()
