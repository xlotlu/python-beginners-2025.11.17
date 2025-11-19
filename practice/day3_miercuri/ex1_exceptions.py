# exceptions


try:
    # chestii
    # instanțiem ceva care are nevoie de cleanup
    pass
except (ExceptionType1, ExceptionType2):
    # chestii specifice
    pass
except ExceptionType3 as e:
    print("fac ceva cu", e)
    msg = e.args[0]
    # și pot să fac re-raise:
    raise e
#except ...
else: # opțional
    # se rulează doar când a fost ok
    pass
finally: # opțional
    # rulat întotdeauna
    # aici putem face cleanup
    pass



def myfunc():
    try:
        #1 / 0

        print("am ajuns aici?")
        #statement1()
        #statement2()
        # etc.

    except ZeroDivisionError:
        print("» infinity is closeby")

    except IndexError:
        pass

    except ValueError:
        pass

    except:
        # catch-all exception
        print("» there was some error!")

    else:
        # aceasta se rulează
        # doar dacă tot blocul de sub try
        # a fost în regulă

        print("» everything ok!!!")
        # un bloc complex de logică

    finally:
        print("» acesta se rulează întotdeauna, cu sau fără excepție")

    print("am rulat în continuare")


def myotherfunc():
    print("eu sunt intermediară")
    myfunc()

myotherfunc()


# Exemplu de capturat excepția
# și înlocuit cu o excepție custom:
from datetime import time

def parse_time(timespec):
    "transforms a string into a time object"
    # "xx:yy:zz"
    values = timespec.split(":")
    
    try:
        hour = int(values[0])
        minute = int(values[1])
        second = int(values[2])
    except IndexError as e:
        # avem nevoie de e.args[0] ? nu prea.
        raise ValueError("Invalid timespec: '%s'" % timespec)
    except Exception as e:
        # catch-all. a fost o problemă pe care
        # nu am prevăzut-o.
        # 
        # vrem să o lăsăm să bubuie,
        # dar vrem să logăm problema, undeva...

        print(
            "buba!",
            type(e),
            e.args,
            e.with_traceback
        )

        # las excepția să treacă mai departe
        raise e
    
    return time(hour, minute, second)



