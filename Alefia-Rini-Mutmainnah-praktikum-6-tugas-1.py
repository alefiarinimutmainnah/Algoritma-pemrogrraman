nilai = [ 4.00 , 3.75 , 3.50 , 3.00 , 2.75 , 2.50 , 2.00 , 1.75 , 1.50 , 1.25]

def vartoscore(p):

    if p == 'A':
        score = float(nilai[0])
    elif p == 'A-':
        score = float(nilai[1])
    elif p == 'B+':
        score = float(nilai[2])
    elif p == 'B':
        score = float(nilai[3])
    elif p == 'B-':
        score = float(nilai[4])
    elif p == 'C+':
        score = float(nilai[5])
    elif p == 'C':
        score = float(nilai[6])
    elif p == 'C-':
        score = float(nilai[7])
    elif p == 'D':
        score = float(nilai[8])
    elif p == 'E':
        score = float(nilai[9])
    else:
        print('INVALID SCORE!')
        score = 0
    return score

def rata2kan(datanya):
    total = sum(datanya)
    rata2 = float(total / len(datanya))
    return rata2

def masukkandata():
        varnilai = str.upper(input('"exit" untuk berhenti!\nMasukkan nilai siswa: '))
        return varnilai

def hasil():    
    print(('''
          
          
          Nilai siswa:
          {0}
          
          Jumlah siswa: {1}
          
          Total nilai: {2}
          
          Rata-rata nilai = {3}
          
          
          ''').format(datanilai,len(datanilai),sum(datanilai),rata2kan(datanilai)))

datanilai = []
# User Interface
ulang = 0
nomor = 0
while ulang == 0:
    nomor += 1
    nilaivar = masukkandata()
    if nilaivar == 'EXIT':
        ulang = 1
    else:
        s = vartoscore(nilaivar)
        print(('Siswa ke-{0} = {1}').format(nomor,s))
        datanilai.append(s)

hasil()
