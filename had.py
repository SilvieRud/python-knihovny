import sys

def had_velbloud(parametr):
    slova = parametr.split("_")
    return slova[0] + "".join([slovo[0].upper() + slovo[1:] for slovo in slova[1:]])

print(had_velbloud(sys.argv[1]))
