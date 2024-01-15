print("======================== THE SOUND PROJECT FESTIVAL =========================\n")
print("     DAY 1                    DAY 2                           DAY 3")
print("- ALI                     - BANDA NEIRA                  - DONGKER")
print("- D'MASIV                 - KELOMPOK PENERBANG ROKET     - HIVI")
print("- HINDIA                  - MAHALINI                     - IDGITAF")
print("- MALIQ & D'ESSENTIAL     - PARADE HUJAN                 - J ROCKS")
print("- MORFEM                  - UNGU                         - WALI")
print("- VIERRATALLE             - REALITY CLUB                 - PEE WEE GASKINS")
print("- RUMAH SAKIT             - THE CHANGCHUTERS             - PERUNGGU")
print("- STAND HERE ALONE        - THE PANTURAS                 - SORE\n")

def jadwal_day123():
    print("     DAY 1                    DAY 2                           DAY 3")
    print("- ALI                     - BANDA NEIRA                  - DONGKER")
    print("- D'MASIV                 - KELOMPOK PENERBANG ROKET     - HIVI")
    print("- HINDIA                  - MAHALINI                     - IDGITAF")
    print("- MALIQ & D'ESSENTIAL     - PARADE HUJAN                 - J ROCKS")
    print("- MORFEM                  - UNGU                         - WALI")
    print("- VIERRATALLE             - REALITY CLUB                 - PEE WEE GASKINS")
    print("- RUMAH SAKIT             - THE CHANGCHUTERS             - PERUNGGU")
    print("- STAND HERE ALONE        - THE PANTURAS                 - SORE\n")

def jadwal_12():
    print("     DAY 1                    DAY 2             ")
    print("- ALI                     - BANDA NEIRA               ")
    print("- D'MASIV                 - KELOMPOK PENERBANG ROKET  ")
    print("- HINDIA                  - MAHALINI                  ")
    print("- MALIQ & D'ESSENTIAL     - PARADE HUJAN              ")
    print("- MORFEM                  - UNGU                      ")
    print("- VIERRATALLE             - REALITY CLUB              ")
    print("- RUMAH SAKIT             - THE CHANGCHUTERS          ")
    print("- STAND HERE ALONE        - THE PANTURAS            \n")
    
def jadwal_13():
    print("     DAY 1                     DAY 3")
    print("- ALI                     - DONGKER")
    print("- D'MASIV                 - HIVI")
    print("- HINDIA                  - IDGITAF")
    print("- MALIQ & D'ESSENTIAL     - J ROCKS")
    print("- MORFEM                  - WALI")
    print("- VIERRATALLE             - PEE WEE GASKINS")
    print("- RUMAH SAKIT             - PERUNGGU")
    print("- STAND HERE ALONE        - SORE\n")

def jadwal_23():
    print("    DAY 2                           DAY 3")
    print("- BANDA NEIRA                  - DONGKER")
    print("- KELOMPOK PENERBANG ROKET     - HIVI")
    print("- MAHALINI                     - IDGITAF")
    print("- PARADE HUJAN                 - J ROCKS")
    print("- UNGU                         - WALI")
    print("- REALITY CLUB                 - PEE WEE GASKINS")
    print("- THE CHANGCHUTERS             - PERUNGGU")
    print("- THE PANTURAS                 - SORE\n")

def jadwal1():
    print("     DAY 1                ")
    print("- ALI                     ")
    print("- D'MASIV                 ")
    print("- HINDIA                  ")
    print("- MALIQ & D'ESSENTIAL     ")
    print("- MORFEM                  ")
    print("- VIERRATALLE             ")
    print("- RUMAH SAKIT             ")
    print("- STAND HERE ALONE      \n")

def jadwal2():
    print("     DAY 2                  ")
    print("- BANDA NEIRA               ")
    print("- KELOMPOK PENERBANG ROKET  ")
    print("- MAHALINI                  ")
    print("- PARADE HUJAN              ")
    print("- UNGU                      ")
    print("- REALITY CLUB              ")
    print("- THE CHANGCHUTERS          ")
    print("- THE PANTURAS            \n")

def jadwal3():
    print("     DAY 3")
    print("- DONGKER")
    print("- HIVI")
    print("- IDGITAF")
    print("- J ROCKS")
    print("- WALI")
    print("- PEE WEE GASKINS")
    print("- PERUNGGU")
    print("- SORE\n")
    

print("=======================DENAH=================================================\n")

denah = """
Alamat : Jalan Muhammad Faiz No.28 

            ___________________________________
            |                                  |
            |               STAGE              |
            |__________________________________|

    _______________    ______________      _______________
    |             |    |             |    |              |
    |      R      |    |     VIP     |    |      R       |
    |      E      |    |_____________|    |      E       |
    |      G      |                       |      G       |
    |      U      |_______________________|      U       |
    |      L                                     L       |
    |      E               REGULER               E       |
    |      R                                     R       |
    |____________________________________________________|
"""
print(denah)

totaltiket = 0
totalharga = 0

