# Exercițiu:
# scrieți o funcție
def countdown(seconds):
    pass
# ce printează la fiecare secundă
# timpul rămas

from time import sleep
import sys

# 3 stream-uri fundamentale
# sys.stdout, sys.stdin, sys.stderr

def countdown(seconds):
    #lungimea stringului dat la intrare
    length = len(str(seconds))

    while seconds > 0:
        sys.stdout.write(
            "timp rămas %s\r" % str(seconds).rjust(length)
        )
        sys.stdout.flush()
        sleep(1)
        seconds -= 1
countdown(3)
