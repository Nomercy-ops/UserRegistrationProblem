
class RegexPattern:
    NAME_PATTERN = "^[A-Z]{1}[a-z]{2,}"
    EMAIL_PATTERN = "^([a-z]{2,}[0-9a-z]{1,}([_+-.*$#]{0,1}[a-z0-9]{1,}){0,1}[@]{1}[a-z0-1]{1,}[.]{1}[a-z]{2,4}([.]{0,1}[a-z]{2,3}){0,1})$"
    PHONE_PATTERN = "^[\+][9?][1?][\-\s]?[6-9]{1}[\d]{9}$"
    PASSWORD_PATTERN = "^(?=.*[@#$%^&+=])(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$"
