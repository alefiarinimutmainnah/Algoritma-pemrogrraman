ulangin="y"
while ulangin=="y":
    print("""
----------------------------------------------------
SELAMAT DATANG DI KEBUN STRAWBERRY
----------------------------------------------------
silahkan masukkan kata dan sandi
email 
pass 
    """)
    kata=input("masukan kata:")
    sandi=input("masukan sandi:")
    if kata=="arini" and sandi=="12345":
        ngulang="y"
        while ngulang=="y":
            print("""
----------------------------------------------------
SELAMAT DATANG DI KEBUN STRAWBERRY
----------------------------------------------------
silahkan pilih pembelian tiket

A.TIKET VIP 

----------------------------------------------------
            """)
            pilihtiket = input("Silahkan pilih pembelian tiket dengan memasukkan abjad dari list di atas :")


            if pilihtiket == "a" or pilihtiket == "A":
                ulangtiketkebun = "y"
                while ulangtiketkebun == "y":
                    print("""
------------------------------------
TIKET VIP 
------------------------------------
*BELI TIKET VIP 
- mendapatkan voucer susu coklat hangat
- memetik strawberry sepuasnya 
- Mendapatkan posisi tempat duduk di daerah pegunungan
------------------------------------                    
                    """)
                    pilihan = input("Silahkan Tulis buy untuk membeli tiket :")

                    if pilihan == "buy":
                        stop = "y"
                        while stop == "y":
                            from datetime import datetime

                            current = datetime.now()
                            tahun = current.year
                            bulan = current.month
                            hari = current.day
                            jumlahorang = int(input("Jumlah orang :"))
                            total = []
                            if jumlahorang > 4:
                               print("Jumlah maksimal untuk satu tiket 4 orang")
                               break
                            nama = []
                            umur = []
                            total = 0
                            for i in range(jumlahorang):
                                print("\nData ke-", i + 1)
                                nama_pengunjung = input("Masukkan nama :")
                                umur_pengunjung = int(input("Masukkan umur :"))
                                if umur_pengunjung <= 2:
                                   total += 0
                                   print("tiket GRATIS!")
                                elif umur_pengunjung >= 3 and umur_pengunjung <= 12:
                                   total += 14000
                                   print("tiket sebesar Rp14000")
                                elif umur_pengunjung >=13 and umur_pengunjung < 65:
                                   total += 23000
                                   print("tiket sebesar Rp23000")
                                else:
                                   total += 18000
                                   print("tiket sebesar Rp18000")

                                   
                                print("Total yang harus dibayar : Rp ", total)

                            jumlahbayar = int(input("Masukan uang :Rp"))
                            for i in range(umur_pengunjung ):
                                print("----------------------------------------------")
                                print("Tiket Orang Masuk kebun")
                                print("----------------------------------------------")
                                print("{}/{}/{}".format(hari, bulan, tahun))
                                for cetaknama in nama:
                                    print("nama : {}".format(cetaknama))
                                for cetakumur in umur:
                                    print("umur : {}".format(cetakumur))
                                print("----------------------------------------------")
                                print("Harga : Rp", total)
                                print("Total Harga : Rp", total)
                                print("Kembali : Rp", jumlahbayar - total)
                                print("----------------------------------------------")
                                print("Terimakasih dan selamat menikmati")
                                print("----------------------------------------------")
                                ulangtiketbermain= input("Masukkan y untuk kembali :")
                                break

            else:
                print("User dan password salah")
                ulangin=input("Apakah anda ingin login kembali y/n :")
            
