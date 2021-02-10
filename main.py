import time
print("Lancement de simple-python en cours, veuillez patienter...")
time.sleep(2)
print("Fait !")
print("Afficher la liste des commandes avec aide()")

#Commande d'aide
def aide():
  print("afficher(n)\nadditionner(n1,n2)\nsoustraire(n1,n2)\nmultiplier(n1,n2)\ndiviser(n1,n2)\ndef répéter(n, texte, a=\"0\", b=\"1\"):")

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

#Commande répéter
def répéter(n, texte, a="0", b="1"):
  for n in range(n,a,b):
    print(texte)    
