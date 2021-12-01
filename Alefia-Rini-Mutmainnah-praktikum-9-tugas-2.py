judul = str(input("Masukkan judul file : "))
namafile = (f"{judul}.txt")
f = open(namafile, "w")
f.close()
print(f"File {namafile} telah terbentuk!")
print("Masukkan x untuk berhenti.")

def write(string):
    file = open(f"{judul}.txt","w")
    file.write(str(string))
    file.close()

def read ():
    file = open(f"{judul}.txt", "r")
    teks = file.read()
    print(teks)

a = True
while a == True:
    b = (input(""))
    if b == "x":
        print("\nTeks telah tersimpan!")
        x = False
    else:
        write(b)
        read()
