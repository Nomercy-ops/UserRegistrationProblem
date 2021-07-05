"""
@Author: Rikesh Chhetri
@Date: 2021-07-05 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-05 07:03:30
@Title : Program Aim is to validate user entered details using regular expression.
"""

from UserValidation import ValidateUser
from LogHandler import logger

def getUserInput():
    """
    Description:
        This method is used for getting user input frm the user.
        It calls the validate name method of validate user class for validation of name.
       
    """
    try:
        firstName = input("Enter your FirstName: ")
        logger.info("Entered first name {}".format(ValidateUser.ValidateName(firstName)))
    
    except Exception as e:
        logger.error(e)
    

if __name__ == "__main__":
    getUserInput()