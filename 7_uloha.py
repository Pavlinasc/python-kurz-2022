class Auto:
    def __init__(self, registracna_znacka, typ_vozidla, najete_km):
        self.registracna_znacka = registracna_znacka
        self.typ_vozidla = typ_vozidla
        self.najete_km = najete_km
        self.dostupne = True

    def pujc_auto(self):
        if self.dostupne:
            self.dostupne = False
            return "Vozidlo neni k dispozici"
        else:
            return "Potvrduji pujceni vozidla"
        
    def get_info(self):
        return f"Znacka: {self.registracna_znacka}, Typ: {self.typ_vozidla}"

auto1 = Auto("4A2 3020", "Peugeot 403 Cabrio", 47534)
auto2 = Auto("1P3 4747", "Skoda Octavia", 41253)

pujcka = input("zadaj ktore auto chces Peugeot/Skoda: ")
if pujcka == "Peugeot":
    auto=auto1
elif pujcka == "Skoda":
    auto=auto2
else:
    print("Nezpravne zadanie")

print(auto.get_info())
print(auto.pujc_auto())