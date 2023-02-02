print(multi(4,5))
vysledek = multi(3, 5)
print(f"Vysledko je: {vysledek}")


price_night = 850
price_breakfast = 125
def total_price(persons, breakfast=False):
    if breakfast:
        price_person = price_night + price_breakfast
    else:
        price_person = price_night
    return persons * price_person

print(total_price(12, False))

#priklad 3
