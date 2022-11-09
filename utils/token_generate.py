import string
import random


def token_generator(size=20, chars=string.ascii_lowercase + string.digits + string.ascii_uppercase):
    return ''.join(random.choice(chars) for _ in range(size))
