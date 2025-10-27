import numpy as np
n = input('fino a quanto vuoi sommare? ')
nf = int(n)
somma = 0
for i in range(nf+1):
	somma=somma+i

print('La somma dei primi', n, "numeri naturali e':", somma)
