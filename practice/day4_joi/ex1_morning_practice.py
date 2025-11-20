# Exercițiu:
# scrieți o funcție
def count_appearances(s, txt, insensitive=False):
    pass

# care returnează numărul aparițiilor
# stringului `s` în stringul `txt`

def count_appearances(s, txt, insensitive=False):
    if insensitive:
        s = s.casefold()
        txt = txt.casefold()
    return txt.count(s)


def count_appearances(s, txt, insensitive=False):
    if insensitive:
        return txt.casefold().count(s.casefold())
    else:
        return txt.count(s)


count_appearances("bla", "bla bla")             # --> 2
count_appearances("bla", "bla bla Bla")         # --> 2
count_appearances("bla", "bla bla Bla", True)   # --> 3

count_appearances("BLA", "bla bla")             # --> 0
count_appearances("BLA", "bla bla", True)       # --> 2

# like, really, don't do this....
def c(s, txt, insensitive=False): return txt.casefold().count(s.casefold()) if insensitive else txt.count(s)