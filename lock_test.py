import unittest
from lock import User
from lock import Credentials

class TestClass(unittest.TestCase):
    """
    Test class that defines test cases of the class user behaviours

    """

    def setUp(self):

       """
       method to run before individual test cases

       """
       self.new_user= User("paulinenanzala19","Syt45nfh")
    # """
    # create user object
    # """

    def test_init(self):
       """
       test case to test if the object has been initialized properly
       """

       self.assertEqual(self.new_user.username,"paulinenanzala19")
       self.assertEqual(self.new_user.password, "Syt45nfh")

    def test_save_user(self):
       """
       test case to test if the user object is saved into the user list
       """ 
       self.new_user.save_user()
       self.assertEqual(len(User.user_list),1)

class TestCredentials(unittest.TestCase):
    """
    Test class that defines test cases of the class credentials behaviour
    """
    def setUp(self):
       """
       method that runs before each individual credentials test
       """
       self.new_credential=Credentials("twitter","pauline_nanzala19","Fjkf899th")
    
    def test_init(self):
        """
        test case to test if the credentials object has been initialised properly
        """
        self.assertEqual(self.new_credential.account,"twitter")
        self.assertEqual(self.new_credential.username,"pauline_nanzala19")
        self.assertEqual(self.new_credential.password,"Fjkf899th")

    def test_save_credentials(self):
        """
        test case to test if the credentials are saved in the credential list
        """
        self.new_credential.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)

    def tearDown(self):
        """
        this is a method that cleans up after each test case has run
        """
        Credentials.credentials_list=[]

    def test_save_multiple_credentials(self):
        """
        test case to test if we can save multiple credential object to our credential list
        """
        self.new_credential.save_credentials()
        test_credential= Credentials("instagram","paulananzala","Hybj76t6")
        test_credential.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)

    def test_delete_credentials(self):
        """
        test case to test if we can remove credential from credential list
        """
        self.new_credential.save_credentials()
        test_credential=Credentials("instagram","paulananzala","Hybj76t6")
        test_credential.save_credentials()

        self.new_credential.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)
        

    def test_search_credential(self):
        """
        test to find credential details using the username
        """
        self.new_credential.save_credentials()
        test_credential=Credentials("instagram","paulananzala","Hybj76t6")
        test_credential.save_credentials()

        test_credential.search_credential("paulananzala")
        self.assertEqual(test_credential.username,test_credential.username)


    



if __name__ == '__main__':
    unittest.main()