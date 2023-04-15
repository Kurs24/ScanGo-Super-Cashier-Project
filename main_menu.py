import transaction
def menu_greeting():
    """
    Merupakan sebuah fungsi untuk menampilkan bagian awal dari program yang dijalankan
    """
    print(
        """
        ============================================================================================
        Selamat datang di ScanGo Self Service Cashier, silahkan pilih menu berikut untuk melanjutkan
        =============================================================================================
        1. Tambahkan item ke Keranjang
        2. Cek dan validasi isi Keranjang
        3. Edit Keranjang
        4. Hapus Item dalam Keranjang
        5. Check Out item dalam Keranjang
        6. Keluar dari Aplikasi
        """)

def pilih_menu():
    """
    Fungsi ini akan berfungsi untuk navigasi dari main menu pada aplikasi kasir ini
    """
    keranjang_belanja = []
    while True:
        choosen_menu = input("Masukkan Nomor menu yang ingin anda akses: ")
        try:
            choosen_menu = int(choosen_menu)
        except:
            print('Pilihan yang dimasukkan tidak valid harap masukkan kembali')
        if choosen_menu == 1:
            print("Anda memilih menu untuk menambahkan item ke keranjang! \n")
            daftar_item = transaction.tambah_item()
            keranjang_belanja.append(daftar_item)
        elif choosen_menu == 2:
            print("Anda memilih menu untuk mengecek item pada keranjang! \n")
            transaction.cek_keranjang(keranjang_belanja)
        elif choosen_menu == 3:
            print("Anda memilih menu untuk mengubah/mengedit item pada keranjang! \n")
            print(
            """
            1. Mengubah nama item pada keranjang
            2. Mengubah jumlah item pada keranjang
            3. Mengubah harga item pada keranjang
            """)
            pil_user = input("Masukkan Nomor yang anda pilih: ")
            try:
                pil_user = int(pil_user)
            except:
                print('Pilihan yang dimasukkan tidak valid')
            if pil_user == 1:
                print("Anda akan mengubah nama item dalam keranjang \n")
                nama_item = input("Masukkan nama item yang ingin diubah: ").capitalize()
                nama_baru = input("Masukkan nama baru dari item: ").capitalize()
                keranjang_belanja = transaction.update_nama_item(keranjang_belanja,nama_item,nama_baru)
            elif pil_user == 2:
                print("Anda akan mengubah Jumlah item dalam keranjang \n")
                nama_item = input("Masukkan nama item yang ingin diubah: ").capitalize()
                jumlah_baru = int(input("Masukkan jumlah baru dari item: "))
                keranjang_belanja = transaction.update_jumlah_item(keranjang_belanja,nama_item,jumlah_baru)
            elif pil_user == 3:
                print("Anda akan mengubah harga item dalam keranjang \n")
                nama_item = input("Masukkan nama item yang ingin diubah: ").capitalize()
                harga_baru = float(input("Masukkan harga baru dari item: "))
                keranjang_belanja = transaction.update_harga_item(keranjang_belanja,nama_item,harga_baru)
            else:
                print("Kembali ke main menu")
        elif choosen_menu == 4:
            print("Anda memilih menu untuk menghapus item pada keranjang! \n")
            print(
            """
            1. Menghapus salah satu item dalam keranjang
            2. Menghapus seleruh item dalam keranjang
            """)
            pil_user = input("Masukkan Nomor yang anda pilih: ")
            try:
                pil_user = int(pil_user)
            except:
                print('Pilihan yang dimasukkan tidak valid')
            if pil_user == 1:
                print("Anda akan menghapus salah satu item pada keranjang! \n")
                nama_item = input("Masukkan nama item yang ingin dihapus: ").capitalize()
                keranjang_belanja = transaction.hapus_item(keranjang_belanja,nama_item)
            elif pil_user == 2:
                print("Anda akan menghapus seluruh item pada keranjang! \n")
                keranjang_belanja = transaction.reset_transaksi(keranjang_belanja)
                print("Seluruh item dalam keranjang berhasil dihapus")
            else:
                print("Kembali ke main menu")
        elif choosen_menu == 5:
            print("Anda memilih menu untuk melakukan checkout item pada keranjang! \n")
            transaction.check_out(keranjang_belanja)
        elif choosen_menu == 6:
            print('Terima Kasih telah berbelanja di Super Self Service Cashier')
            break