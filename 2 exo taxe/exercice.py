print("\t ",52*"*")
print("\t  ** Calcul du montant total toutes taxes comprises **")
print("\t ",52*"*")

print("\n")
print("\n")

x=float(input("\t Saisissez le prix de l'article 1 :"))
y = float(input("\t Saisissez le prix de l'article 2 :"))
z = float(input("\t Saisissez le prix de l'article 3 :"))

print("\n")

s=x+y+z
round(s,3)
print("\t le montant total est     : ", round(s,2), "$")
taxe=s*0.05
round(taxe,3)
print("\t La taxe federale est     : ", round(taxe), "$")
tvq=s*0.09975

print("\t La taxe provinciale est  : ", round(tvq,2), "$")

print("\n")
prt=s+taxe+tvq
print("\t Le montant a payer est   : ", round(prt,1), "$")
print("\n")

print("Merci d'avoir magasine chez nous.")
print("Nous sommes heureux de vous avoir comme client.")
print("Au plaisir de vous servir une autre fois.")
