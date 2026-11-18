print("=====Kasir Kantin Kampus=====")
total = 0

while True:
    print("\n DAFTAR MENU")
    print("1. sate ayam = 15.000")
    print("2. ayam bakar = 20.000")
    print("3. ayam goreng = 15.000")
    print("4. mi ayam = 12.000")
    print("5. mi bakso = 12.000")
    print("0. selesai memilih")

    pilihan = int(input("pilih menu:"))
    if pilihan == 0:
        break
    elif pilihan == 1:
        total += 15.000
    elif pilihan == 2:
        total += 20.000
    elif pilihan == 3:
        total += 15.000
    elif pilihan == 4 :
        total += 12.000
    elif pilihan == 5:
        total += 12.000
    else:
        print("Menu tidak ada")

    jumlah = int(input("jumlah pesanan:"))
    subtotal = total * jumlah
    total = total + subtotal
    print("subtotal:", subtotal)

#diskon
if total >100.000:
    diskon = 10
else:
    diskon = 0

potongan = total * diskon / 100
total_bayar = total - potongan

#struk
print("\n=====STRUK PEMBAYARAN=====")
print("total belanja:", total)
print("diskon:", diskon, "%")
print("potongan:", potongan)

print("total bayar:", total_bayar)
print("terima kasih dan selamat menikmati") 
