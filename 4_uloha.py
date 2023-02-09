predvolba = "+420"

def cislo(predvolba, mobil):
    vypocet = predvolba + mobil
    return vypocet

tel_cislo = input("Zadej telefone cislo: ")
if len(tel_cislo) == 9:
    print("Spravne cislo")
    print("True")
else:
    print("Zadaj 9 mistne cislo")
    print("False")

print(cislo(predvolba,tel_cislo))

sprava=input("teraz zadaj tvoju SMS spravu: ")
if len(sprava) < 180:
    print("Platis iba 3kc")
elif len(sprava) >= 180:
    print("Platis uz 6ks")
