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
