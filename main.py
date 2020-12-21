import time
print("Lancement de simple-python en cours, veuillez patienter...")
time.sleep(2)
print("Fait !")
print("Afficher la liste des commandes avec aide()")

#Commande afficher
def afficher(n):
  print(n)

#Commande additionner
def additionner(n1,n2):
  print(n1+n2)

#Commande soustraire
def soustraire(n1,n2):
  print(n1-n2)

#Commande multiplier
def multiplier(n1,n2):
  print(n1*n2)

#Commande diviser
def diviser(n1,n2):
  print(n1/n2)

#Commande répéter 1
def répéter(n, ndeux):
  for n in range(n):
    print(ndeux)

#Commande répéter 2
def répéterdeux(n, a, ntrois):
  for n in range(n, a):
    print(ntrois)

#Commande répéter 3
def répétertrois(n, a, b, nquatre):
  for n in range(n,a, b):
    print(nquatre)    