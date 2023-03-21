print()


v0 = float(input("\tSaisissez le montant du pret en $ : "))
terme = float(input("\tSaisissez le duree de remboursement en annee (s) : "))
n=12*terme
j = float(input("\tSaisissez le taux d'interet annuel en % : "))
i=j/(12*100)

vp = (i*v0*((1+i)**n))/(-1+((1+i)**n))
print("\n\t Le versement periodique est de : ",vp,"$")


print()
print(" ______________________________________________________________")
print("|        |","           |","           |","          |","              |")
print("| Numero |  Versement |  Interet   |  Capital  |    Capital    |")
print("|   vp   | periodique |    paye    |  remburse |      du       |")
print("|        |","           |","           |","          |","              |")
print(" ______________________________________________________________")

print("|        |","           |","           |","          |","   " "%8.2f" %v0,"  |")

n = int(n)
for nvp in range(1,n+1):
    ip = v0*i
    cr = vp - ip
    v0 = v0 - cr
    nvp = str(nvp).zfill(3)
    print("| ",nvp,"  |","%7.2f" %vp,"   |","%7.2f" %ip,"   |","%7.2f" %cr,"  |","   " "%8.2f" %v0,"  |")

print("|        |","           |","           |","          |","              |")
print(" ______________________________________________________________")

