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

def verify_users(username,password):
    """
    Function that verifies incoming new users
    """
    User.verify_user(username,password)

def login_new_user(username,password):
    """
    Function that check if a user exits and logs them in
    """
    login_user=User.verify_user(username,password)
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
    return Credentials.display_credentials()

def find_credentials(username):
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

    elif short_code=="si":
        print("-"*30)
        print("Enter your username and password to sign in")
        print("-"*30)
        username=input("user_name: ")
        password=input("password: ")
        # sign_in =login_new_user(username,password)
        # if login_new_user == sign_in:
        print(f"hello {username} your log in was successful, welcome\n")
    
    while True:
        print("NC- new credential\n DC- display credentials\n SC-search credentials\n  ")
        short_code=input().lower().strip()
        if short_code=="nc":
           print("create new credentials")
           print("-"*30)
           print("Enter account name...")
           account=input().lower().strip()
           print ("Enter your username...")
           username=input()
           while True:
               print("TP -type password\n GP-generate password\n")
               password_selected=input().lower().strip()
               if password_selected=="tp":
                   password=input("Enter your password\n")
                   break

               elif password_selected=="gp":
                   password=gen_random_password()
                   break

               else:
                    print("invalid password")

           save_new_credentials(generate_new_credentials(account,username,password))
           print("\n")
           print("Your credentials have been successfully saved\n")

        elif short_code=="dc": 
            if display_new_credentials():
                print("This are your credentials")

                for username in display_new_credentials():
                    print(f"account: {username.account} \n username: {username.username} \n password: {password} \n saved successfully\n")
            
            else:
                print("You dont have any saved credentials")

        elif short_code=="sc":
           print("Enter the username of the account you want to search for...")
           find_name=input().lower().strip()
           if find_credentials(username):
               search_details=find_credentials(username)
               print("-"*30)
               print(f"Account: {search_details.account}\n userName: {search_details.username}\n password: {search_details.password}\n")

           else:
               print("The credential does not exist")
    
                  





    







if __name__ == '__main__':

    main()
