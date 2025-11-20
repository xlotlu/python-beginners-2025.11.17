d = {
    "k1": "value",
    "k2": "value 2",
}

# acces după cheie:
d["k1"]

mykey = "k2"
d[mykey]

try:
    d["bau"]
except KeyError:
    print("there is no bau")

# Exercițiu:
# 1. vă rog să creați un dicționar
# cu cheile respectiv valorile:

# name: Jane
# age:  42
# city: Brashov

d = {
    "name": "Jane",
    "age": 42,
    "city": "Brașov"
}

# și asignați-l variabilei `d`

# 2. accesați și printați valoarea
#    asignată cheii "city" a lui `d`
print(d["city"])

# 3. asignați valoarea 43 pentru
#    cheia "age"
d["age"] = 43
d["age"] += 1
d["city"] += " de din Deal"

# 4. adăugăm o cheie nouă:
#    "hobbies": ["biking", "hiking", "knitting", "cooking"]
d['hobbies'] = ["biking", "hiking", "knitting", "cooking"]

# 5. adăugăți-i hobby-ul "reading"
#    (nu facem re-assignment!)
d['hobbies'].append("reading")

# 6. ștergem cheia 'city'
del d["city"]

# 7. hai să iterăm:
# de ținut minte: .keys(), .values(), .items()

for elem in d.items():
    print(elem)

for key, value in d.items():
    print(key, "::", value)

# 8. ștergeți cheia 'age', în timp ce o asignați
#    unei variabile `age`
age = d.pop("age")


d = {
   "Jane": 42,
   "George": 21,
   "Abdrew": 32,
   "Mary": 28,
}

for name, age in d.items():
    print(name, age)

# dar dacă știu că nu o să-l mai folosesc,
# aș putea să și golesc memoria în timp
# ce iterez prin el...

while d:
    name, age = d.popitem()
    print(name, age)



# Exercițiu
# dată fiind lista de tuple
people = [
    ("Jane", 20, ["reading", "hiking", "biking"]),
    ("Mike", 17, ["hiking", "fishing"]),
    ("Anna", 25, []),
    ("Sam", 40, ["playing guitar"]),
    ("Dan", 34, ["painting", "reading"]),
]

# creați o listă de dicționare de forma
[
    {
        "name": "Jane",
        "age": 20,
        "hobbies": ["reading", "hiking", "biking"]
    },
    {
        "name": "Jane"
    },
    ...
]

# pattern de acumulare
dictlist = []
# iterăm prin sursă:
for name, age, hobbies in people:
    d = {
        "name": name,
        "age": age,
        "hobbies": hobbies,
    }
    # acumulăm
    dictlist.append(d)
print(dictlist)

# Exercițiu:
# folosind lista de dicționare `dictlist`,
# construiți un dicționar nou `ages`,
# în care cheia este numele, și valoarea este vârsta.

"""
ages = {
    "Jane": 20,
    "Mike": 17,
    ...
}
"""

# pattern de acumulare
# instanțiem
ages = {}
# iterăm
for d in dictlist:
    name = d["name"]
    age = d["age"]
    # acumulăm
    ages[name] = age
print(ages)

