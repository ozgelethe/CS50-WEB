people = [
    {"name": "rukiye", "house":"denizli"},
    {"name": "mina", "house": "istanbul"},
    {"name": "yaren", "house": "edirne"}
]

# isimlere göre alfabedik sıralama:
    
# def f(person):
#     return person["name"]

# people.sort(key=f)

people.sort(key=lambda person:person["name"])

print(people)