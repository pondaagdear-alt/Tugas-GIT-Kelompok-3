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

