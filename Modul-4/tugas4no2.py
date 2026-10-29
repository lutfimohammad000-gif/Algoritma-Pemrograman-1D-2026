total = 0

for hari in range(1, 8):
    print("Hari ke-", hari)

    while True:
        lembur = int(input("Jam lembur: "))

        if lembur > 8:
            print("Jam lembur melebihi batas!")
            upah = 0
            break
        elif lembur >= 0 and lembur <= 3:
            upah = lembur * 25000
            break
        elif lembur == 4:
            upah = 100000
            break
        elif lembur == 6:
            upah = 200000
            break
        elif lembur == 8:
            upah = 300000
            break
        else:
            print("Jam lembur tidak sesuai ketentuan, masukkan ulang!")

    shift = input("Shift malam? (ya/tidak): ")

    if shift == "ya":
        tambahan = 50000
    else:
        tambahan = 0

    gaji = 100000 + upah + tambahan
    total += gaji

    print("Gaji harian: Rp", gaji)

print("Total gaji mingguan: Rp", total)

