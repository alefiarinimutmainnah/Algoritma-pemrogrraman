from math import sqrt

print("--Persamaan Kuadrat--")
print("=====================================")
a = int(input("masukan koefisien A = "))
b = int(input("masukan koefisien B = "))
c = int(input("masukan koefisien C = "))

d = (b**2) - (4*a*c)

if a == 0:
    print("Koefisien A tidak boleh 0")
else:
    print(f"Persamaan Kuadrat {a} x^2 + {b}x + {c}")
    print(f"Determinan = {d}")

    if d < 0:
        print("Merupakan Jenis Akar Imaginer")
        print(f"Akar x1 = -{b} + Akar {d} / {b} * {a}")
        print(f"Akar x2 = -{b} - Akar {d} / {b} * {a}")
    elif d == 0:
        x1 = -b / (2*a)
        x2 = x1
        print("Merupakan Jenis Akar Kembar")
        print(f"Akar x1 = {x1}")
        print(f"Akar x2 = {x2}")
    elif d > 0:
        x1 = (-b + sqrt(d)) / (2*a)
        x2 = (-b - sqrt(d)) / (2*a)
        print("Merupakan Jenis Akar Berbeda")
        print(f"Akar x1 = {x1}")
        print(f"Akar x2 = {x2}")
