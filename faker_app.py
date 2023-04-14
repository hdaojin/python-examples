"""
Name: faker_app.py
Description: 这个脚本用于生成随机用户信息，用于测试
Author: hdaojin
Version: 1.0.0
Creation date: 2023.04.14
Last modified: 2023.04.14
Usage: python3 faker_app.py
Requirements: Faker
documentation: https://faker.readthedocs.io/en/master/
"""

# pip install Faker

import csv
import random
from faker import Faker

fake = Faker()  # 使用英文环境
# 使用中文环境
# fake = Faker('zh_CN')

# 部门及人数
departments = {
    "Management": 5,
    "Sales": 15,
    "Technical": 10
}

# 生成用户信息
def generate_user_info(department):
    first_name = fake.first_name()
    last_name = fake.last_name()
    name = f"{first_name} {last_name}"
    user_name = f"{first_name.lower()}-{last_name.lower()}"
    email_name = f"{first_name.lower()}.{last_name.lower()}"
    email = f"{email_name}@appsrv.com"
    return [name, department, user_name, email]

# 保存用户信息到CSV文件
def save_users_to_csv(users, filename='users.csv'):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['ID', 'Name', 'Department', 'Username', 'Email'])
        # 生成用户ID, enumerate()函数用于生成序号
        for index, user in enumerate(users, start=1):
            csv_writer.writerow([index] + user)

if __name__ == '__main__':
    users = []
    for department, count in departments.items():
        for _ in range(count):
            users.append(generate_user_info(department))
    random.shuffle(users)  # 打乱用户顺序
    save_users_to_csv(users)