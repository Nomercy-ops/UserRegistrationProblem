"""
@Author: Rikesh Chhetri
@Date: 2021-07-01
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-01 10:03:30
@Title : Test case for user registration problem using pytest
"""

from UserValidation import ValidateUser as validate
from InputSample import Sample as sample
import pytest

#   " Test Case For First Name And LastName "

@pytest.mark.name
@pytest.mark.parametrize("name_input,expected",sample.valid_name)
def test_validName(name_input,expected):
    """
Description:
    The given valid name should return true in test case

Parameter:
    It takes name_input and expected as a parameter.

"""
    assert validate.ValidateName(name_input) == expected


@pytest.mark.name
@pytest.mark.parametrize("invalid_name,expected",sample.invalid_name)

def test_invalidName(invalid_name,expected):
    """
Description:
    The given invalid name should return false in test case

Parameter:
    It takes invalid_name and expected as a parameter..

"""
    assert validate.ValidateName(invalid_name) == expected
   

 #   " Test Case For Email "

@pytest.mark.email
@pytest.mark.parametrize("valid_email,expected",sample.valid_emails)

def test_validEmail(valid_email,expected):
    """
Description:
    The given valid email should return true in test case

Parameter:
    It takes valid_email and expected as a parameter.

"""

    assert validate.ValidateEmail(valid_email) == expected


@pytest.mark.email
@pytest.mark.parametrize("invalid_email_input,expected",sample.invalid_emails)

def test_invalidEmail(invalid_email_input,expected):
    """
Description:
    The given invalid Email should return false in test case

Parameter:
    It takes invalid_email_input and expected as parameter.

"""
    assert validate.ValidateEmail(invalid_email_input) == expected

    #  " Test Case For Phone Number "

@pytest.mark.phonenumber
@pytest.mark.parametrize("phone_number_input,expected", sample.valid_phoneNumber)
def test_validPhoneNumber(phone_number_input,expected):
    """
Description:
    The given valid Phone number should return true in test case

Parameter:
    It takes phone_number_ input and expected as a parameter.

"""
    assert validate.ValidatePhoneNumber(phone_number_input) == expected


@pytest.mark.phonenumber
@pytest.mark.parametrize("invalid_phoneNumber,expected",sample.invalid_phoneNumber)
def test_invalidPhoneNumber(invalid_phoneNumber,expected):
    """
Description:
    The given invalid phone number should return false in test case

Parameter:
    It takes invalid_phone number and expected as a parameter

"""
    assert validate.ValidatePhoneNumber(invalid_phoneNumber) == expected
   

#   " Test Case For Password:  "

@pytest.mark.password
@pytest.mark.parametrize("password_input,expected",sample.valid_password)

def test_validPassword(password_input,expected):
    """
Description:
    The given valid Password should return true in test case

Parameter:
     It takes valid_password and expected as a parameter

"""
    assert validate.ValidatePassword(password_input) == expected
    

@pytest.mark.password
@pytest.mark.parametrize("invalid_password_input , expected",sample.invalid_password)

def test_invalidPassword(invalid_password_input,expected):
    """
Description:
    The given invalid Password should return false in test case

Parameter:
    It takes invalid_password and expected as a parameter

"""

    assert validate.ValidatePassword(invalid_password_input) == expected
   
