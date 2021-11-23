print("ini merupakan program pemangkatan negatif dan positif")

def pangkat(base, power):
    if power == 0:
        return 1
    elif power < 0:
        return 1 / (base * pangkat(base, abs(power)-1))
    else:
        return base * pangkat(base, power-1)

while True:
    base = int(input("Masukan angka : "))
    power = int(input("Masukan pangkat : "))
    print(pangkat(base, power),"\n")
