import glob
import os

local = input('local = ')

tudo = glob.glob(local + '\\*')
print(tudo)

qtd = int(input('delete how many characters ? '))

for i in range(len(tudo)):

 arqu = os.path.basename(tudo[i])  # receive 1 file from the list (only name without path)
 
 f = arqu[qtd:]
 
 fim = local + '\\' + f

 os.rename(tudo[i], fim)



