def convert(list):
    a = sum(d * 10**i for i, d in enumerate(list[::-1]))
    return a

def tentukan2(a):
    if a == 2:
        return 'nd'
    elif a == 3:
        return 'rd'
    elif a == 1:
        return 'st'
    else:
        return 'th'
    
def tentukan1(a):
    res = [int(a) for a in str(angka)]
    if len(res) >= 2:
        akhir2 = list()
        akhir2.append(res[-2])
        akhir2.append(res[-1])
        che = convert(akhir2)
        if che == 11 or che == 12 or che == 13:
            return 'th'
        else:
            return tentukan2(res[-1])
    else:
        return tentukan2(a)


while True:    
    try:  
        print()
        angka = int(input('Masukkan angka: '))
    except ValueError:
        print('INVALID')
    else:
        hasil = tentukan1(angka)
        print(str(angka)+hasil)
