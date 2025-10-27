import numpy as np
print('Ottobre: ')
sett=['Lunedì','Martedì','Mercoledì','Giovedì','Venerdì','Sabato','Domenica']
sett_ottobre=sett*5
for g in sett_ottobre[2: 33]:
	print(g)

inizio = 2
n_giorni = 31

mese_ottobre = {}
for giorno in range(1, n_giorni+1):
    mese_ottobre[giorno] = sett[(inizio + giorno - 1) % 7]

print(mese_ottobre)

