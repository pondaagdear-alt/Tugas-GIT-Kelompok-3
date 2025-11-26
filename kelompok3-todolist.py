# Fungsi Edit dan Hapus Tugas

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
