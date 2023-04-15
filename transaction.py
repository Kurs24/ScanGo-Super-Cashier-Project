import tabulate
import database_management as db
def tambah_item():
    """
    Berikut adalah fungsi untuk menambahkan item ke Keranjang belanja User
    Returns :
        keranjang (Dict)     : Dictionary dari list belanjaan yang ada
    """
    nama_item = input("Masukkan Nama item yang diinginkan: ").capitalize()
    jumlah_item = int(input("Masukkan Jumlah item yang diinginkan: "))
    harga_per_item = float(input("Masukkan harga item yang diinginkan: "))
    print("\n")
    total_harga = jumlah_item * harga_per_item
    if type(nama_item) == str:
        if type(jumlah_item) == int and jumlah_item > 0:
            if type(harga_per_item) in (int,float) and harga_per_item > 0:
                keranjang = {"nama":str(nama_item), "jumlah":int(jumlah_item), "harga":harga_per_item, 
                             "total_harga" : total_harga}
            else:
                raise Exception("Maaf tipe data Harga tidak sesuai dengan Format")
        else:
            raise Exception("Maaf tipe data Jumlah Item tidak sesuai dengan Format")
    else:
        raise Exception("Maaf tipe data Nama Item tidak sesuai dengan Format")
    return keranjang

def update_nama_item(list_belanja, nama_item, nama_baru):
    """
    Fungsi untuk mengubah nama item yang ada dalam keranjang belanja user.

    Parameter :
        list_belanja (list) : daftar belanja user yang ada di keranjang
        nama_item (string)  : nama item pada keranjang yang akan diubah
        nama_baru (string)  : nama baru untuk item yang diubah

    Returns:
        list_belanja (list) : daftar belanja user yang ada di keranjang
    """
    if type(nama_item) == str:
        list_item = []
        for index in range(len(list_belanja)):
            list_item.append(list_belanja[index]["nama"])
            if list_belanja[index]["nama"] == nama_item:
                list_belanja[index]["nama"] = nama_baru
                print(f"Item {nama_item} telah diubah menjadi {nama_baru}!")
                break
        if nama_item not in list_item:
            print("Nama item belum ada dalam keranjang")
    else:
        raise Exception("Maaf tipe data Nama Item tidak sesuai dengan Format")
    return list_belanja

def update_jumlah_item(list_belanja, nama_item, jumlah_baru):
    """
    Fungsi untuk mengubah jumlah item yang ada dalam keranjang belanja user.

    Parameter :
        list_belanja (list) : daftar belanja user yang ada di keranjang
        nama_item (string)  : nama item pada keranjang yang akan diubah
        jumlah_baru (int)   : jumlah baru untuk item yang diubah

    Returns:
        list_belanja (list) : daftar belanja user yang ada di keranjang
    """
    if type(jumlah_baru) == int and jumlah_baru > 0:
        list_item = []
        for index in range(len(list_belanja)):
            list_item.append(list_belanja[index]["nama"])
            if list_belanja[index]["nama"] == nama_item:
                list_belanja[index]["jumlah"] = jumlah_baru
                list_belanja[index]["total_harga"] = list_belanja[index]["jumlah"] * list_belanja[index]["harga"]
                print(f"Jumlah item {nama_item} pada keranjang anda telah diubah menjadi {jumlah_baru}!")
        if nama_item not in list_item:
            print("Nama item belum ada dalam keranjang")
    else:
        raise Exception("Maaf tipe data Jumlah Item tidak sesuai dengan Format")
    return list_belanja

def update_harga_item(list_belanja, nama_item, harga_baru):
    """
    Fungsi untuk mengubah harga item yang ada dalam keranjang belanja user.

    Parameter :
        list_belanja (list) : daftar belanja user yang ada di keranjang
        nama_item (string)  : nama item pada keranjang yang akan diubah
        harga_baru (float)  : harga baru untuk item yang diubah

    Returns:
        list_belanja (list) : daftar belanja user yang ada di keranjang
    """
    if type(harga_baru) in (int,float) and harga_baru > 0:
        list_item = []
        for index in range(len(list_belanja)):
            list_item.append(list_belanja[index]["nama"])
            if list_belanja[index]["nama"] == nama_item:
                list_belanja[index]["harga"] = harga_baru
                list_belanja[index]["total_harga"] = list_belanja[index]["jumlah"] * list_belanja[index]["harga"]
                print(f"Harga item {nama_item} pada keranjang anda telah diubah menjadi Rp.{harga_baru}!")
        if nama_item not in list_item:
            print("Nama item belum ada dalam keranjang")
    else:
        raise Exception("Maaf tipe data Harga tidak sesuai dengan Format")
    return list_belanja

