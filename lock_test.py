import unittest
from lock import user

class TestClass(unittest,TestCase):
    """
    Test class that defines test cases of the class user behaviours

    """

def setUp(self):
    """
    method to run before individual test cases

    """
    self.new_user= user("paulinenanzala19","Syt45nfh")
    """
    create user object
    """


