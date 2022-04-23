import unittest
from lock import User

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


if __name__ == '__main__':
    unittest.main()