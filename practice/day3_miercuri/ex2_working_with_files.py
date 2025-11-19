# working with files

fp = open("path") # default: mode 'r'

# open() rulat fără argumentul encoding,
# moștenește encoding-ul default al sistemului.

# good practice (mai ales pe windows!) este
# să specificați encoding

fp = open("cheatsheet.rst", encoding="utf-8")

import os
# căile se rezolvă relativ la "current working directory"
os.getcwd()
# care se putea schimba
os.chdir("/tmp")






# citim, câte puțin:
fp.read(100)
# sau tot:
fp.read()

# dacă vreau să citesc de la început?
fp.seek(0)




# Exercițiu:
# scrieți funcția
def grep(str, filename):
    pass
# care deschide fișierul de la calea `filename`
# și printează fiecare linie care conține `str`


def grep(str, filename):
    fp = open(filename)

    #for line in fp.read().split("\n"):
    #for line in fp.read().splitlines():

    for line in fp.readlines():
        if str in line:
            print(line.removesuffix("\n"))

grep("the age", "txtfile.txt")


# Exercițiu:
# încercați să iterați direct pe un file object.
# funcționează? dacă da, ce se întâmplă?

def grep(str, filename):
    fp = open(filename)

    # când suntem în mod text,
    # vom vrea să iterăm direct
    for line in fp:
        if str in line:
            print(line.removesuffix("\n"))










print("ok?")


# de vizitat:
fp.close()
fp.flush()
