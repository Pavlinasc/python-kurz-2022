sklad = {
  "1N4": 250,
  "BAV": 54,
  "KC1": 147,
  "2N7": 97,
  "BC5": 10
}
kod=input("Zadej kod soucastky: ")
mnozstvo= int(input("Zadej mnozstvo: "))

if kod not in sklad:
    print(f"Bohuzel soucastka neni na sklade.")
elif kod in sklad and mnozstvo not in sklad:
    print("Pouze Omezene mnozstvi kusu.")
    sklad.pop(kod)
elif kod in sklad and mnozstvo <= sklad:
    mnozstvo= sklad(mnozstvo) - mnozstvo
    print("Vase objednavka je prijata.")