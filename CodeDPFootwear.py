import time
import pandas as pd
import numpy as np

start = time.time()

men = pd.read_excel("data_footwear.xlsx", sheet_name='Men')
women = pd.read_excel("data_footwear.xlsx", sheet_name='Women')
kids = pd.read_excel("data_footwear.xlsx", sheet_name='Kids')

arrMen = men.to_numpy()
arrWomen = women.to_numpy()
arrKids = kids.to_numpy()

arrCow = [list(row) for row in arrMen]
arrCew = [list(row) for row in arrWomen]
arrCil = [list(row) for row in arrKids]

print("Pilihan kategori gender : ")
print("Men\nWomen\nKids\nAll")
print("\nMasukkan pilihan : ")
pilihan = str(input())
print("Masukkan budget : ")
budget = int(input())
arrPilihan = []

# memilih pilihan footwear
if pilihan.lower() == 'men':
    arrPilihan = arrCow
elif pilihan.lower() == 'women':
    arrPilihan = arrCew
elif pilihan.lower() == 'kids':
    arrPilihan = arrCil
elif pilihan.lower() == 'all':
    arrPilihan = arrCow + arrCew + arrCil

# sorting
arrPilihan.sort(key=lambda x: x[3])

print("Gender setelah di sorting : ")
for item in arrPilihan:
    print(item)

# memindahkan data ke variabel baru
wt = [item[3] for item in arrPilihan]
val = [item[2] for item in arrPilihan]

n = len(arrPilihan)

# dynamic programming
def knapSack(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]], K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
    return K

K = knapSack(budget, wt, val, n)
print("Rate : ", K[n][budget])

# menampilkan barang rekomendasi
i = n
j = budget
total = 0
# menambahkan variabel untuk menghitung jumlah pilihan footwear
count = 0  

print("Rekomendasi Footwear : ")
while i > 0 and j > 0:
    if K[i][j] != K[i-1][j]:
        print(arrPilihan[i-1])
        total += arrPilihan[i-1][3]
        count += 1
        j -= wt[i-1]
    i -= 1

# menampilkan jumlah pilihan footwear
print("Jumlah pilihan footwear: ", count) 
# menampilkan harga total pilihan footwear
print("Total Harga : ", total)

end = time.time()
print("Waktu Running : ", end-start)
