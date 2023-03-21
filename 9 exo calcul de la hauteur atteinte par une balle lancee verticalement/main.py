print()
print("\tCalcul de la hauteur atteinte par une balle lance verticalement")
print()
v0 = float(input("Saisissez la vitesse de lancement initiale en m/s: "))
print()
d = float(input("Saisissez la duree de calcul en ms: "))
g = 9.81
t=0
print()

while t<=d:
    h = -(1 / 2) * g * ((t/1000) ** 2) + v0 * (t/1000)
    print("a t =","%5.0f" %t," ms la hauteur de la balle est : ", "%0.3f" %h ," m")
    t += 50
    if h<0:
        break

