# Fungsi tambah dan tampilkan tugas

to_do_list = []

def tambah_tugas():
    tugas = input("Masukkan tugas baru: ")
    to_do_list.append(tugas)
    print("✔ Tugas berhasil ditambahkan.\n")


def tampilkan_tugas():
    if not to_do_list:
        print("✖ Belum ada tugas.\n")
    else:
        print("\n====== DAFTAR TUGAS =====")
        for i, tugas in enumerate(to_do_list, start=1):
            print(f"{i}. {tugas}")
        print()


# Fungsi Edit dan Hapus Tugas

def edit_tugas():
    tampilkan_tugas()
    if not to_do_list:
        return
    
    try:
        nomot = int(input("pilih nomor tugas yang ingin di edit: "))
        if  1 <= nomor <= len(to_do_list):
            tugas_baru = input("masukan tugas baru: ")
            to_do_list[nomor - 1]  = tugas_baru
            print("✔tugas berhasil diubah!\n")
        else:
            print ("✖ Nomor tidak valid.\n")
    except ValueError:
        print("✖ Input harus berupa angka.\n")

def hapus_tugas():
    tampilkan_tugas()
    if not to_do_list:
        return

    try:
        nomor = int(input("pilih nomor tugas yang ingin dihapus: "))
        if 1 <= nomor <= len (to_do_list):
             print("✔ Tugas berhasil dihapus!\n")
        else:
            print("✖ Nomor tidak valid.\n")
    except ValueError:
        print("✖ Input harus berupa angka.\n")

# Fungsi Simpan dan Muat Data

def simpan_data():
    with open("to_do.txt", "w") as file:
        for tugas in to_do_list:
            file.write(tugas + "\n")
    print("✔ Data berhasil disimpan ke to_do.txt!\n")


def muat_data():
    try:
        with open("to_do.txt", "r") as file:
            for baris in file:
                to_do_list.append(baris.strip())
        print("✔ Data berhasil dimuat!\n")
    except FileNotFoundError:
        print("ℹ Tidak ditemukan file sebelumnya. Membuat baru...\n")

# Menu Utama Program 

def menu():
    muat_data()  # memuat data saat aplikasi dibuka

    while True:
        print("===== Aplikasi To-Do List =====")
        print("1. Tambah Tugas")
        print("2. Tampilkan Tugas")
        print("3. Edit Tugas")
        print("4. Hapus Tugas")
        print("5. Simpan Tugas")
        print("6. Keluar\n")

        pilihan = input("Pilih menu (1-6): ")

        if pilihan == "1":
            tambah_tugas()
        elif pilihan == "2":
            tampilkan_tugas()
        elif pilihan == "3":
            edit_tugas()
        elif pilihan == "4":
            hapus_tugas()
        elif pilihan == "5":
            simpan_data()
        elif pilihan == "6":
            print("Terima kasih telah menggunakan aplikasi!")
            break
        else:
            print("✖ Pilihan tidak valid. Silakan pilih 1-6.\n")


menu()
