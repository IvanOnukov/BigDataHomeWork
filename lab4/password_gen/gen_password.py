import random
import string
import re


def validation_password(password: str):
    atLeastLetterLow = re.search(r'[a-z]', password) is not None
    atLeastLetterUp = re.search(r'[A-Z]', password) is not None
    atLeastNumber = re.search(r'[0-9]', password) is not None
    atLeastOther = re.search(r'\W', password) is not None

    if len(password) > 12 and atLeastLetterLow and atLeastLetterUp and atLeastNumber and atLeastOther:
        # the password is strong
        return True
    else:
        return False


def random_password(length):
    letters = string.ascii_letters + string.digits + string.ascii_uppercase + '!@#$%^&*()-+'
    return ''.join(random.choice(letters) for i in range(length))


if __name__ == '__main__':

    passwordLen = random.randint(12, 128)
    password = random_password(passwordLen)
    while not validation_password(password):
        passwordLen = random.randint(12, 64)
    print(password)
