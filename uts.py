# Program Kasir Warung Kopi (Mencakup Materi Pertemuan 1 - 7)

# Pertemuan 7: Struktur Data Dictionary untuk daftar menu
daftar_menu = {
    "K01": {"nama": "Kopi Hitam", "harga": 10000},
    "K02": {"nama": "Es Kopi Susu", "harga": 15000},
    "K03": {"nama": "Teh Tarik", "harga": 12000},
    "M01": {"nama": "Roti Bakar", "harga": 18000},
    "M02": {"nama": "Kentang Goreng", "harga": 15000}
}

# Pertemuan 6: Struktur Data List untuk menampung keranjang belanja
keranjang = []

print("=" * 45)
print("        PROGRAM KASIR WARUNG KOPI")
print("=" * 45)

# Pertemuan 3: Input & Manipulasi String
nama_pelanggan = input("Masukkan Nama Pelanggan: ").strip().title()

# Pertemuan 5: Perulangan while untuk input transaksi berulang
while True:
    print("\n--- DAFTAR MENU ---")
    # Perulangan for untuk menampilkan isi dictionary
    for kode, info in daftar_menu.items():
        print(f"{kode} | {info['nama']:<15} | Rp {info['harga']:,}")
    print("-" * 45)

    kode_pilih = input("Masukkan Kode Menu (atau ketik 'SELESAI'): ").strip().upper()

    # Pertemuan 4: Percabangan untuk mengecek kondisi keluar atau validasi menu
    if kode_pilih == "SELESAI":
        break
    elif kode_pilih in daftar_menu:
        # Pertemuan 2: Konversi tipe data (str ke int) dan operator aritmatika
        jumlah = int(input(f"Jumlah beli {daftar_menu[kode_pilih]['nama']}: "))
        
        if jumlah > 0:
            nama_item = daftar_menu[kode_pilih]["nama"]
            harga_satuan = daftar_menu[kode_pilih]["harga"]
            subtotal = harga_satuan * jumlah

            # Menyimpan item ke dalam list keranjang dalam bentuk dictionary
            keranjang.append({
                "nama": nama_item,
                "harga": harga_satuan,
                "jumlah": jumlah,
                "subtotal": subtotal
            })
            print(f"-> Berhasil menambahkan {jumlah}x {nama_item}")
        else:
            print("-> Jumlah beli harus lebih dari 0!")
    else:
        print("-> Kode menu tidak ditemukan, silakan coba lagi.")

# Perhitungan Akhir & Cetak Struk
print("\n" + "=" * 45)
print(f"STRUK PEMBAYARAN - Pelanggan: {nama_pelanggan}")
print("=" * 45)

if len(keranjang) == 0:
    print("Tidak ada transaksi yang dilakukan.")
else:
    total_belanja = 0
    for item in keranjang:
        print(f"{item['nama']:<15} x{item['jumlah']:<3} : Rp {item['subtotal']:,}")
        total_belanja += item["subtotal"]  # Pertemuan 2: Shorthand operator (+=)

    # Pertemuan 4 & 2: Percabangan dan operator perbandingan untuk diskon
    if total_belanja >= 50000:
        diskon = int(total_belanja * 0.10)  # Diskon 10%
    else:
        diskon = 0

    total_bayar = total_belanja - diskon

    print("-" * 45)
    print(f"Total Belanja : Rp {total_belanja:,}")
    print(f"Diskon (10%)  : Rp {diskon:,}")
    print(f"Total Bayar   : Rp {total_bayar:,}")
    print("=" * 45)

    # Input pembayaran & hitung kembalian
    while True:
        uang_bayar = int(input("Masukkan Uang Pembayaran: Rp "))
        if uang_bayar >= total_bayar:
            kembalian = uang_bayar - total_bayar
            print(f"Kembalian     : Rp {kembalian:,}")
            print("Terima kasih telah berbelanja!")
            break
        else:
            kurang = total_bayar - uang_bayar
            print(f"Uang kurang Rp {kurang:,}. Silakan masukkan nominal yang cukup.")
