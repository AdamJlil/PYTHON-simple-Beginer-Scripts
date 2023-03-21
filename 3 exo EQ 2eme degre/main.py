a = float(input("Saisissez la valeur de a : "))
b = float(input("Saisissez la valeur de b : "))
c = float(input("Saisissez la valeur de c : "))

q = (b**2)-4*a*c
x1= (-b-(q**(1/2)))/(2*a)
x2= (-b+(q**(1/2)))/(2*a)

print("\n \t La valeur du discriminant est : ",q)


if a==0:
    if b!=0:
        print("La solution particuliere de l'equation est: x = "-(c/b))
    elif b==0 and c==0:
        print("La solution est indeterminee (tous les reelles sont solution)")
    elif b==0 and c!=0:
        print("La solution est impossible")

if a!=0:
    if q==0:
        print("\t Une solution reelle double: x1 = x2 = ",x1)
    elif q>0:
        print("\t 2 solutions reelles distinctes : x1 ",x1," et x2 = ",x2)
    elif q<0:
        print("\t Pas de solution reelle")