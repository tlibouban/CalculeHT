# -*- coding: utf-8 -*-
#
#
from sys import version

if version[0] == "3":
    raw_input = input
print("""
    Bienvenue dans l'appli2ouf
""")
print("""
    Les devises prisent en charge sont :
        Le dollars  [1]
        L'euro      [2]
        Le franc    [3]""")
while true:
    response = raw_input("    Choisissez votre devise 1, 2 ou 3 : ")
    if response in ['1', '2', '3']:
        break
    else:
        print("Choix incorrect !")
devise = response
if response == str(1):
    devise = "$"
    print("Le dollars  [1]")
elif response == str(2):
    devise = "€"
    print("L'euro      [2]")
elif response == str(3):
    devise = "Frs"
    print("Le franc    [3]")
print("Vous avez choisi : ", devise)
vatTX = input("Quel est le taux de TVA ? ")
vatTX = float(vatTX)
vatTX = float("{0:.2f}".format(vatTX))
priceTTC = input("Quel est le prix TTC (" + devise + ") ?")

priceTTC = float(priceTTC)
priceHT = priceTTC / (1 + (1 * (vatTX / 100)))
amountVAT = priceTTC - priceHT
amountVAT = float(amountVAT)
amountVAT = float("{0:.2f}".format(amountVAT))
print("""
 Le prix HT est :
 %.2f""" % priceHT, devise)
print("""
 Le montant de la TVA est :
 %.2f""" % amountVAT, devise)
