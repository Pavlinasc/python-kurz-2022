teploty = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]
]
teplota_a = [sum(teplota)/len(teplota) for teplota in teploty]
print(teplota_a)

r_seznam = []
teplota_b = [teplota[0] for teplota in teploty]
print(teplota_b)

for teplota in teploty:
    r_seznam.append(teplota[0])
print(r_seznam)

n_seznam=[]
for teplota in teploty:
    n_seznam.append(teplota[3])
print(n_seznam)

novy_seznam = []
#for teplota in teploty:
#    novy_seznam=(teplota[0] + teplota[3])
#print(novy_seznam)
