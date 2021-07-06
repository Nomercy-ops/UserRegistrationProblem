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
        name = validate.ValidateName("Rikesh")
        self.assertTrue(name)

    def test_givenName_withMinimumThreeLetters_shouldReturnTrue(self):
        
        """
    Description:
        The given valid name with minimum 3 character
        should return true in test case
    
    Parameter:
        It takes self as a parameter.
       
    """
        name = validate.ValidateName("Rik")
        self.assertTrue(name)

    def test_givenName_withLessThanThreeLetters_shouldReturnFalse(self):
        
        """
    Description:
        The given invalid name with less than three character
        should return false in test case
    
    Parameter:
        It takes self as a parameter.
       
    """
        name = validate.ValidateName("Ri")
        self.assertFalse(name)

    def test_givenInvalidName_WithSmallLetter_shouldReturnfalse(self):
        
        """
    Description:
        The given invalid name with all small letter
        should return false in test case
    
    Parameter:
        It takes self as a parameter.
       
    """
        name = validate.ValidateName("rikesh")
        self.assertFalse(name)

    def test_givenName_withAllUpperCaseCharacter_shouldReturnFalse(self):
        
        """
    Description:
        The given invalid name with all Capital letter
        should return false in test case
    
    Parameter:
        It takes self as a parameter.
       
    """
        name = validate.ValidateName("RIKESH")
        self.assertFalse(name)

    def test_givenName_whenContainNumber_shouldReturnFalse(self):
        
        """
    Description:
        The given invalid name with numbers
        should return false in test case
    
    Parameter:
        It takes self as a parameter.
       
    """
        name = validate.ValidateName("Ri786es")
        self.assertFalse(name)

    def test_givenName_whenContainSpecialCharacter_shouldReturnFalse(self):
        
        """
    Description:
        The given invalid name with special characters
        should return false in test case
    
    Parameter:
        It takes self as a parameter.
       
    """
        name = validate.ValidateName("Ri@kesh")
        self.assertFalse(name)


            
    #   " Test Case For Email "



