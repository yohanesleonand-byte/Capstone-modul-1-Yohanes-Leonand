# === SISTEM LOGIN ADMIN ===
def login_admin():
    admin_username = "Ujang Sprocket"
    admin_password = "P Balap"
    attempts = 0
    while attempts < 3:
        username = input("Masukkan username admin: ")
        password = input("Masukkan password admin: ")
        if username == admin_username and password == admin_password:
            print("Login berhasil!\n")
            return True
        else:
            attempts += 1
            print(f"Login gagal. Percobaan ke-{attempts}/3.\n")
    print("Gagal login 3 kali. Program dihentikan.")
    return False


# === DATA MOBIL ===
data_mobil = [
    {"id": 1, "merk": "Volkswagen Golf", "tahun": 2014, "harga": 300000, "warna": "putih", "jumlah_kursi": 4},
    {"id": 2, "merk": "Mercedes Benz C200", "tahun": 2018, "harga": 500000, "warna": "Silver", "jumlah_kursi": 5},
    {"id": 3, "merk": "BMW F30", "tahun": 2018, "harga": 450000, "warna": "Hitam", "jumlah_kursi": 5},
    {"id": 4, "merk": "Toyota Innova Reborn", "tahun": 2022, "harga": 400000, "warna": "Abu-abu", "jumlah_kursi": 5},
    {"id": 5, "merk": "Mazda CX-5", "tahun": 2023, "harga": 450000, "warna": "Merah", "jumlah_kursi": 5},
]


# === FUNGSI CRUD MOBIL ===
def tampilkan_mobil():
    print("\nDAFTAR MOBIL RENTAL:")
    print("-" * 80)
    for mobil in data_mobil:
        print(
            f"ID: {mobil['id']}, Merk: {mobil['merk']}, Tahun: {mobil['tahun']}, "
            f"Harga Sewa: Rp{mobil['harga']:,}/hari, Warna: {mobil['warna']}, "
            f"Jumlah Kursi: {mobil['jumlah_kursi']}"
        )
    print("-" * 80)


def tambah_mobil():
    id_baru = max(mobil["id"] for mobil in data_mobil) + 1
    merk = input("Masukkan merk mobil: ")

    # Validasi tahun
    tahun_input = input("Masukkan tahun mobil (4 digit): ")
    if not tahun_input.isdigit() or len(tahun_input) != 4:
        print("Tahun harus terdiri dari 4 digit angka. Tambah mobil dibatalkan.")
        return
    try:
        tahun = int(tahun_input)
    except ValueError:
        print("Tahun harus berupa angka. Tambah mobil dibatalkan.")
        return

    # Validasi harga
    try:
        harga = int(input("Masukkan harga sewa per hari: "))
    except ValueError:
        print("Harga harus berupa angka. Tambah mobil dibatalkan.")
        return

    warna = input("Masukkan warna mobil: ")

    # Validasi jumlah kursi
    try:
        jumlah_kursi = int(input("Masukkan jumlah kursi: "))
    except ValueError:
        print("Jumlah kursi harus berupa angka. Tambah mobil dibatalkan.")
        return

    # Simpan data jika semua valid
    data_mobil.append({
        "id": id_baru,
        "merk": merk,
        "tahun": tahun,
        "harga": harga,
        "warna": warna,
        "jumlah_kursi": jumlah_kursi
    })
    print("Mobil berhasil ditambahkan!")



def update_mobil():
    try:
        id_edit = int(input("Masukkan ID mobil yang ingin diubah: "))
    except ValueError:
        print("ID harus berupa angka. Update dibatalkan.")
        return

    for mobil in data_mobil:
        if mobil["id"] == id_edit:
            print(f"Data saat ini: {mobil}")

            mobil["merk"] = input("Merk baru: ")

            tahun_input = input("Tahun baru (4 digit): ")
            if not tahun_input.isdigit() or len(tahun_input) != 4:
                print("Tahun harus terdiri dari 4 digit angka. Update dibatalkan.")
                return
            try:
                mobil["tahun"] = int(tahun_input)
            except ValueError:
                print("Tahun harus berupa angka. Update dibatalkan.")
                return

            try:
                mobil["harga"] = int(input("Harga baru per hari: "))
            except ValueError:
                print("Harga harus berupa angka. Update dibatalkan.")
                return

            mobil["warna"] = input("Warna baru: ")

            try:
                mobil["jumlah_kursi"] = int(input("Jumlah kursi baru: "))
            except ValueError:
                print("Jumlah kursi harus berupa angka. Update dibatalkan.")
                return

            print("Data mobil berhasil diupdate!")
            return

    print("Mobil tidak ditemukan.")



