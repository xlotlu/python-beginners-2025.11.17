# 1. basics

import module

from module import symbol

# symbol poate să fie:
# - variabilă
# - funcție
# - clasă
# - un alt modul


# 2. alias-uri

import module as mymod

from module import symbol as mysymb


# 3. multi-import

import module1, module2

from module import symbol1, symbol2

from module import (
    symbol1,
    symbol2,
    symbol3,
    symbol4,
    symbol5,
    symbol6,
)

from module import *


# 4. packages:
#    adică un modul care e părinte
#    pentru alte module
#    (un folder, opțional cu fișierul __init__.py)


# 5. cale relativă
#    !!! merge doar în interiorul unui package
from . import submodule
from .submodule import symbol


# 6. de știut:
#    1) importul cauzează evaluarea fișierului
#    2) importul este cache-uit

# dacă vrem să ștergem cache-ul:
del sys.modules['mymodule']

# 7. nu uitați:

import this
