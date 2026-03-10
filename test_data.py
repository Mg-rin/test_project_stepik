from faker import Faker

fake = Faker('ru_RU')

def generate_email():
    """Генерирует случайный email"""
    return fake.email()

def generate_password(length=8):
    """Генерирует случайный пароль заданной длины"""
    return fake.password(length=length)

def generate_credentials():
    return fake.email(), fake.password()