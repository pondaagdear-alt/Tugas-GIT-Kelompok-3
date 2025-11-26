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