def hapus_item(list_belanja, nama_item):
    """
    Fungsi untuk menghapus item yang ada dalam keranjang belanja user.

    Parameter :
        list_belanja (list) : daftar belanja user yang ada di keranjang
        nama_item (string)  : nama item pada keranjang yang akan dihapus

    Returns:
        list_belanja (list) : daftar belanja user yang ada di keranjang
    """
    if type(nama_item) == str:
        list_item = []
        for index in range(len(list_belanja)):
            list_item.append(list_belanja[index]["nama"])
            if list_belanja[index]["nama"] == nama_item:
                list_belanja.pop(index)
                print(f"Item {nama_item} telah dihapus dari keranjang belanja anda!")
        if nama_item not in list_item:
            print("Nama item belum ada dalam keranjang")
    else:
        raise Exception("Maaf tipe data Nama Item tidak sesuai dengan Format")  
    return list_belanja

def reset_transaksi(list_belanja):
    """
    Fungsi yang akan menghapus seluruh item pada keranjang belanja user.

    Parameter :
        list_belanja (list) : daftar belanja user yang ada di keranjang

    Returns : 
        list_belanja (list) : daftar belanja user yang ada di keranjang
    """
    list_belanja.clear()
    return list_belanja

def cek_keranjang(list_belanja):
    """
    Fungsi untuk mengecek dan menampilkan isi keranjang user

    Parameter :
        list_belanja (list) : daftar belanja user yang ada di keranjang

    Returns : 
        list_belanja (list) : daftar belanja user yang ada di keranjang
    """
    if len(list_belanja) > 0:
        for order in list_belanja:
            order_error = 0
            for key,value in order.items():
                if value in ("", None):
                    order_error += 1
                    break
        if order_error > 0:
            print("Terdapat kesalahan input pada Keranjang anda!")
        else:
            print("Keranjang anda sudah aman :D, Berikut adalah daftar belanjaan anda!")
            header = list_belanja[0].keys()
            rows = [x.values() for x in list_belanja]
            print(tabulate.tabulate(rows, header, tablefmt='grid'))
    else:
        print("Keranjang belanja anda masih Kosong!, silahkan tambahkan item dahulu")

def check_out(list_belanja):
    """
    Fungsi untuk melakukan check out keranjang dan menampilkan diskon serta total harga dari belanjaan user,
    fungsi ini juga akan melakukan input data transaksi ke SQLite database.
    Parameter :
        list_belanja (list) : daftar belanja user yang ada di keranjang

    Returns : 
        list_belanja (list) : daftar belanja user yang ada di keranjang
    """
    total_belanja = 0
    list_diskon = []
    for index in range(len(list_belanja)):
        if list_belanja[index]["total_harga"] <= 200000:
            diskon = 0
            list_diskon.append(diskon)
        elif list_belanja[index]["total_harga"] <= 300000:
            diskon = 0.05 * list_belanja[index]["total_harga"]
            list_diskon.append(diskon)
            list_belanja[index]["total_harga"] = list_belanja[index]["total_harga"] - diskon
        elif list_belanja[index]["total_harga"] <= 500000:
            diskon = 0.06 * list_belanja[index]["total_harga"]
            list_diskon.append(diskon)
            list_belanja[index]["total_harga"] = list_belanja[index]["total_harga"] - diskon
        elif list_belanja[index]["total_harga"] > 500000:
            diskon = 0.07 * list_belanja[index]["total_harga"]
            list_diskon.append(diskon)
            list_belanja[index]["total_harga"] = list_belanja[index]["total_harga"] - diskon
        total_belanja += list_belanja[index]["total_harga"]
    update_dict_diskon(list_diskon, list_belanja)
    db.import_to_database(list_belanja)
    cek_keranjang(list_belanja)
    print(f"Total belanja anda adalah: Rp {total_belanja}")
    return list_belanja

def update_dict_diskon(list_diskon, list_belanja):
    """
    Fungsi ini digunakan untuk menyimpan potongan harga yang didapatkan user pada sesi check out
    Parameter :
        list_diskon (list)  : daftar diskon yang didapat oleh user pada sesi check out
        list_belanja (list) : daftar belanja user yang ada di keranjang

    Returns : 
        - None
    """
    indeks = 0
    for index in list_belanja:
        index.update(diskon = list_diskon[indeks])
        indeks += 1