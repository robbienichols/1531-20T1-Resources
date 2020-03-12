def check_password(password):
    '''
    Takes in a password, and returns a string based on the strength of that password.

    The returned value should be:
    * "Strong password", if at least 12 characters, contains at least one number, at least one uppercase letter, at least one lowercase letter.
    * "Moderate password", if at least 8 characters, contains at least one number.
    * "Poor password", for anything else
    * "Horrible password", if the user enters "password", "iloveyou", or "123456"
    '''
    
    if password == 'password' or password == 'iloveyou' or password == '123456':
        return 'Horrible password'

    numCheck = any(character.isdigit() for character in password)
    upperCheck = any(character.isupper() for character in password)
    lowerCheck = any(character.islower() for character in password)

    if len(password) >= 12 and numCheck and upperCheck and lowerCheck:
        return 'Strong password'
    if len(password) >= 8 and numCheck:
        return 'Moderate password'
    return 'Poor password'
