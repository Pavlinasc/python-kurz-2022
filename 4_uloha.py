def overcislo(cislo):
    if len(cislo) == 9 or (len(cislo) == 13 and predvolba("+420")):
        return True
    else:
        return False

def cenasms(sprava):
    znaky=len(sprava)
    cena=(znaky//180+1)*3
    return cena

cislo = input("Zadej telefone cislo: ")
if not overcislo(cislo):
    print("Neplatne cislo")
else:
    sprava = input("teraz zadaj tvoju SMS spravu: ")
    cena = cenasms(sprava)
    print("Cena spravy je", cena, "CZK")