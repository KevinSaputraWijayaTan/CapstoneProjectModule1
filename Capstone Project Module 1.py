# Capstone Project Module 1
# Case Study: Gudang (Data Stok)

from prettytable import PrettyTable

Stok_Barang = {
    'Sofa':['TOP001', 'Impor', 300, 'Rp 3.000.000'],
    'Kasur':['TOP002', 'Lokal', 150, 'Rp 5.000.000'],
    'Lemari':['TOP003', 'Impor', 200, 'Rp 8.000.000'],
    'Meja':['TOP004', 'Impor', 400, 'Rp 4.000.000'],
    'Kursi':['TOP005', 'Lokal', 500, 'Rp 2.000.000']
}

def main_menu () :
    print('''
    ========= Selamat Datang di Pergudangan Toko Octo Prompto ==========
    
    List Menu:
    
    1. Menampilkan Barang di Stok Gudang
    2. Menambah Barang di Stok Gudang
    3. Memperbarui Barang di Stok Gudang
    4. Menghapus Barang di Stok Gudang
    5. Keluar dari Program
    ''')

def seluruh_barang () :
    print('\nBerikut Ini List Barang di Stok Gudang')
    tabel_keseluruhan = PrettyTable(['Kode', 'Jenis', 'Kategori', 'Qty', 'Harga'])
    for i in Stok_Barang :
        tabel_keseluruhan.add_row([Stok_Barang[i][0], i, Stok_Barang[i][1], Stok_Barang[i][2], Stok_Barang[i][3]])
    print(tabel_keseluruhan)

def filter_barang () :
    print('\nBerikut Ini List Barang di Stok Gudang Berdasarkan Kategori')

    print('\nBarang Impor:')
    tabel_impor = PrettyTable(['Kode', 'Jenis', 'Kategori', 'Qty', 'Harga'])
    for i in Stok_Barang :
        if Stok_Barang[i][1] == 'Impor' :
            tabel_impor.add_row([Stok_Barang[i][0], i, Stok_Barang[i][1], Stok_Barang[i][2], Stok_Barang[i][3]])
    print(tabel_impor)

    print('\nBarang Lokal:')
    tabel_lokal = PrettyTable(['Kode', 'Jenis', 'Kategori', 'Qty', 'Harga'])
    for i in Stok_Barang :
        if Stok_Barang[i][1] == 'Lokal' :
            tabel_lokal.add_row([Stok_Barang[i][0], i, Stok_Barang[i][1], Stok_Barang[i][2], Stok_Barang[i][3]])
    print(tabel_lokal)

def tambah_barang () :
    print('\nMasukkan Input untuk Barang yang Ingin Ditambah\n')
    new_kode = str(input('Masukkan Kode Barang Baru: '))
    new_jenis = str(input('Masukkan Jenis Barang Baru: '))
    new_kategori = str(input('Masukkan Kategori Barang Baru: '))
    new_qty = int(input('Masukkan Jumlah Barang Baru: '))
    new_harga = str(input('Masukkan Harga Barang Baru: '))
    Stok_Barang[new_jenis] = new_kode, new_kategori, new_qty, new_harga
    print('\nBarang Telah Ditambah ke Dalam Stok Gudang.')
    seluruh_barang ()
    
