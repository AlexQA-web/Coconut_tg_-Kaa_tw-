import random
import string
from faker import Faker
from PART_4.Cinescope.constants import EMAIL_PROV

faker = Faker()

class DataGenerator:

    @staticmethod
    def get_random_email():
        random_email_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        return f'lol{random_email_string}{EMAIL_PROV}'

    @staticmethod
    def get_random_name():
        return f'{faker.first_name()} {faker.last_name()}'

    @staticmethod
    def get_random_password():
        upper_letter = random.choice(string.ascii_uppercase)
        digit = random.choice(string.digits)
        special_symbols = """~!?@#$%^&*_-+(){}></\|".,:'"""

        password_length = random.randint(6, 30)
        all_chars = string.ascii_lowercase + string.digits + special_symbols
        random_string = ''.join(random.choices(all_chars, k=password_length))
        password = list(upper_letter + digit + random_string)
        random.shuffle(password)
        return ''.join(password)


