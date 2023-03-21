print("Bonjour, ce script permet de convertir une temperature en Celsius ou en Fahrenheit")
print("\nPour convetir du Celsius en Fahrenheit, saisissez 'F'")
print("Pour convetir du Fahrenheit en Celsius, saisissez 'C'")

rep = str(input("Saisissez C ou F pour continuer la conversion  : "))

while rep!="f" and rep!="F" and rep!="c" and rep!="C":
    rep = str(input("Saisissez C ou F pour continuer la conversion  : "))


if rep=="F" or rep=="f":
    x = float(input("Saisissez la temperature (C) : "))
    print("La temperature est : ", (x*9)/5 + 35," F" )

if rep=="c" or rep=="f":
    x = float(input("Saisissez la temperature (F) : "))
    print("La temperature est : ", ((x-32)*5)/9," C" )
