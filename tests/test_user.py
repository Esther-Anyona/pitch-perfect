import unittest
from app.models import User

class UserModelTest(unittest.TestCase):

    def setUp(self):
        self.new_user = User(password = 'pitches')

    # confirm that password input has a value
    def test_password_setter(self):
        self.assertTrue(self.new_user.password is not None)

    # confirm that app raises an attribute error when trying to access password property
    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.password

    # test to confirm that password hash can be verified if correct password is passed
    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('pitches'))