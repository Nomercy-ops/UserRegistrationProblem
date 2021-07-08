class Sample:
    # input for invalid Name
  valid_name = [("Rikesh",True),("Rik",True)]

    # input for invalid Name
  invalid_name = [("Ri", False),
                      ("rikesh", False),
                      ("RIKESH", False),
                      ("Ri786es", False),
                      ("Ri@kesh", False)]

    # inputs for valid emails
  valid_emails = [("abc10@yahoo.com", True),
                      ("abc-100@yahoo.com", True),
                      ("abc.100@yahoo.com", True),
                      ("abc111@abc.com", True),
                      ("abc-100@abc.net", True),
                      ("abc.100@abc.com.au", True)]

    # inputs for invalids emails
  invalid_emails = [("rikesh@.com", False),
                      ("rikesh@gmail", False),
                      ("abc..28@gmail.com", False),
                      ("abc123@gmail.c", False),
                      ("abc@abc@gmail.com", False),
                      (".abc@abc@gmail.com", False)]
  
    # input for valid phone numbers
  valid_phoneNumber = [("+91-7865434321",True),("+91 6865434321",True)]

    # inputs for invalids phone numbers
  invalid_phoneNumber = [("+91-786543", False),
                      ("+91-78654346578", False),
                      ("7865438768", False),
                      ("+91  8765654324", False),
                      ("+91-876565r324", False),
                      ("+91-87656@r324", False)]

   # input for valid password
  valid_password = [("Mercy@123",True),("mercy@Yoo76#",True)]

    # inputs for invalid password
  invalid_password = [("Silv@12", False),
                       ("rikes76#", False),
                      ("Riki45eh" , False),
                      ("rikeSH#W", False),
                      ("rikes76R" , False)]
