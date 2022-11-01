"""
name: faker_to_csv.py
description: Generate fake data and save to csv file.
author: hdaojin
version: 1.0.0
creation date: 2022-11-01
last modified: 2022-11-01
"""

import csv
from faker import Faker

fake = Faker('zh_CN')

def generate_fake_data(counts):
    """Generate fake data."""
    fake_data = []
    for _ in range(counts):
        preson_data = (fake.user_name(), 
                       fake.password(length=8, special_chars=False, upper_case=False), 
                       fake.phone_number())
        fake_data.append(preson_data)
    return fake_data

def save_to_csv(data):
    headers = ['username', 'password', 'phone_number']
    with open('users.csv', 'w', newline='') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(headers)
        csv_writer.writerows(data)

def read_csv():
    with open('users.csv', 'r', newline='') as f:
        csv_reader = csv.reader(f)
        for row in csv_reader:
            print(row)

def main():
    data = generate_fake_data(100)
    save_to_csv(data)
    read_csv()
   

if __name__ == "__main__":
    main()
