# ScanGo : Python Self-service cashier Project

Sebuah program Kasir sederhana yang dibangun menggunakan bahasa Python dan terhubung dengan database SQLite.

## A. Latar Belakang Project
Seorang pemilik supermarket memiliki rencana untuk melakukan perbaikan proses bisnis pada supermarketnya dengan cara membuat sistem kasir yang self-service di supermarket miliknya dengan harapan :
* Customer bisa langsung memasukkan item yang dibeli, jumlah item yang dibeli, dan harga item yang dibeli dan fitur yang lain.
* Customer yang tidak berada di kota tersebut bisa membeli barang dari supermarket tersebut.

maka dibuatlah ScanGo yang merupakan program self-service cashier untuk memenuhi harapan tersebut.

## B. Feature Requirements
* Customer dapat menambahkan nama, jumlah dan harga item pada keranjang dengan <span style="background-color: #000; color: #fff; padding: 1px 3px;">tambah_item()</span>
* Mengubah item yang sudah ada di keranjang, seperti:
    - Mengubah nama item yang sudah ada pada keranjang dengan <span style="background-color: #000; color: #fff; padding: 1px 3px;">update_nama_item()</span>
    - Mengubah jumlah item yang sudah ada pada keranjang dengan <span style="background-color: #000; color: #fff; padding: 1px 3px;">update_jumlah_item()</span>
    - Mengubah harga item yang sudah ada pada keranjang dengan <span style="background-color: #000; color: #fff; padding: 1px 3px;">update_harga_item()</span>
* Menghapus item yang ada pada keranjang, seperti:
    - Menghapus salah satu item yang ada pada keranjang dengan <span style="background-color: #000; color: #fff; padding: 1px 3px;">hapus_item()</span>
    - Menghapus seluruh item yang ada pada keranjang dengan <span style="background-color: #000; color: #fff; padding: 1px 3px;">reset_transaksi()</span>
* Jika diperlukan, customer dapat mengecek keranjang belanja dengan <span style="background-color: #000; color: #fff; padding: 1px 3px;">cek_keranjang()</span>
* Jika belanja sudah selesai, customer dapat melakukan check out dengan <span style="background-color: #000; color: #fff; padding: 1px 3px;">check_out()</span>

## C. Alur Code / Flowchart
![flowchart](flowchart.jpg)
## D. Penjelasan Code yang digunakan
Program ScanGo terdiri atas 4 file yaitu 3 file modul dan satu buah file utama, file utama ini yang nantinya akan dijalankan dan berinteraksi dengan user. 

![Foto Main Menu](mainmenu.jpg)

3 modul yang disebutkan sebelumnya adalah modul <span style="background-color: #000; color: #fff; padding: 1px 3px;">transaction</span>, <span style="background-color: #000; color: #fff; padding: 1px 3px;">main_menu</span> dan <span style="background-color: #000; color: #fff; padding: 1px 3px;">database_management</span>
1. modul transaction, modul ini menyimpan method-method yang digunakan untuk membantu proses transaksi user pada saat menggunakan program ScanGo, method tersebut adalah:
    - <span style="background-color: #000; color: #fff; padding: 1px 3px;">tambah_item()</span>
    ![method tambah_item](tambahitemmtd.png)
    - <span style="background-color: #000; color: #fff; padding: 1px 3px;">update_nama_item()</span>
    ![method update_nama_item](updtnmitmmtd.jpg)
    - <span style="background-color: #000; color: #fff; padding: 1px 3px;">update_jumlah_item()</span>
    ![method update_jumlah_item](updtjmitmmtd.jpg)
    - <span style="background-color: #000; color: #fff; padding: 1px 3px;">update_harga_item()</span>
    ![method update_harga_item](updthrgitmmtd.jpg)
    - <span style="background-color: #000; color: #fff; padding: 1px 3px;">hapus_item()</span>
    ![method hapus_item](hpsitmmtd.jpg)
    - <span style="background-color: #000; color: #fff; padding: 1px 3px;">reset_transaksi()</span>
    ![method reset_transaksi](rstmtd.jpg)
    - <span style="background-color: #000; color: #fff; padding: 1px 3px;">cek_keranjang()</span>
    ![method cek_keranjang](ckkrnjgmtd.jpg)
    - <span style="background-color: #000; color: #fff; padding: 1px 3px;">check_out()</span>
    ![method check_out](cekotmtd.jpg)
    - <span style="background-color: #000; color: #fff; padding: 1px 3px;">update_dict_diskon()</span>
    ![method update_dict_diskon](updtdictmtd.jpg)

2. Modul main_menu, modul ini digunakan untuk menampilkan tampilan main menu dari program ScanGo, method yang ada di dalamnya adalah:
    - <span style="background-color: #000; color: #fff; padding: 1px 3px;">menu_greeting()</span>
    ![method menu_greeting](menugrtmtd.jpg)
    - <span style="background-color: #000; color: #fff; padding: 1px 3px;">pilih_menu()</span>
    ![method pilih_menu](pilihmnmtd.png)

3. Modul database_management, modul ini digunakan untuk menyimpan data transaksi yang telah dilakukan ke dalam database SQLite, method yang ada di dalamnya adalah:
    - <span style="background-color: #000; color: #fff; padding: 1px 3px;">import_to_database()</span>
    ![method import_to_database](importmtd.png)

## E. Test Case
Selanjutnya adalah pengujian program dengan *test case* yang sudah ditentukan.
1. Test 1 : Menambahkan item pada keranjang
![tes 1_1](tes11.jpg)
![tes 1_2](tes12.jpg)
2. Test 2 : Melakukan *delete item* dari keranjang
![tes 2_1](tes21.jpg)
3. Test 3 : Melakukan *reset transaction*
![tes 3_1](tes3.jpg)
4. Test 4 : Melakukan *check out* dari keranjang
![tes 4_1](tes41.jpg)
![tes 4_2](tes42.jpg)
## F. Kesimpulan
1. Penggunaan OOP dalam penerapan Kode
2. Menambahkan Error handling yang mungkin terjadi, karena program banyak meminta input dari user.
3. Pengembangan lainnya berdasarkan masukkan dari user.