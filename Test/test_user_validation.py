"""
@Author: Rikesh Chhetri
@Date: 2021-07-01 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-01 10:03:30
@Title : Test case for user registration problem.
"""

from UserValidation import ValidateUser as validate
import unittest


class TestUserValidation(unittest.TestCase):

    #   " Test Case For First Name And LastName "

    def test_givenValidName_shouldReturnTrue(self):
        """
    Description:
        The given valid name should return true in test case

    Parameter:
        It takes self as a parameter.

    """

        self.assertTrue(validate.ValidateName("Rikesh"))
        self.assertTrue(validate.ValidateName("Rik"))

    def test_givenInvalidName_shouldReturnFalse(self):
        """
    Description:
        The given invalid name should return false in test case

    Parameter:
        It takes self as a parameter.

    """
        self.assertFalse(validate.ValidateName("Ri"))
        self.assertFalse(validate.ValidateName("rikesh"))
        self.assertFalse(validate.ValidateName("RIKESH"))
        self.assertFalse(validate.ValidateName("Ri786es"))
        self.assertFalse(validate.ValidateName("Ri@kesh"))

     #   " Test Case For Email "

    def test_givenValidEmail_shouldReturnTrue(self):
        """
    Description:
        The given valid email should return true in test case

    Parameter:
        It takes self as a parameter.

    """

        self.assertTrue(validate.ValidateEmail("abc10@yahoo.com"))
        self.assertTrue(validate.ValidateEmail("abc-100@yahoo.com"))
        self.assertTrue(validate.ValidateEmail("abc.100@yahoo.com"))
        self.assertTrue(validate.ValidateEmail("abc111@abc.com"))
        self.assertTrue(validate.ValidateEmail("abc-100@abc.net"))
        self.assertTrue(validate.ValidateEmail("abc.100@abc.com.au"))
        self.assertTrue(validate.ValidateEmail("abc@1.com"))
        self.assertTrue(validate.ValidateEmail("abc@gmail.com.com"))

    def test_givenInvalidEmail_shouldReturnFalse(self):
        """
    Description:
        The given invalid Email should return false in test case

    Parameter:
        It takes self as a parameter.

    """
        self.assertFalse(validate.ValidateEmail("rikesh@.com"))
        self.assertFalse(validate.ValidateEmail("rikesh@gmail"))
        self.assertFalse(validate.ValidateEmail("abc..28@gmail.com"))
        self.assertFalse(validate.ValidateEmail("abc123@gmail.c"))
        self.assertFalse(validate.ValidateEmail("abc@abc@gmail.com"))
        self.assertFalse(validate.ValidateEmail(".abc@abc@gmail.com"))

    
    #   " Test Case For Phone Number "

    def test_givenValidPhoneNumber_shouldReturnTrue(self):
        """
    Description:
        The given valid Phone number should return true in test case

    Parameter:
        It takes self as a parameter.

    """
        self.assertTrue(validate.ValidatePhoneNumber("+91-7865434321"))
        self.assertTrue(validate.ValidatePhoneNumber("+91 6865434321"))

    
    def test_givenInvalidPhoneNumber_shouldReturnFalse(self):
        """
    Description:
        The given invalid phone number should return true in test case

    Parameter:
        It takes self as a parameter.

    """
        self.assertFalse(validate.ValidatePhoneNumber("+91-786543"))
        self.assertFalse(validate.ValidatePhoneNumber("+91-78654346578"))
        self.assertFalse(validate.ValidatePhoneNumber("+91 5765654324"))
        self.assertFalse(validate.ValidatePhoneNumber("7865438768"))
        self.assertFalse(validate.ValidatePhoneNumber("+91  8765654324"))
        self.assertFalse(validate.ValidatePhoneNumber("+91-876565r324"))
        self.assertFalse(validate.ValidatePhoneNumber("+91-87656@r324"))
        
