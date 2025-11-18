fundamental concepts:
=====================

callable
totul este obiect
totul este referință

PEP = Python Enhancement Proposal

PEP8: styleguide
https://peps.python.org/pep-0008/




keywords:
=========

clasă --> când este apelată (called), generează un obiect (o instanță a acelei clase)

OCD = obsessive-compulsive disorder



fundamental data types:
=======================

int, float, str
tuple, list


essential debugging tools:
==========================
print()
type()
help()
dir() # returnează lista atributelor obiectului


things special about Python:
============================

whitespace is semantically meaningful,
  except when inside brackets.

operatori:
// și % **

instalare de pachete:
(în shell) pip install ipython


chestii despre VSCode:
======================
Run file: Ctrl+F5
  # rulează executabilul de Python și face exit

Run selection: Shift+Enter
  # rulează executabilul de Python, lasă shell-ul deschis
  # și face copy-paste selecției

Comment selection: Ctrl+/

Make ipython the default shell:
  open settings.json (Ctrl+Shift+p --> search "settings")
  and add:
```
    "python.terminal.launchArgs": [
        "-m", "IPython", "--no-autoindent"
    ],
```


metode uzuale stringuri:
========================

.count

.find / .rfind # returns -1
.index / .rindex # raises ValueError

.startswith / .endswith

.format
```
"{name} are {years:03d} ani".format(name="Andrew", years=12)
```

.isdecimal

.lower / .upper

.replace
.strip / .lstrip / .rstrip

.removeprefix / .removesuffix


[!] .join / .split


sequences:
==========

(o formă particulară de iterabile)

str, tuple, list

- sunt accesibile după index # raises IndexError
  (și după slice)
- au metoda .count()
- au metoda .index() # raises ValueError
- numărabile cu len()
- suportă operatorul `in`


str & tuple: immutable
list:        mutable



excepții uzuale:
================

IndexError
ValueError
TypeError
NameError



essential wisdom:
=================

There are two hard problems in computing:
- naming things
- cache invalidation
- off-by-one errors


from builtins import print, range

