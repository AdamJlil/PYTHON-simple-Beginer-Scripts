h=-1
m=-2

while h<0 or m<0 or h>23 or m>59:
    m = int(input("Saisissez la minute : "))
    h = int(input("Saisissez l'heure : "))

m1 = m+1
h1 = h+1

if h >= 23 and m<59:
    print("L'heure actuelle est : ", h ," : ", m1)
elif h==23 and m==59:
    print("L'heure actuelle est : 00 : 01 ")
elif h < 23 and m==59:
    print("L'heure actuelle est : ",h1," : 01")