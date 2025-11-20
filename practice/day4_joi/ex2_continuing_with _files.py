# să join-uim path-uri
# să închidem fișierele (și să știm când e nevoie)
# și să facem și write

from os import path
from config import BASE_DIR


filename = "txtfile.txt"

# nu facem așa
# filepath = BASE_DIR + '/' + filename

# facem așa
filepath = path.join(BASE_DIR, filename)

# mai există și pathlib
""" # acesta este un multi-line string
import pathlib
path = pathlib.Path("/somewhere/over/the-rainbow")
path.joinpath("and", "so on...")
"""


def readit():
    fp = open(filepath, encoding="utf-8")

    try:
        lst = [1, 2, 3]
        print(lst[5])
        content = fp.read()
    except Exception:
        # whatever
        pass
    else:
        return content
    finally:
        fp.close()


try:
    content = readit()
except Exception:
    #print("totul merge mai departe")
    content = ""

# `with` introduce un "context manager"
with open(filepath, encoding="utf-8") as fp:
    print(fp.read())
    1 / 0

def read():
    fp = open(filepath, encoding="utf-8")
    content = fp.read()

    # mai fac un milion de chestii
    return content


# Exercițiu
# scrieți o funcție
def writeinto(filename, content, overwrite=False):
    pass
# care scrie în fișierul `filename`, conținutul `content`,
# refuzând să înlocuiască fișierul dacă `overwrite` = False.
#
# deschideți fișierul folosind context manager.

# DRY
def writeinto(filename, content, overwrite=False):
    # if overwrite:
    #     mode = 'w'
    # else:
    #     mode = 'x'
    
    mode = 'w' if overwrite else 'x'

    with open(filename, mode, encoding="utf-8") as fp:
        fp.write(content)


writeinto("test-overwrite.txt", "ceva content") # merge prima oară
writeinto("test-overwrite.txt", "ceva content") # nu merge a doua oară
writeinto("test-overwrite.txt", "alt content", True) # dar așa merge


# Exercițiu
# scrieți o funcție
def cp(source, target, overwrite=False):
    pass

# ce copiază conținutul fișierului de la locația `source`
# în fișierul de la locația `target`.

# Take 1:
def cp(source, target, overwrite=False):
    with open(source, 'r', encoding="utf-8") as fin:
        content = fin.read()

    mode = 'w' if overwrite else 'x'
    with open(target, mode, encoding="utf-8") as fout:
        fout.write(content)




def cp(source, target, overwrite=False):
    with open(source, 'r', encoding="utf-8") as fin:
        content = fin.read()

    mode = 'w' if overwrite else 'x'
    with open(target, mode, encoding="utf-8") as fout:
        fout.write(content)

# Take 2:
# multiple context managers
def cp(source, target, overwrite=False):
    mode = 'w' if overwrite else 'x'
    
    with (
        open(source, 'r', encoding="utf-8") as fin,
        open(target, mode, encoding="utf-8") as fout
    ):
        fout.write(
            fin.read()
        )

# Take 3:
# îmbunătățim utilizarea memoriei
# (dar începem să ne dăm seama că merge doar în mod text)
def cp(source, target, overwrite=False):
    mode = 'w' if overwrite else 'x'
    
    with (
        open(source, 'r', encoding="utf-8") as fin,
        open(target, mode, encoding="utf-8") as fout
    ):
        for line in fin:
            fout.write(line)

# Take 4:
# funcționăm și cu fișiere binare
# (și folosim "walrus" operator)
def cp(source, target, overwrite=False, chunk=8192):
    mode = 'wb' if overwrite else 'xb'
    
    with (
        open(source, 'rb') as fin,
        open(target, mode) as fout
    ):
        while content := fin.read(chunk):
            fout.write(content)
