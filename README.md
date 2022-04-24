# PASSWORD LOCKER

Password locker is a python application that runs on terminal which allows users to manage their credentials for different accounts.
### Author
* Pauline Wafula
### version
* 24/04/2022

### Description
This is a web application that uses flask , a framework in python, to generate a password locker that enables a user to manage their own accounts.This include creating an account, saving the account,displaying,creating multiple accounts and also deleting accounts that are are nolonger needed.A user has an option of typing their own password or the system to generate a password for them.The system has a pyper clip that can copy and paste the password.

### setup
* #### Cloning
Navigate into your project's folder 
In your terminal, run the commands
  > $ git clone https://github.com/paulinenanzala19/password_locker.git
  > 
  > $ cd passwordlocker

* #### Running the application
 chmod +x run.py
 ./run.py

### Technologies used
Python
This application is developed using [python3.8]
### BDD
| Behaviour    | input     | output     |
| -------------| :--------:| -----------|
| Displays short codes for navigating |**Enter:** ca   | Create an account by entering your username and password |
|Prompts user to login after creating an account/have an existing account|**Enter:**si username and password|Login successful|
|Displays short codes for credentials navigation|**Enter:** nc|Please enter an account, username and password and saves the credentials |
|Displays short codes for navigaing through the application|**Enter:** dc|Prompts user to display saved credentials|
|Displays short codes for navigaing through the application|**Enter:** sc|Prompts user to search existing credentials|
|Displays short codes for credentials navigation|**Enter:** dd/gp/ex/|Prompts users to delete credentials of choice/generate random password for the user/exiting|

### Known Bugs
No known bugs
### License
This project is Licensed under MIT.
©2022 Copyright.
### Collaborate
>To Collaborate, Reach me out at:
>>Github: [paulinenanzala19](https://github.com/paulinenanzala19/password_locker)
>>Email: paulinenanzala19@gmail.com
