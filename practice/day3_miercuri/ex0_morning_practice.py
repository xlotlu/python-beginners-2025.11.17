# bună dimineața!

# Dată fiind o structură de date de forma:
people = [
    ("Jane", 20, ["reading", "hiking", "biking"]),
    ("Mike", 17, ["hiking", "fishing"]),
    ("Anna", 25, []),
    ("Sam", 40, ["playing guitar"]),
    ("Dan", 34, ["painting", "reading"]),
]

#1. creați o listă nouă, formată din liste,
#   unde listele de pe nivelul 2 sunt formate din 
#   [nume, hobbies]

"""
ppl2 = [
    ["Jane", ["reading", "hiking", "biking"]],
    ["Mike", ...],
    ...
]
"""

ppl2 = []
for person in people:
    name = person[0]
    hobbies = person[2]

    p = [name, hobbies]

    ppl2.append(p)
print(ppl2)


ppl2 = []
for person in people:
    # don't do this, it's ugly and you can't read it
    ppl2.append([person[0], person[2]])
print(ppl2)

#2. scrieți o funcție
def find_by_name(lst, name):
    pass
# ce primind ca argument lista `people` de mai sus
# returnează tupla din aceasta care are pe prima poziție
# valoarea `name`

find_by_name(people, "Sam") # --> ("Sam", 40, ["playing guitar"])

"""
def find_by_name(lst, name):
    out = []
    for elem in lst:
        if elem[0] == name:
            out = elem
            break
    return out
"""

def find_by_name(lst, name):
    for elem in lst:
        if elem[0] == name:
            return elem


#3. adăugați lui Jane și Sam hobby-ul "cooking".
#   pentru a îi găsi, folosiți funcția `find_by_name()` de mai sus.

ppl_cooking = ["Jane", "Sam", "Dan", "Andrew"]

for name in ppl_cooking:
    person = find_by_name(people, name)
    if person:
        person[2].append("knitting")

# după ce ați modificat pe Jane și Sam, inspectați lista `people`.
# ce observați?

#4. ștergeți "reading" dintre hobby-urile lui Jane,
#   (prefăcându-vă că nu știți indexul la care se află)

jane = find_by_name(people, "Jane")
try:
    jane[2].remove("reading")
except ValueError:
    #print("nu are reading")
    pass


#5. ștergeți primul hobby al lui Dan, păstrându-l în același timp într-o variabilă.
dan_hobby = find_by_name(people, "Dan")[2].pop(0)


#6. știind că există funcția `filter(func, iterable)`, ce returnează un iterabil nou,
#   al cărui fiecare element a fost filtrat prin funcția `func(elem)`, 
#   găsiți toți prietenii cu hobby-ul "hiking".
#
#   "a filtra" în contextul `func` înseamnă că returnează True sau False.


def has_hiking(elem):
    return "hiking" in elem[2]

my_hiking_friends = list(filter(has_hiking, people))

# Alternate solution:
# generic implementation
def find_by_hobby(hobby, lst):
    # `hobby` is available at this level

    def has_hobby(elem):
        # `hobby` is also available at this level
        return hobby in elem[2]

    my_hobby_friends = list(filter(has_hobby, lst))

    return my_hobby_friends

# re-implementare cu lambda:
def find_by_hobby(hobby, lst):
    return list(
        filter(
            lambda elem: hobby in elem[2],
            lst
        )
    )

# Exercițiu:
# revizităm exercițiul din ziua 1:
# cerem vărsta utilizatorului și aplicăm funcția următoare:

def is_of_proper_age(num):
    if num < 18:
        print("you are too young")
    elif num > 60:
        print("sorry, too old")
    else:
        print("you are hired")

age = input("Varsta ta?: ")
# între aceste 2 linii, verificați că inputul a fost numeric;
# dacă nu a fost numeric, dați un mesaj de eroare,
# și cereți în mod repetat vârsta
is_of_proper_age(age)


# 1. cerem vârsta
# 2. verificăm
# 3. cât timp _nu este_ numeric, din nou input


# sau:
# putem inițializa vârsta cu ceva non-numeric
# și intrăm direct în ciclu


# două pattern-uri de while:
####
# A) încep deja cu o valoare:
####
age = input("Varsta ta?: ")
# DRY = "don't repeat yourself"

while not age.isdigit(): # buclă numai pe timp de eroare
    print("zi un număr")
    age = input("Varsta ta?: ")

is_of_proper_age(int(age))

####
# B) loop infinit, fac break ! explicit !
####

while True:
    age = input("Varsta ta?: ")
    if age.isdigit(): # escape din buclă pe caz valid
        break
    else:
        print("eroare!")

is_of_proper_age(int(age))


###
# B.2) același lucru, dar try/except în loc de if
###
while True:
    age = input("Varsta ta?: ")

    try:
        age = int(age)
    except ValueError:
        print("eroare!")
    else:
        break

is_of_proper_age(int(age))


