"""
@Author: Rikesh Chhetri
@Date: 2021-07-05 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-05 07:03:30
@Title : Program Aim is to validate user entered details using regular expression.
"""
import re
from RegexPattern import RegexPattern as regex_pattern
from LogHandler import logger

class ValidateUser:
    
    def ValidateName(input):
        """
    Description:
        This method is used for validating name with regex pattern.

    Return:
        It return a valid true if name is valid and false if it's invalid.
    
    Parameter:
        It takes input as a parameter.
       
    """
        try:
            if (re.match(re.compile(regex_pattern.NAME_PATTERN),input)):
                return True
            else:
                return False
        
        except Exception as e:
            logger.error(e)
        
    
    def ValidateEmail(emailInput):
        """
    Description:
        This method is used for validating email with regex pattern.

    Return:
        It return a valid  if email is valid and invalid if it's invalid.
    
    Parameter:
        It takes input as a parameter.
       
    """
        try:
            if (re.match(re.compile(regex_pattern.EMAIL_PATTERN),emailInput)):
                return True
            else:
                return False
        
        except Exception as e:
            logger.error(e)

    
    def ValidatePhoneNumber(phoneInput):
        """
    Description:
        This method is used for validating phone number with regex pattern.

    Return:
        It return a valid  if phone number is valid and invalid if it's invalid.
    
    Parameter:
        It takes input as a parameter.
       
    """
        try:
            if (re.match(re.compile(regex_pattern.PHONE_PATTERN),phoneInput)):
                return True
            else:
                return False
        
        except Exception as e:
            logger.error(e)

    
    def ValidatePassword(passwordInput):
        """
    Description:
        This method is used for validating password with regex pattern.

    Return:
        It return a valid  if password is valid and invalid if it's invalid.
    
    Parameter:
        It takes input as a parameter.
       
    """
        try:
            if (re.match(re.compile(regex_pattern.PASSWORD_PATTERN),passwordInput)):
                return True
            else:
                return False
        
        except Exception as e:
            logger.error(e)
