#imports here

from logger import logger
from summa import summa
from erotus import erotus

logger("aloitetaan ohjelma")

x = int(input("luku 1: "))
y = int(input("luku 2: "))

print(f"Lukujen {x} ja {y} summa on {summa(x, y)}")  # muutos bugikorjaus-branchissa
print(f"Lukujen {x} ja {y} erotus on {erotus(x, y)}")  # muutos bugikorjaus-branchissa
<<<<<<< HEAD
#hello this is the bugfix branch
=======
#hello this is the main branch
>>>>>>> main
logger("lopetetaan")
print("goodbye") #bugfix
