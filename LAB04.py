try:
    print("Selamat datang di Pacil Mart!\n")
    file = input("Masukkan nama file input: ")
    # mengecek format file, kalau tidak ada .txt maka ditambahkan .txt
    if file[-4:] != ".txt":
        file += ".txt"
    file_input = open(file, "r")
    lines = file_input.readlines()
    jumlah = 0
    kembalian = 0
    # Cek file kosong atau tidak
    if not lines:
        print("File input ada tapi kosong")
    # Supaya format file sesuai
    elif not all(len(line.split()) == 3 for line in lines):
        print("Format file tidak sesuai")
    else:
        print("Nama Barang |  Jumlah| Kembalian")
        print("---------------------------------")
        for line in lines:
            line = line.split()
            if int(line[2]) <= 0:
                print("Harga satuan barang harus > 0")
                break
            if int(line[1]) <= 0:
                print("Uang yang dialokasikan harus > 0")
                break

            jumlah = int(line[1]) // int(line[2])
            kembalian = int(line[1]) % int(line[2])
            
            if len(line[0]) > 12:
                line[0] = line[0][:12]
            if len(line[1]) > 8:
                line[1] = line[1][:8]
            if len(line[2]) > 10:
                line[2] = line[2][:10]
            print(f"{line[0]:<12}|{jumlah:>8}|{kembalian:>10}")
    file_input.close()
# Exception kalau file tidak ada
except FileNotFoundError:
    print("File tidak tersedia")