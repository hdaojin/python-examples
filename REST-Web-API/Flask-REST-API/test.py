import requests

r1 = requests.get('http://localhost:5000/countries')
print(r1.json())

r2 = requests.get('http://localhost:5000/countries/1')
print(r2.json())

r3 = requests.post('http://localhost:5000/countries', json={'name': 'China', 'capital': 'Beijing', 'area': 9596961})
print(requests.get('http://localhost:5000/countries').json())

