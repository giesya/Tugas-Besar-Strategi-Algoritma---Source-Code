import time
import pandas as pd
import numpy as np

start = time.time()

men = pd.read_excel("dataset_footwear.xlsx", sheet_name='Men')
women = pd.read_excel("dataset_footwear.xlsx", sheet_name='Women')
kids = pd.read_excel("dataset_footwear.xlsx", sheet_name='Kids')

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
harga = int(input())
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

print("Footwear setelah di sorting : ")
for i in range(len(arrPilihan)):
    print(arrPilihan[i])

# memilih pakaian
print("Rekomendasi footwear : ")
total = 0
value = 0
count = 0  # menambahkan variabel untuk menghitung jumlah pilihan footwear
for i in range(len(arrPilihan)):
    if harga < arrPilihan[i][3]:
        break
    print(arrPilihan[i])
    total += arrPilihan[i][3]
    value += arrPilihan[i][2]
    harga -= arrPilihan[i][3]
    count += 1  # menambah count untuk setiap footwear yang dipilih

print("Jumlah pilihan footwear: ", count)# menampilkan jumlah pilihan footwear
print("Total harga : ", total)# menampilkan total harga pilihan footwear
print("Rate : ", value)

end = time.time()
print("waktu running", end-start ,"detik")
