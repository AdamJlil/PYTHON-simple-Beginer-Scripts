print("\n\t\tTable de multiplication")
print()


print(" \t|\t",end="")
for i in range(9):
    print(i+1, end = "\t")

print()
print("\t|")
print(43*"-")

for k in range(9):
    print((k+1),"\t|\t",end="")
    for i in range(9):
        print((k+1)*(i+1), end = "\t")
    print()
    print("\t|")
