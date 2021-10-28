#Nama    : Amanda Chairunnisa
#NIM     : 2004625
#Project : UTS PBO

class bank :
    def __init__(self, saldoumum, saldotab, nominal):
        self.saldoumum = saldoumum
        self.saldotab = saldotab
        self.nominal = nominal

    def printname(self):
        print(self.saldoumum)
        print(self.saldotab)
        print(self.nominal)

    def menu(self):
        print ("Selamat Datang")

    def info(self):
        print ("Aplikasi Pencatatan Uang Digital")
        

class transaksi(bank) :
    def __init__(self, saldoumum, saldotab, nominal):
        bank().__init__(saldoumum, saldotab, nominal)
        self.saldoumum = 0
        self.saldotab = 0

    def menu(self):
        print(" 1. Informasi Saldo")
        print(" 2. Tambah Saldo ")
        print(" 3. Ambil Saldo ")
        print(" 0. Keluar ")

    def info(self):
        print("Saldo Umum Anda Saat ini Berjumlah ", self.saldoumum)
        print("Saldo Tabungan Anda Saat ini Berjumlah ", self.saldotab)

    def tambah1(self, nominal):
        self.nominal = nominal
        self.saldoumum = self.saldoumum + self.nominal
        
        print ("Transaksi Berhasil!")
        print ("Saldo Umum Anda Saat Ini Berjumlah : Rp. ", self.saldoumum)

    def tambah2(self, nominal):
        self.nominal = nominal
        self.saldotab = self.saldotab + self.nominal

        print ("Transaksi Berhasil!")
        print ("Saldo Tabungan Anda Saat Ini Berjumlah : Rp. ", self.saldotab)

    def ambil1(self, nominal):
        self.nominal = nominal
        if self.nominal > self.saldoumum: 
            print ("Maaf Saldo Anda tidak Mencukupi!")

        else:
            self.saldoumum = self.saldoumum - self.nominal
            print ("Transaksi Berhasil!")
            print ("Saldo Tabungan Anda Saat Ini Berjumlah : Rp. ", self.saldoumum)

    def ambil2 (self, nominal):
        self.nominal = nominal
        if self.nominal > self.saldotab:
            print ("Maaf Saldo Tabungan Anda tidak Mencukupi!")

        else:
            self.saldotab = self.saldotab - self.nominal
            print ("Transaksi Berhasil!")
            print ("Saldo Tabungan Anda Saat Ini Berjumlah : Rp. ", self.saldotab)

    def keluar(self):
        print ("Terimakasih Atas Kunjungannya:))")

    
    object_bank = bank()
    object_transaksi = bank()

    object_bank.menu()
    object_bank.info()
    object_transaksi.menu()
    option=int(input("Silahkan Pilih menu : "))
    if option==1:
            object_transaksi.info()
    elif option==2:
            print("1. Saldo Umum")
            print("2. Saldo Tabungan")
            option2=int(input("Pilih Penyimpanan : "))
            if option2==1:
                self.nominal=int(input("Masukan Nominal :"))
                object_transaksi.tambah1()
            elif option2==2:
                self.nominal=int(input("Masukan Nominal :"))
                object_transaksi.tambah2()
            else:
                print("Transaksi Gagal! Silahkan Melakukan Transaksi Ulang!")
    elif option==3:
            object_transaksi.info()
            print("1. Saldo Umum")
            print("2. Saldo Tabungan")
            option3=int(input("Pilih Penyimpanan : "))
            if option3==1:
                self.nominal=int(input("Masukan Nominal :"))
                object_transaksi.ambil1()
            elif option3==2:
                self.nominal=int(input("Masukan Nominal :"))
                object_transaksi.ambil2()
            else:
                print("Transaksi Gagal! Silahkan Melakukan Transaksi Ulang!")
    elif option==4:
            object_transaksi.keluar()

        

