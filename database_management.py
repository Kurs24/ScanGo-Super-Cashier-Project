def import_to_database(list_belanja):
    """
    Fungsi yang digunakan untuk melakukan import data hasil transaksi ke dalam database SQLite

    Parameter:
        list_belanja (list) : daftar belanja user yang ada di keranjang
    
    Return:
        - None
    """
    import sqlite3
    con = sqlite3.connect('data_transaksi.db')
    cur = con.cursor()

    ## Membuat tabel transaksi
    cur.execute('''CREATE TABLE IF NOT EXISTS transaksi(
    no_id integer PRIMARY KEY AUTOINCREMENT,
    nama_item varchar(100),
    jumlah_item integer,
    harga float,
    total_harga float,
    diskon float,
    harga_diskon float)''')

    ## Melakukan insert data ke Tabel transaksi
    for row in list_belanja:
        cur.execute('''INSERT INTO transaksi (nama_item, jumlah_item, harga, total_harga, diskon, harga_diskon) VALUES(?, ?, ?, ?, ?, ?)''',
                    (row['nama'], row['jumlah'], row['harga'], row['jumlah']*row['harga'], row['diskon'], row['total_harga']))
        
    
    ## Menyimpan perubahan pada database
    con.commit()

    ## Menutup koneksi ke database
    cur.close()
    con.close()
    