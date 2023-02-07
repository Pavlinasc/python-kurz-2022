import json

with open("body.json", encoding="utf-8") as vstupni_soubor:
    data = json.load(vstupni_soubor)

print(data)
#neviem, ako mam prepisat values :(
for item, body in data.items():
    if body >= 60:
        body == "Pass"
    else:
        body == "Fail"
print(data)

with open("vysledek.json", mode="w", encoding="utf-8") as vystupni_soubor:
    json.dump(data, vystupni_soubor, ensure_ascii=False, indent=4)
