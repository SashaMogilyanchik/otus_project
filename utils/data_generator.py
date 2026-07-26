from uuid import uuid4

from faker import Faker

fake = Faker()


def generate_user_data(email=None):
    first_name = fake.first_name()
    last_name = fake.last_name()
    password = fake.password(length=10, special_chars=False, digits=True, upper_case=True, lower_case=True)

    return {
        "name": f"{first_name} {last_name}",
        "email": email or f"test_{uuid4().hex[:12]}@example.com",
        "password": password,
        "title": "Mr",
        "birth_date": "10",
        "birth_month": "5",
        "birth_year": "1990",
        "firstname": first_name,
        "lastname": last_name,
        "company": fake.company(),
        "address1": fake.street_address(),
        "address2": fake.secondary_address(),
        "country": "United States",
        "zipcode": fake.zipcode(),
        "state": fake.state_abbr(),
        "city": fake.city(),
        "mobile_number": fake.numerify("##########"),
        "newsletter": "true",
    }
