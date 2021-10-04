Created on Mon Oct  4 14:21:13 2021

@author: ALEFIA RINI
"""

x = int(input("Sisi A: "))
y = int(input("Sisi B: "))
z = int(input("Sisi C: "))

if x + y <= z or x + z <= y or y + z <= x :
    print("Bukan segitiga")
elif x == y and y == z :
    print("Segitiga sama sisi")
elif x == y or x == z or y == z :
    print("Segitiga sama kaki")
elif x*x + y*y == z*z :
    print("Segitiga siku-siku")
else:
    print("Segitiga sembarang")
