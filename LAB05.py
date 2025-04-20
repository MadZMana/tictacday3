import math

def volume_balok(panjang, lebar, tinggi):
    return panjang * lebar * tinggi

def volume_kerucut(jari_jari, tinggi):
    return (1/3) * math.pi * (jari_jari**2) * tinggi

nama = input("Masukkan nama anda: ")
nama = nama.capitalize()
volume_balok_total = 0
volume_kerucut_total = 0
print(f"\nSelamat datang di Depot Minuman {nama}!")
print("=========================================")
while True:
    bentuk_galon = input("\nMasukkan bentuk galon yang diinginkan (STOP untuk berhenti): ")
    if bentuk_galon == "BALOK":
        panjang = float(input("Masukkan panjang balok: "))
        lebar = float(input("Masukkan lebar balok: "))
        tinggi = float(input("Masukkan tinggi balok: "))
        if panjang <= 0 or lebar <= 0 or tinggi <= 0:
            print("Panjang, lebar, dan tinggi harus lebih dari 0")
            continue
        volume = volume_balok(panjang, lebar, tinggi)
        volume_balok_total += volume
    if bentuk_galon == "KERUCUT":
        jari_jari = float(input("Masukkan jari-jari kerucut: "))
        tinggi = float(input("Masukkan tinggi kerucut: "))
        if jari_jari <= 0 or tinggi <= 0:
            print("Jari-jari dan tinggi harus lebih dari 0")
            continue
        volume = volume_kerucut(jari_jari, tinggi)
        volume_kerucut_total += volume
    if bentuk_galon == "STOP":
        break
    elif bentuk_galon != "BALOK" and bentuk_galon != "KERUCUT" and bentuk_galon != "STOP":
        print("Input tidak benar, masukkan kembali\n")
        continue

total_volume = volume_balok_total + volume_kerucut_total
total_bayar = total_volume * 700
if total_volume > 0 and total_bayar > 0:
    print("\n=============================================")
    print(f"Total volume air yang dikeluarkan: {total_volume:.2f}")
    print(f"Total harga yang harus dibayar: Rp. {total_bayar:.2f}")
    print("=============================================")
    print(f"\nTerima kasih telah menggunakan Depot Air Minum {nama}!\n")
else:
    print("\n=================================================")
    print("Anda tidak memasukkan input satupun :(")
    print(f"Terima kasih telah menggunakan Depot Air Minum {nama}!\n")
    print("=================================================")
