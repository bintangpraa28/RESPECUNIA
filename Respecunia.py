from termcolor import colored

# Menu utama
def main():
    catatan_keuangan = []

    while True:
        print(colored("\n========================", "blue"))
        print(colored("=                      =", "blue"))
        print(colored("=   Program Keuangan   =", "blue"))
        print(colored("=      RESPECUNIA      =", "blue"))
        print(colored("=                      =", "blue"))
        print(colored("========================", "blue"))
        print("1. Input Pemasukan dan Pengeluaran")
        print("2. Tampilkan Riwayat Pemasukan dan Pengeluaran")
        print("3. Hapus Catatan")
        print("4. Edit Catatan")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1/2/3/4/5): ")
        
        if pilihan == '1':
            pemasukan_pengeluaran(catatan_keuangan)
        elif pilihan == '2':
            riwayat(catatan_keuangan)
        elif pilihan == '3':
            hapus_catatan(catatan_keuangan)
        elif pilihan == '4':
            edit_catatan(catatan_keuangan)
        elif pilihan == '5':
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Fitur input pemasukan pengeluaran
def pemasukan_pengeluaran(catatan):
    pemasukan_total = 0
    pengeluaran_total = 0

    for bulan in range(1, 4):  # 3 bulan terakhir
        print(f"\nBulan {bulan}:")

        # Validasi pemasukan
        while True:
            pemasukan = input("Masukkan total pemasukan: Rp")
            if pemasukan.replace('.', '', 1).isdigit() and float(pemasukan) >= 0:
                pemasukan = float(pemasukan)
                break
            else:
                print("Input tidak valid! Masukkan angka yang benar untuk pemasukan.")

        # Validasi pengeluaran
        while True:
            pengeluaran = input("Masukkan total pengeluaran: Rp")
            if pengeluaran.replace('.', '', 1).isdigit() and float(pengeluaran) >= 0:
                pengeluaran = float(pengeluaran)
                break
            else:
                print("Input tidak valid! Masukkan angka yang benar untuk pengeluaran.")
        
        print("=====================================")
        
        pemasukan_total += pemasukan
        pengeluaran_total += pengeluaran
        rata_rata_pemasukan = pemasukan_total / bulan
        rata_rata_pengeluaran = pengeluaran_total / bulan
        
        catatan.append({
            'bulan': bulan,
            'pemasukan': pemasukan,
            'pengeluaran': pengeluaran
        })
    
    print("\n=== Catatan rata-rata Pemasukan dan Pengeluaran ===")
    print(f"Rata-rata pemasukan bulanan: Rp {rata_rata_pemasukan:.2f}")
    print(f"Rata-rata pengeluaran bulanan: Rp {rata_rata_pengeluaran:.2f}")
    analisis(pemasukan_total, pengeluaran_total)

# Fitur analisis pengeluaran ideal
def analisis(pemasukan_total, pengeluaran_total):
    print("\n=== Analisis Pemasukan dan Pengeluaran ===")
    if pengeluaran_total > pemasukan_total:
        print("Pengeluaran Anda melebihi pemasukan!")
        saran = (pemasukan_total / 3) * 0.8  # pengeluaran ideal = 80% pemasukan
        print(f"Saran pengeluaran ideal per bulan adalah: Rp {saran:.2f}")
    else:
        print("Pengeluaran Anda sudah ideal.")

# Fitur riwayat pemasukan pengeluaran
def riwayat(catatan):
    print("\n=== Riwayat Pemasukan dan Pengeluaran ===")
    if not catatan:
        print("Belum ada catatan.")
        return
    elif catatan:
        for entry in catatan:
            print(f"Bulan {entry['bulan']}: Pemasukan: Rp {entry['pemasukan']}, Pengeluaran: Rp {entry['pengeluaran']}")

# Fitur hapus catatan
def hapus_catatan(catatan):
    while True:
        bulan = input("Masukkan bulan yang ingin dihapus (1-3): ")
        if bulan.isdigit() and 1 <= int(bulan) <= 3:
            bulan = int(bulan)
            break
        else:
            print("Input tidak valid! Masukkan bulan antara 1 dan 3.")

    for entry in catatan:
        if entry['bulan'] == bulan:
            catatan.remove(entry)
            print(f"Catatan bulan {bulan} berhasil dihapus.")
            return
    print("Catatan tidak ditemukan.")

# Fitur edit catatan
def edit_catatan(catatan):
    while True:
        bulan = input("Masukkan bulan yang ingin diedit (1-3): ")
        if bulan.isdigit() and 1 <= int(bulan) <= 3:
            bulan = int(bulan)
            break
        else:
            print("Input tidak valid! Masukkan bulan antara 1 dan 3.")
    
    for entry in catatan:
        if entry['bulan'] == bulan:
            # Validasi pemasukan
            while True:
                pemasukan = input("Masukkan total pemasukan baru: Rp")
                if pemasukan.replace('.', '', 1).isdigit() and float(pemasukan) >= 0:
                    pemasukan = float(pemasukan)
                    break
                else:
                    print("Input tidak valid! Masukkan angka yang benar untuk pemasukan.")
            
            # Validasi pengeluaran
            while True:
                pengeluaran = input("Masukkan total pengeluaran baru: Rp")
                if pengeluaran.replace('.', '', 1).isdigit() and float(pengeluaran) >= 0:
                    pengeluaran = float(pengeluaran)
                    break
                else:
                    print("Input tidak valid! Masukkan angka yang benar untuk pengeluaran.")
            
            entry['pemasukan'] = pemasukan
            entry['pengeluaran'] = pengeluaran
            print(f"Catatan bulan {bulan} berhasil diperbarui.")
            return
    print("Catatan tidak ditemukan.")

# Memulai program
main()
