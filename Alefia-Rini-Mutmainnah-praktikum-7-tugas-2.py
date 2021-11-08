print("program menentukan hari dalam bulan tertentu")
def tanggalbulan(bulan):
        if bulan in [1,2,3,4,5,6,7,8,9,10,11,12]:
            if bulan == 2:
                tahun = int(input("masukkan tahun : "))
                tanggaltahun(tahun)
            else:
                if bulan in [1,3,5,7,8,10,12]:
                    print("ada 31 hari dalam bulan")
                else:
                    print("ada 30 hari dalam bulan")
        else:
            print(f"nilai yang dimasukkan salah : {bulan}")

def tanggaltahun(tahun):
        if tahun%4==0:
            print("ada 29 hari dalam bulan")
        else:
            print("ada 28 hari dalam bulan")

loop = True
while loop == True:
    print("masukkan -1 untuk berentikan program")
    bulan = int(input("masukkan bulan (1-12) : ")) 
                      
    if bulan == -1:
        print("terimakasih telah memilih program kami, sampai jumpa.")
    else:
        tanggalbulan(bulan)
        
