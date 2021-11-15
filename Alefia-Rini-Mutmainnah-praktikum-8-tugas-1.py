def fibbonaci(a):
   if a <= 1:
       return a
   else:
       return(fibbonaci(a-1) + fibbonaci(a-2))
   
def cetak(x):
    if x <= 0:
        print("Hanya angka postif!")
    else:
       print('Bilangan FIBBONACI ke-'+str(x),'adalah',fibbonaci(x))

while True:
    try:
        bil = int(input('Masukkan bilangan >> '))
    except ValueError:
        print('Invalid input, masukkan angka bulat!\n')
    else:
        cetak(bil)
