import json

with open("body.json", encoding="utf-8") as vstupni_soubor:
    data = json.load(vstupni_soubor)

print(data)
#novy slovnik a pass/fail

novy_slovik = {}
for item, body in data.items():
    if body >= 60:
        novy_slovik[item] = "Pass"
    else:
        novy_slovik[item] = "Fail"
print(novy_slovik)

with open("vysledek.json", mode="w", encoding="utf-8") as vystupni_soubor:
    json.dump(novy_slovik, vystupni_soubor, ensure_ascii=False, indent=4)