def hapus_mobil():
    try:
        id_hapus = int(input("Masukkan ID mobil yang ingin dihapus: "))
    except ValueError:
        print("ID harus berupa angka. Penghapusan dibatalkan.")
        return

    for mobil in data_mobil:
        if mobil["id"] == id_hapus:
            data_mobil.remove(mobil)
            print("Mobil berhasil dihapus!")
            return

    print("Mobil tidak ditemukan.")



# === PEMBAYARAN ===
def menu_pembayaran():
    print('\n------------ Total Pembayaran ---------------')
    peminjam = input("Silahkan masukan nama peminjam: ")
    print("Nama peminjam:", peminjam)

    total1 = 0
    jenis1 = ''

    def fungsi_mobil():
        nonlocal total1, jenis1
        print('\n--------- Jenis Mobil ----------')
        for mobil in data_mobil:
            print(f"{mobil['id']}. {mobil['merk']} ({mobil['tahun']}) - Rp {mobil['harga']:,}/hari, "
                  f"Warna: {mobil['warna']}, Jumlah Kursi: {mobil['jumlah_kursi']}")

        nomor = int(input("Masukkan pilihan mobil (ID): "))
        hari = int(input("Masukkan jumlah hari sewa: "))
        for mobil in data_mobil:
            if mobil["id"] == nomor:
                total1 = hari * mobil["harga"]
                jenis1 = mobil["merk"]
                print(f"Biaya peminjaman {mobil['merk']} selama {hari} hari adalah = Rp{total1:,}")
                return
        print("Pilihan tidak valid. Ulangi.")
        fungsi_mobil()

    fungsi_mobil()

    total2 = 0
    jenis2 = ''

    def fungsi_supir():
        nonlocal total2, jenis2
        print('\n---------- Pilihan Supir ----------')
        print('1. Dengan supir (jarak 10-50 Km) = Rp 350.000')
        print('2. Dengan supir (jarak 100-200 Km) = Rp 500.000')   
        print('3. Dengan supir (jarak Antar Kota) = Rp 1.000.000') 
        print('4. Tanpa Supir = Rp 0') 
        nomor = int(input('Masukkan pilihan supir (1-4): '))

        if nomor == 1:
            total2 = 350000
            jenis2 = 'dengan supir (10-50 Km)'
        elif nomor == 2:
            total2 = 500000
            jenis2 = 'dengan supir (100-200 Km)'
        elif nomor == 3:
            total2 = 1000000
            jenis2 = 'dengan supir (Antar Kota)'
        elif nomor == 4:
            total2 = 0
            jenis2 = 'tanpa supir'
        else:
            print("Pilihan tidak ada, silahkan masukkan lagi")
            fungsi_supir()

    fungsi_supir()

    total_semua = total1 + total2
    print(f'\nTotal yang harus dibayar: Rp{total_semua:,}')
    uang = int(input('Uang tunai pembeli: Rp'))
    kembalian = uang - total_semua
    print(f'Kembalian: Rp{kembalian:,}')

    print('\n---------- Struk Pembayaran ----------')
    print(f'Nama       : {peminjam}')
    print(f'Mobil      : {jenis1}')
    print(f'Supir      : {jenis2}')
    print(f'Tagihan    : Rp{total_semua:,}')
    print(f'Uang       : Rp{uang:,}')
    print(f'Kembalian  : Rp{kembalian:,}')
    print('---------- Terima Kasih ----------')


# === MENU UTAMA ===
def menu():
    while True:
        print("\n=== MENU RENTAL MOBIL ===")
        print("1. Lihat Daftar Mobil")
        print("2. Tambah Mobil")
        print("3. Update Mobil")
        print("4. Hapus Mobil")
        print("5. Pemesanan dan Pembayaran")
        print("6. Keluar")

        pilihan = input("Pilih menu (1-6): ")

        if pilihan == "1":
            tampilkan_mobil()
        elif pilihan == "2":
            tambah_mobil()
        elif pilihan == "3":
            update_mobil()
        elif pilihan == "4":
            hapus_mobil()
        elif pilihan == "5":
            menu_pembayaran()
        elif pilihan == "6":
            print("Terima kasih telah menggunakan aplikasi rental mobil!")
            break
        else:
            print("Pilihan tidak valid!")


# === EKSEKUSI PROGRAM ===
if login_admin():
    menu()
