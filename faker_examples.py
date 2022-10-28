"""
name: faker_examples.py
description: Examples of using the faker module.
author: hdaojin
version: 1.0.0
creation date: 2022-10-28
last modified: 2022-10-28
usage: python3 faker_examples.py
"""

"""
faker has a cli tool, you can use it to generate fake data. eg: faker -r 3 name
"""

from faker import Faker
import click


fake = Faker('zh_CN')
person_data = []

def generate_person_data(counts):
    """Generate fake person data."""
    for _ in range(counts):
        data = {}
        data['name'] = fake.name()
        data['address'] = fake.address()
        data['phone_number'] = fake.phone_number()
        person_data.append(data)
    return person_data

if __name__ == "__main__":
    generate_person_data(10)
    print(person_data)
