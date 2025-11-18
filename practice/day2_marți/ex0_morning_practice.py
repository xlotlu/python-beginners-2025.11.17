#1. obțineți partea întreagă a împărțirii lui 17 la 4.
17 // 4

#2. obțineți restul împărțirii lui 17 la 4.
17 % 4

#3. ridicați 8 la puterea a 3a.
8 ** 3

#4. setați variabilele
name = "Jane"
is_student = True

# și folosiți-le într-un condițional care să facă print
# pe un branch la "<name> is a student",
# și pe celălalt la "<name> is not a student".

if is_student:
    print(name, "is a student")
else:
    print(name, "is not a student")

# repetați codul cu variabilele 
name = "Andrew"
is_student = False

if is_student:
    print(name, "is a student")
else:
    print(name, "is not a student")

#5. concatenați string-ul "bla bli blu" cu sine de 7 ori.
"bla bli blu" * 7

#6. scrieți o funcție `cube(x)` ce calculează x la puterea a 3a.
def cube(x):
    return x ** 3

#7. luați un număr întreg ca input de la utilizator,
# și folosind funcția cube() faceți print cu textul
# "Cubul numărului <număr> este <cub>."
# Folosiți string interpolation.
num = input("Un număr întreg pls: ")
num = int(num)
print(
    "Cubul numărului %d este %d." % (num, cube(num))
)

#8. cereți numele utilizatorului, și, folosind
# funcția `greet_by_tod()` de ieri,
# faceți print unui string de forma "<greeting>, <name>!".

from practice.day1_luni.ex2_functions import greet_by_tod

name = input("Numele tău? ")
print(
    "%s, %s!" % (greet_by_tod(), name)
)