penumpang = 0
pendapatan = 0
totaljarak = 0
terjauh = 0

while True:
    jarak = float(input("Masukkan jarak penumpang,masukan 0 jika selesai: "))
    if jarak == 0:
        break
    if jarak < 0:
        print("ulang")
        continue

    if jarak <= 5:
        tarif = 3000
    elif jarak <= 15:
        tarif = 3000 + (jarak - 5) * 1000
    else:
        tarif = 13000 + (jarak - 15) * 500

    penumpang = penumpang + 1

    if penumpang % 5 == 0:
        tarif = tarif * 0.5
        print("Diskon 50%")

    print("Tarif:",tarif)

    pendapatan = pendapatan + tarif
    totaljarak = totaljarak + jarak

    if jarak > terjauh:
        terjauh = jarak

print("Jumlah penumpang:",penumpang)
print("Total pendapatan: ", pendapatan,"Rp")
print("Jarak terjauh:", terjauh, "km")

if penumpang > 0:
    rata = totaljarak / penumpang
    print("Rata-rata jarak:", rata, "km")
else:
    print("Belum ada penumpang")
