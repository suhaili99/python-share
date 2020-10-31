walet = 0
nama = ""


def beli(kode):
    kode = kode.lower()
    if kode == "a1":
        namab = "Pulsa 5000"
        harga = 5000
        global walet   
        walet -= harga
        return "Anda telah Membeli {} dengan Harga {} sisa Saldo {}".format(namab,harga,walet)
        
    elif kode == "a2":
        namab = "Pulsa 100000"
        harga = 10000
        walet -= harga
        return "Anda telah Membeli {} dengan Harga {} sisa Saldo {}".format(namab,harga,walet)
def isiWalet(topup):
    global walet
    walet += topup
    return "'PENGISIAN WALET BERHASIL!' kamu telah mengisi walet {} sehingga walet anda sekarang {}".format(topup,walet)

def cek():
    return walet

def menu():
    print("=================================PULSA APP===========================================")
    print("Selamat Datang {} di Toko Pulsa PyShare".format(nama))
    print("Saldomu {}".format(walet))
    print("Untuk Membeli silahkan masukan Kode pembelian dibawah ini:")
    print("a1 = pulsa 5000;a2 = pulsa 100000")
    print("untuk Cek dan isi topup tinggal ketik kode d1 dan d2!")
    print("mengakhiri program tekan x")
    tombol = input("Masukan Kode Pembelian !")
    if tombol != "x" and tombol == "a1":
        hasil = beli(tombol)
        print(hasil)
        kembali = input("ingin kembali ke menu awal atau keluar? y/n")
        if kembali=="y":
            menu()
        else:
            print("anda telah keluar")
    elif tombol != "x" and tombol == "a2":
        hasil = beli(tombol)
        print(hasil)
        kembali = input("ingin kembali ke menu awal atau keluar? y/n")
        if kembali=="y":
            menu()
        else:
            print("anda telah keluar")
    elif tombol != "x" and tombol == "d1":
        isi = int(input("Isi Berapa? "))
        hasil = isiWalet(isi)
        print(hasil)
        kembali = input("ingin kembali ke menu awal atau keluar? (y/n) ")
        if kembali=="y":
            menu()
        else:
            print("anda telah keluar")
    elif tombol != "x" and tombol== "d2":
        print(cek())
        kembali = input("ingin kembali ke menu awal atau keluar? (y/n) ")
        if kembali=="y":
            menu()
        else:
            print("anda telah keluar")
    elif tombol == "x":
        print("program Berakhir")
    else :
        print("kode Salah silahkan ulang lagi !")
        return menu
    
    

nama = input("Masukan Nama mu : ")
walet = int(input("Wajib isi saldo mu : "))
if nama == "" or walet == 0:
    print("Program Keluar")
else:
    menu()

    

