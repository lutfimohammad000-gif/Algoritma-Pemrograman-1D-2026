jbaris = int(input("Masukkan jumlah baris lampu: "))
jlampu = int(input("Masukkan jumlah lampu setiap baris: "))

for i in range(1, jbaris + 1):
    print("Pemeriksaan baris", i)

    for j in range(1, jlampu + 1):
        if j % 3 == 0:
            print("Lampu", j, "mengalami gangguan")
        else:
            print("Lampu", j, "berfungsi normal")

print("Periksa sumber listrik utama taman!")