nama = input("Nama Pembeli : ")
while True:
    x = 0
    y = 0

    def total():
        bayar = x*y
        print("Jumlah Tiket :", x)
        print("Total Harga Tiket :", bayar)

    print("JENIS TICKET")
    print("1. REGULER")
    print("2. VIP")
    print("3. KELUAR\n")
    a = input("PILIH JENIS TICKET YANG INGIN DIBELI : ")
    if a == "1" :
        keterangan = "REGULER"
        print("1. MULTI DAY PASS")
        print("2. ONE DAY PASS")
        b = input("SILAHKAN PILIH JENIS REGULER TICKET : ")
        if b == "1" :
            print("1. MULTI DAY THREE DAYS")
            print("2. MULTI DAY TWO DAYS")
            c = input("SILAHKAN PILIH JENIS MULTI DAY REGULER TICKET : ")
            if c == "1" :
                jadwal_day123()
                print("HARGA = 450.000 ")
                harga = 450000
                e = int(input("INGIN PESAN BERAPA TICKET ? "))
                x = x + e
                y = y + harga
                total()

            elif c == "2" : 
                print("1. DAY 1 AND DAY 2")
                print("2. DAY 1 AND DAY 3")
                print("3. DAY 2 AND DAY 3")
                e = input("SILAHKAN PILIH TICKET DARI MULTI DAYS TWO DAYS : ")
                if e == "1" :
                    jadwal_12()
                    print("HARGA = 300.000 ")
                    harga = 300000
                    e = int(input("INGIN PESAN BERAPA TICKET ? "))
                    x = x + e
                    y = y + harga
                    total()

                elif e == "2" :
                    jadwal_13()
                    print("HARGA = 300.000 ")
                    harga = 300000
                    e = int(input("INGIN PESAN BERAPA TICKET ? "))
                    x = x + e
                    y = y + harga
                    total()

                elif e == "3" :
                    jadwal_23()
                    print("HARGA = 300.000 ")
                    harga = 300000
                    e = int(input("INGIN PESAN BERAPA TICKET ? "))
                    x = x + e
                    y = y + harga
                    total()
                else:
                    print("PILIHAN TIDAK TERSEDIA")
                    continue
            else:
                print("PILIHAN TIDAK TERSEDIA")
                continue

                    
        elif b == "2" :
            keterangan = "VIP"
            print("1. DAY 1")
            print("2. DAY 2")
            print("3. DAY 3")    
            c = input("PILIH TICKET DAY BERAPA (1/2/3) ? ")      
            if c == "1" :
                jadwal1()
                print("HARGA = 150.000 ")
                harga = 150000
                e = int(input("INGIN PESAN BERAPA TICKET ? "))
                x = x + e
                y = y + harga
                total()

            elif c == "2" : 
                jadwal2()
                print("HARGA = 150.000 ")
                harga = 150000
                e = int(input("INGIN PESAN BERAPA TICKET ? "))
                x = x + e
                y = y + harga
                total()

            elif c == "3" :
                jadwal3()
                print("HARGA = 150.000 ")
                harga = 150000
                e = int(input("INGIN PESAN BERAPA TICKET ? "))
                x = x + e
                y = y + harga
                total()
            else:
                print("PILIHAN TIDAK TERSEDIA")
                continue
        else:
            print("PILIHAN TIDAK TERSEDIA")
            continue
        
    elif a == "2" :
        print("1. VIP SEAT ONLY")
        print("2. VIP SEAT + BACK STAGE ACCESS")
        b = input("SILAHKAN PILIH JENIS VIP TICKET : ")
        if b == "1" :
            print("1. MULTI DAY PASS")
            print("2. ONE DAY PASS")
            c = input("SILAHKAN PILIH JENIS VIP SEAT ONLY TICKET : ")
            if c == "1" :
                print("1. MULTI DAY THREE DAYS")
                print("2. MULTI DAY TWO DAYS")
                d = input("SILAHKAN PILIH JENIS MULTI DAY VIP TICKET : ")
                if d == "1" :
                    jadwal_day123()
                    print("HARGA = 750.000 ")
                    harga = 750000
                    e = int(input("INGIN PESAN BERAPA TICKET ? "))
                    x = x + e
                    y = y + harga
                    total()

                elif d == "2" : 
                    print("1. DAY 1 AND DAY 2")
                    print("2. DAY 1 AND DAY 3")
                    print("3. DAY 2 AND DAY 3")
                    f = input("SILAHKAN PILIH TICKET DARI MULTI DAYS TWO DAYS : ")
                    if f == "1" :
                        jadwal_12()
                        print("HARGA = 500.000 ")
                        harga = 500000
                        e = int(input("INGIN PESAN BERAPA TICKET ? "))
                        x = x + e
                        y = y + harga
                        total()

                    elif f == "2" :
                        jadwal_13()
                        print("HARGA = 500.000 ")
                        harga = 500000
                        e = int(input("INGIN PESAN BERAPA TICKET ? "))
                        x = x + e
                        y = y + harga
                        total()

                    elif f == "3" :
                        jadwal_23()
                        print("HARGA = 500.000 ")
                        harga = 500000
                        e = int(input("INGIN PESAN BERAPA TICKET ? "))
                        x = x + e
                        y = y + harga
                        total()
                    else:
                        print("PILIHAN TIDAK TERSEDIA")
                        continue
                else:
                    print("PILIHAN TIDAK TERSEDIA")
                    continue
                        
            elif c == "2" :
                print("1. DAY 1")
                print("2. DAY 2")
                print("3. DAY 3")    
                d = input("PILIH TICKET DAY BERAPA (1/2/3) ? ")      
                if d == "1" :
                    jadwal1()
                    print("HARGA = 250.000 ")
                    harga = 250000
                    e = int(input("INGIN PESAN BERAPA TICKET ? "))
                    x = x + e
                    y = y + harga
                    total()

                elif d == "2" : 
                    jadwal2()
                    print("HARGA = 250.000 ")
                    harga = 250000
                    e = int(input("INGIN PESAN BERAPA TICKET ? "))
                    x = x + e
                    y = y + harga
                    total()

                elif d == "3" :
                    jadwal3()
                    print("HARGA = 250.000 ")
                    harga = 250000
                    e = int(input("INGIN PESAN BERAPA TICKET ? "))
                    x = x + e
                    y = y + harga
                    total()
                else:
                    print("PILIHAN TIDAK TERSEDIA")
                    continue
            else:
                print("PILIHAN TIDAK TERSEDIA")
                continue

        if b == "2" :
            print("1. MULTI DAY PASS")
            print("2. ONE DAY PASS")
            c = input("SILAHKAN PILIH JENIS VIP SEAT + BACKSTAGE : ")
            if c == "1" :
                print("1. MULTI DAY THREE DAYS")
                print("2. MULTI DAY TWO DAYS")
                d = input("SILAHKAN PILIH JENIS MULTI DAY VIP TICKET : ")
                if d == "1" :
                    jadwal_day123()
                    print("HARGA = 1.050.000 ")
                    harga = 1050000
                    e = int(input("INGIN PESAN BERAPA TICKET ? "))
                    x = x + e
                    y = y + harga
                    total()

                elif d == "2" : 
                    print("1. DAY 1 AND DAY 2")
                    print("2. DAY 1 AND DAY 3")
                    print("3. DAY 2 AND DAY 3")
                    f = input("SILAHKAN PILIH TICKET DARI MULTI DAYS TWO DAYS : ")
                    if f == "1" :
                        jadwal_12()
                        print("HARGA = 750.000 ")
                        harga = 750000
                        e = int(input("INGIN PESAN BERAPA TICKET ? "))
                        x = x + e
                        y = y + harga
                        total()

                    elif f == "2" :
                        jadwal_13()
                        print("HARGA = 750.000 ")
                        harga = 750000
                        e = int(input("INGIN PESAN BERAPA TICKET ? "))
                        x = x + e
                        y = y + harga
                        total()

                    elif f == "3" :
                        jadwal_23()
                        print("HARGA = 750.000 ")
                        harga = 750000
                        e = int(input("INGIN PESAN BERAPA TICKET ? "))
                        x = x + e
                        y = y + harga
                        total()
                    
                    else:
                        print("PILIHAN TIDAK TERSEDIA")
                        continue
                else:
                    print("PILIHAN TIDAK TERSEDIA")
                    continue
                        
            elif c == "2" :
                print("1. DAY 1")
                print("2. DAY 2")
                print("3. DAY 3")    
                d = input("PILIH TICKET DAY BERAPA (1/2/3) ? ")      
                if d == "1" :
                    jadwal1()
                    print("HARGA = 350.000 ")
                    harga = 350000
                    e = int(input("INGIN PESAN BERAPA TICKET ? "))
                    x = x + e
                    y = y + harga
                    total()
                    
                elif d == "2" : 
                    jadwal2()
                    print("HARGA = 350.000 ")
                    harga = 350000
                    e = int(input("INGIN PESAN BERAPA TICKET ? "))
                    x = x + e
                    y = y + harga
                    total()

                elif d == "3" :
                    jadwal3()
                    print("HARGA = 350.000 ")
                    harga = 350000
                    e = int(input("INGIN PESAN BERAPA TICKET ? "))
                    x = x + e
                    y = y + harga
                    total()

                else:
                    print("PILIHAN TIDAK TERSEDIA")
                    continue
            else:
                print("PILIHAN TIDAK TERSEDIA")
                continue

    elif a == "3" :
        break
    else:
        print("PILIHAN TIDAK TERSEDIA")
        continue

    totaltiket = totaltiket + e
    totalharga = totalharga + (harga * e)

    print("Ingin lanjut membeli tiket ? ")
    lanjut = input("(Y/N)")
    lanjut = lanjut.upper()


    if lanjut == "Y":
        continue
    elif lanjut == "N":

        print("\n===== TICKET INVOICE =====")
        print("Pembelian atas Nama : ",nama)
        print("Jenis Tiket yang dipilih :",keterangan)
        print("Jumlah tiket yang dibeli :",totaltiket)
        print("Harga yang harus dibayarkan :",totalharga)
        print("==========================")

        break 

