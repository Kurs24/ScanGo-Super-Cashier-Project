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
![flowchart](https://user-images.githubusercontent.com/92706710/232246658-12c31f03-5f5f-4c09-81ec-c28139774cdb.jpg)
## D. Penjelasan Code yang digunakan
Program ScanGo terdiri atas 4 file yaitu 3 file modul dan satu buah file utama, file utama ini yang nantinya akan dijalankan dan berinteraksi dengan user. 

![mainmenu](https://user-images.githubusercontent.com/92706710/232246681-b866c7b0-849b-42f6-a098-86bb7f99fafb.jpg)

3 modul yang disebutkan sebelumnya adalah modul <span style="background-color: #000; color: #fff; padding: 1px 3px;">transaction</span>, <span style="background-color: #000; color: #fff; padding: 1px 3px;">main_menu</span> dan <span style="background-color: #000; color: #fff; padding: 1px 3px;">database_management</span>
1. modul transaction, modul ini menyimpan method-method yang digunakan untuk membantu proses transaksi user pada saat menggunakan program ScanGo, method tersebut adalah:
    - <span style="background-color: #000; color: #fff; padding: 1px 3px;">tambah_item()</span>
    ![tambahitemmtd](https://user-images.githubusercontent.com/92706710/232246698-e5b30387-40ce-4418-9e90-3c6555234e63.png)
    - <span style="background-color: #000; color: #fff; padding: 1px 3px;">update_nama_item()</span>
    ![updtnmitmmtd](https://user-images.githubusercontent.com/92706710/232246715-72be4b3e-a51f-47e2-a2e5-a33b763a0a88.jpg)
    - <span style="background-color: #000; color: #fff; padding: 1px 3px;">update_jumlah_item()</span>
    ![updtjmitmmtd](https://user-images.githubusercontent.com/92706710/232246754-d7c9a586-8c17-408c-be7c-31c4ba843778.jpg)
    - <span style="background-color: #000; color: #fff; padding: 1px 3px;">update_harga_item()</span>
    ![updthrgitmmtd](https://user-images.githubusercontent.com/92706710/232246772-dbb6435a-92bf-40cf-9077-04b156d607c9.jpg)
    - <span style="background-color: #000; color: #fff; padding: 1px 3px;">hapus_item()</span>
    ![hpsitmmtd](https://user-images.githubusercontent.com/92706710/232246786-253c5c08-c15f-41e1-b539-ea03fe533ca9.jpg)
    - <span style="background-color: #000; color: #fff; padding: 1px 3px;">reset_transaksi()</span>
    ![rstmtd](https://user-images.githubusercontent.com/92706710/232246801-6621bcb5-1e1d-45e1-abf2-bb55f6feed6f.jpg)
    - <span style="background-color: #000; color: #fff; padding: 1px 3px;">cek_keranjang()</span>
    ![ckkrnjgmtd](https://user-images.githubusercontent.com/92706710/232246822-6a0c5b8c-5818-46d0-9a8f-2f63721b829c.jpg)
    - <span style="background-color: #000; color: #fff; padding: 1px 3px;">check_out()</span>
    ![cekotmtd](https://user-images.githubusercontent.com/92706710/232246838-e9b1889a-395a-4c54-a9a5-89817b7d7355.jpg)
    - <span style="background-color: #000; color: #fff; padding: 1px 3px;">update_dict_diskon()</span>
    ![updtdictmtd](https://user-images.githubusercontent.com/92706710/232246861-dc0857d4-0668-4643-bdf5-9f97cfedd2d6.jpg)

2. Modul main_menu, modul ini digunakan untuk menampilkan tampilan main menu dari program ScanGo, method yang ada di dalamnya adalah:
    - <span style="background-color: #000; color: #fff; padding: 1px 3px;">menu_greeting()</span>
    ![menugrtmtd](https://user-images.githubusercontent.com/92706710/232246876-c0dbf6c2-a01e-4037-b345-b43fbc33d555.jpg)
    - <span style="background-color: #000; color: #fff; padding: 1px 3px;">pilih_menu()</span>
    ![pilihmnmtd](https://user-images.githubusercontent.com/92706710/232246889-5c621f94-9d93-4c0a-b2e4-0a997ea2fcab.png)

3. Modul database_management, modul ini digunakan untuk menyimpan data transaksi yang telah dilakukan ke dalam database SQLite, method yang ada di dalamnya adalah:
    - <span style="background-color: #000; color: #fff; padding: 1px 3px;">import_to_database()</span>
    ![importmtd](https://user-images.githubusercontent.com/92706710/232246904-53de89af-1b9e-4a5c-983d-95341490fa61.png)

## E. Test Case
Selanjutnya adalah pengujian program dengan *test case* yang sudah ditentukan.
1. Test 1 : Menambahkan item pada keranjang
![tes11](https://user-images.githubusercontent.com/92706710/232246936-d9e51c43-3cb2-4e81-8e0b-579a5d2a4035.jpg)
![tes12](https://user-images.githubusercontent.com/92706710/232246930-2f42f82b-d9be-4955-8ca0-2ff2976305e7.jpg)
2. Test 2 : Melakukan *delete item* dari keranjang
![tes21](https://user-images.githubusercontent.com/92706710/232246960-b659d8fe-563a-4e3a-9c68-f877fa685dfa.jpg)
3. Test 3 : Melakukan *reset transaction*
![tes3](https://user-images.githubusercontent.com/92706710/232246918-e6c730ad-33a0-4417-b164-df580ae22e49.jpg)
4. Test 4 : Melakukan *check out* dari keranjang
![tes41](https://user-images.githubusercontent.com/92706710/232246962-a97f9539-842e-492d-abb6-7669a37e534f.jpg)
![tes42](https://user-images.githubusercontent.com/92706710/232246966-c9e4a762-3bad-407e-8bee-0b4fedf91733.jpg)
## F. Kesimpulan
1. Penggunaan OOP dalam penerapan Kode
2. Menambahkan Error handling yang mungkin terjadi, karena program banyak meminta input dari user.
3. Pengembangan lainnya berdasarkan masukkan dari user.