def update_barang () :
    print('\nMasukkan Input untuk Barang yang Ingin Diupdate\n')
    seleksi_barang = str(input('Masukkan Jenis Barang yang Ingin Diupdate: ')).capitalize()
    if seleksi_barang in Stok_Barang :
         while True:
              sub_menu2 = int(input('''
    1. Ubah Kode Barang
    2. Ubah Jenis Barang
    3. Ubah Kategori Barang
    4. Ubah Jumlah Barang
    5. Ubah Harga Barang
    6. Mutasi Stok Barang Masuk
    7. Mutasi Stok Barang Keluar
    8. Kembali ke Menu Utama
    
    Masukkan Input yang Anda Inginkan untuk Sub-Menu Berikut: '''))
              
              if sub_menu2 == 1 :
                ubah_kode = str(input('\nMasukkan Kode Barang Setelah Diupdate: '))
                Stok_Barang[seleksi_barang][0] = ubah_kode
                print('\nKode Barang Berhasil Diupdate!')
                seluruh_barang ()
                break
              
              if sub_menu2 == 2 :
                ubah_jenis = str(input('\nMasukkan Jenis Barang Setelah Diupdate: '))
                Stok_Barang[ubah_jenis] = Stok_Barang.pop(seleksi_barang)
                print('\nJenis Barang Berhasil Diupdate!')
                seluruh_barang ()
                break
              
              if sub_menu2 == 3 :
                ubah_kategori = str(input('\nMasukkan Kategori Barang Setelah Diupdate: '))
                Stok_Barang[seleksi_barang][1] = ubah_kategori
                print('\nKategori Barang Berhasil Diupdate!')
                seluruh_barang ()
                break
              
              if sub_menu2 == 4 :
                ubah_jumlah = int(input('\nMasukkan Jumlah Barang Setelah Diupdate: '))
                Stok_Barang[seleksi_barang][2] = ubah_jumlah
                print('\nJumlah Barang Berhasil Diupdate!')
                seluruh_barang ()
                break
              
              if sub_menu2 == 5 :
                ubah_harga = str(input('\nMasukkan Harga Barang Setelah Diupdate: '))
                Stok_Barang[seleksi_barang][3] = ubah_harga
                print('\nHarga Barang Berhasil Diupdate!')
                seluruh_barang ()
                break
              
              if sub_menu2 == 6 :
                mutasi_masuk = int(input('\nMasukkan Jumlah Barang Masuk: '))
                update_jumlah = int(Stok_Barang[seleksi_barang][2]) + mutasi_masuk
                Stok_Barang[seleksi_barang][2] = update_jumlah
                print('\nMutasi Stok Barang Masuk Berhasil Diupdate!')
                seluruh_barang ()
                break
            
              if sub_menu2 == 7 :
                mutasi_keluar = int(input('\nMasukkan Jumlah Barang Keluar: '))
                update_jumlah = int(Stok_Barang[seleksi_barang][2]) - mutasi_keluar
                Stok_Barang[seleksi_barang][2] = update_jumlah
                print('\nMutasi Stok Barang Keluar Berhasil Diupdate!')
                seluruh_barang ()
                break
              
              if sub_menu2 == 8 :
                break
              
              else:
                print ('\n    Input Invalid. Masukkan Input yang Benar.')

def hapus_barang () :
    print('\nMasukkan Input untuk Barang yang Ingin Dihapus\n')
    seleksi_barang = str(input('Masukkan Jenis Barang yang Ingin Dihapus: '))
    del Stok_Barang[seleksi_barang]
    print('\nBarang Telah Dihapus dari Stok Gudang.')
    seluruh_barang ()

def keluar_program () :
    print('\nTerima Kasih Telah Berkunjung ke Pergudangan Toko Octo Prompto! Sampai Jumpa Kembali!')



# App Start
while True:
    main_menu ()
    menu = int(input('    Masukkan Input yang Anda Inginkan untuk Menu Berikut: '))

    if menu == 1 :
        while True:
            sub_menu1 = int(input('''
    1. Tampilkan Seluruh List Barang di Stok Gudang
    2. Tampilkan List Barang di Stok Gudang Berdasarkan Kategori
    3. Kembali ke Menu Utama
            
    Masukkan Input yang Anda Inginkan untuk Sub-Menu Berikut: '''))
            
            if sub_menu1 == 1 :
                seluruh_barang ()
                continue

            elif sub_menu1 == 2 :
                filter_barang ()
                continue

            elif sub_menu1 == 3 :
                break

            else :
                print ('\n    Input Invalid. Masukkan Input yang Benar.')
    
    elif menu == 2 :
        tambah_barang ()
    
    elif menu == 3 :
        update_barang ()
    
    elif menu == 4 :
        hapus_barang ()
    
    elif menu == 5 :
        keluar_program ()
        break

    else :
        print ('\n    Input Invalid. Masukkan Input yang Benar.')