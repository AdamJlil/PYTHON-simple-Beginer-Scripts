print()
n = int(input("\t Saisissez le nombre de note (sur 20) :  "))
listA=[]
s=0
print()
for i in range(n):
    print("Saisissez la note numero", i + 1, "sur 20")
    xvar = float(input())
    while xvar>20:
        print("ERREUR (!! note superieure a 20) Saisissez la note numero",i+1,"sur 20")
        xvar = float(input())
    s=s+xvar
    listA.append(xvar)


y = []
y = sorted(listA)
moyenne = s/n
print()
print("\t Voici les notes en ordre croissant : ", y)
print("\t la moyenne des notes saisis est : ", moyenne)
