def numefunc():
    # statements
    print("m-am rulat")

def add(a, b):
    return a + b


# Exercițiu:
# scrieți o funcție
def ft_to_m(ft):
    pass # placeholder
# ce transformă argumentul `ft` (picioare)
# în metri.
#
# 1ft = 0.3048m

FT_TO_M = 0.3048 # litere mari = convenție: este o constantă

def ft_to_m(ft):
    "primește numărul de picioare și returnează echivalentul în metri"
    return ft * FT_TO_M


ft_from_user = float(input("How many ft? "))
print("That means %s meters" % ft_to_m(ft_from_user))


def m_to_ft(m):
    return m / FT_TO_M


# Exercițiu:
# scriem o funcție `greet(tod)`,
# ce primește ca argument una din valorile:
# "morning", "noon", "evening", "night",
# și returnează salutul potrivit pentru perioada
# respectivă a zilei:
# "good morning" / "good afternoon"
#  / "good evening" / "good night"


def greet(tod):
    if tod == "morning":
        v_greet = "Good morning!"
    elif tod == "noon":
        v_greet = "Good afternoon!"
    elif tod == "evening":
        v_greet = "Good evening!"
    elif tod =="night":
        v_greet = "Good night!"
    else:
        raise ValueError("Invalid time of day: '%s'" % tod)

    return v_greet


# hai să îl rescriem cu match / case


variable = "something else"

match variable:
    case "morning":
        print("was morning")

    case "noon":
        print("was noon")

    case _:
        print("did not match anything")


def greet(tod):
    match tod:
        case "morning":
            return "Good morning!"
        
        case "noon":
            return "Good afternoon!"
        
        case "evening":
            return "Good evening!"
        
        case "night":
            return "Good night!"
        
        case _:
            raise ValueError("Invalid time of day: '%s'" % tod)





# Exercițiu:
# Scrieți o funcție

def greet_by_tod():
    pass

# ce returnează unul din string-urile
#
# "good morning" / "good afternoon"
#  / "good evening" / "good night"
#
# dacă ora curentă a zilei este respectiv între:
# 5-11 / 11-6 / 6-9 / 9-5

# folosim modulul `datetime`, și din el clasa `datetime`.
# folosim metoda `datetime.now().`
# și de pe obiectul obținut folosim atributul `hour`.

from datetime import datetime

# dacă este long-running process,
# aici s-ar face alocarea o singură dată
# now = datetime.now()
# hour = now.hour
# (pentru perpetuitate now va fi momentul inițializării programului)

def greet_by_tod():
    # vrem să detectăm ora curentă la fiecare rulare a funcției
    now = datetime.now()
    hour = now.hour

    if 5 <= hour < 11:
        return 'Good morning'
    elif 11 <= hour < 18:
        return 'Good afternoon'
    elif 18 <= hour < 21:
        return 'Good evening'
    else:
        return 'Good night'

print(greet_by_tod())
    



















