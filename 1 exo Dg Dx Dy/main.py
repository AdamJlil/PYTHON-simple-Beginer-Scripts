
print("\n \t",66*"*")
print("\t **  Resolution d'un systeme de deux equations a deux inconnues  **")
print("\t",66*"*")


a1 = float(input("\nSaisissez la valeur de a1 SVP \t : "))
b1 = float(input("Saisissez la valeur de b1 SVP \t : "))
c1 = float(input("Saisissez la valeur de c1 SVP \t : "))

a2 = float(input("Saisissez la valeur de a2 SVP \t : "))
b2 = float(input("Saisissez la valeur de b2 SVP \t : "))
c2 = float(input("Saisissez la valeur de c2 SVP \t : "))

D = a1*b2 - a2*b1
Dx = c1*b2 - c2*b1
Dy = a1*c2 - a2*c1

x=Dx/D
y=Dy/D

if D == 0:
    if Dx ==0:
        print("Systeme indetermine, les 2 droites sont confondue")
    else:
        print("Systeme impossible, les 2 droites sont paralleles")
else:
    print("\n \t Solution du systeme : ( x ; y ) = (",round(x,2) ,"\t ;\t",round(y,2),")")

print("\n \t ---- A bientot ----")

