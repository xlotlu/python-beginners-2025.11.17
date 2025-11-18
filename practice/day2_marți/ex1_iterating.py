# iterating

# for
# while

# Exercițiu:
# dată fiind tupla:
tup = ("București", "Brașov", "Constanța", "Iași")
# faceți print elementelor care încep cu litera "B"

for elem in tup:
    if elem.startswith("B"):
        print(elem)


# cum implementăm remove pentru o listă?

def remove(lst, elem):
    # verificăm dacă e în listă

    if elem not in lst:
        return # early exit

    # pe ce poziție
    # îi luăm indexul
    idx = lst.index(elem)

    # și îl ștergem
    del lst[idx]



def remove(lst, elem):
    # (încercăm să) îi luăm indexul
    try:
        idx = lst.index(elem)
    except ValueError:
        return

    # și îl ștergem
    del lst[idx]


# alternativ, lăsăm excepția,
# pentru că nu e responsabilitatea noastră
def remove(lst, elem):
    idx = lst.index(elem)
    del lst[idx]


# Exercițiu:
# creați o listă cu pătratul numerelor de la 
# 0 la 5, iterând prin range(6)

# [!!] pattern de acumulare:
# 1. declarăm obiectul final
squares = []
# 2. iterăm prin obiectul sursă
for num in range(6):
    # 3. ne pregătim valoarea curentă
    v = num * num
    # 4. acumulăm
    squares.append(v)
# x. gata.
print(squares)

# Exercițiu:
# creați o listă cu numerele subunitare
# de la 0.01 la 0.20

lst = []
for num in range(1, 21):
    lst.append(num / 100)
print (lst)

# Exercițiu:
# dată fiind lista `lst` de mai sus,
# creați o listă `formatted_lst`
# care conține valorile în mod string,
# formatate cu două decimale.

# "%.04f" % 5 # "string interpolation"
# "{:.04f}".format(5)

formatted_lst = []
for num in lst:
    formatted_lst.append("%.03f" % num)
print(formatted_lst)


# Exercițiu:
# creați o listă cu pătratul numerelor impare
# de la 0 la 20

# pattern de acumulare ajustat:

# 1. instanțiem
odd_squares = []
# 2. iterăm în sursă
for num in range(0, 20 + 1):
    # 3. filtrăm
    if num % 2 == 1:
        # 4. calculăm valoare
        v = num ** 2
        # 5. acumulăm
        odd_squares.append(v)
print(odd_squares)


odd_squares = []
for num in range(0, 20 + 1):
    # alternative filtration
    if not num % 2:
        continue
    odd_squares.append(num ** 2)
print(odd_squares)



# Exercițiu:
# dată fiind lista de tuple (city, distance)
cities = [
    ('Arad', 560),
    ('Brașov', 180),
    ('București', 0),
    ('Cluj', 412),
    ('Constanța', 242),
    ('Iași', 318),
    ('Satu Mare', 542)
]
# sortați lista după distanță

# sortați lista după distanță
def second(elem):
     return elem[1] # returnăm al doilea element
cities.sort(key=second)
print(cities)


# Exercițiu:
lst = ["zero", "unu", "doi", "trei", "patru", "cinci"]
# faceți print celui de-al doilea element
lst[1]

# faceți print penultimului element
lst[-2]

# faceți print slice-ului cu primele 3 elemente
lst[:3]

# faceți print slice-ului cu ultimele 2 elemente
lst[-2:]

# faceți print slice-ului cu toate elementele fără ultimele 2
lst[:-2]

# faceți print slice-ului care conține fiecare al 2lea element
lst[1::2]

# faceți prin listei cu elementele reversate, folosind sintaxa de slice
# (adică nu faceți .reverse() listei)
lst[-1::-1]

# "vrem o listă nouă reversată, lăsând lista originală neatinsă"
# A)
reversed = lst[-1::-1]
# B)
reversed = lst.copy()
reversed.reverse()


# Exercițiu:
# dată fiind lista de tuple
people = [
    ("Jane", 45),
    ("Jay", 12),
    ("Robert", 18),
    ("Andrew", 68),
    ("Mary", 33),
]
# scrieți o funcție
def filter_by_age(lst):
    pass
# ce returnează o nouă listă
# cu oamenii cu vârsta cuprinsă între 18 și 60 de ani

# [!!!]  pattern de acumulare, adaptat la funcție

# pattern de acumulare:
# 1. declarăm obiectul final
# 2. iterăm prin obiectul sursă
# 3. filtrăm dacă este cazul
# 4. ne pregătim valoarea curentă
# 5. acumulăm
# 6. gata.

def filter_by_age(lst):
    out = []

    for item in lst:
        if 18 <= item[1] <= 60:
            out.append(item)

    # "gata"
    return out

print(
    filter_by_age(people)
)