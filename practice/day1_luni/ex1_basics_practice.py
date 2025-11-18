# Exercițiu:
# faceți input pentru a afla vărsta utilizatorului, apoi
# faceți input pentru a afla vărsta prietenului utilizatorului, apoi
# faceți print cu diferența de vârstă dintre aceștia.

user_age = input("Your age? ")
friend_age = input("Friend's age? ")

# TODO: what if the age is malformed / not an integer?
#       (will have to check if the string is an int,
#        and loop until input is correct.)
user_age = int(user_age)
friend_age = int(friend_age)

print("Age diff", user_age - friend_age)


# Exercițiu:
# puteți face ca diferența de vârstă să fie întotdeauna afișată ca pozitivă?

# Răspuns 1:
if user_age > friend_age:
    print("Age diff", user_age - friend_age)
else:
    print("Age diff", friend_age - user_age)

# Răspuns 2:
print("Age diff", abs(user_age - friend_age))

# Exercițiu:
# declarați variabilele
# user_name, user_age
# friend_name, friend_age
#
# comparați vârstele,
# și scrieți "X is older" sau "Y is older"


user_name, user_age = "John", 68
friend_name, friend_age = "Andrew", 72

if user_age > friend_age:
    print(user_name, "is older")
elif friend_age > user_age:
    print(friend_name, "is older")
else:
    print(user_name + " and " + friend_name + " have the same age")


# Exercițiu
# Date fiind variabilele de mai sus,
# faceți print stringului:
# "A este mai în vârstă decât B cu X ani".

"%s are %d ani" % ("Ionel", 22)


younger = user_name if user_age < friend_age else friend_name
older = user_name if user_age > friend_age else friend_name

# am introdus un bug?
# da. când vârstele sunt egale, nu avem rezultat.

print(
    "%s este mai în vârstă decât %s cu %d ani" %
    (older, younger, abs(user_age - friend_age))
)


"""
Am făcut:
- condiționale
- "type casting" (transformare în int)
- string interpolation ("formatting")
- value if condition else other_value
"""













