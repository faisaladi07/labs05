a = {}
print("="*80)
print("|      PROGRAM INPUT NILAI MAHASISWA MENGGUNAKAN DICTIONARY      |")
print("="*80)

while True:
    c = input("(t)ambah, (e)dit, (c)cari, (h)apus, (l)ihat, (k)eluar: ")

    if c.lower() == 't':
        print(" TAMBAH DATA MAHASISWA ")
        nama = input(" Nama        : ")
        nim = int(input(" NIM         : "))
        tugas = int(input(" Nilai Tugas : "))
        uts = int(input(" Nilai UTS   : "))
        uas = int(input(" Nilai UAS   : "))
        n_akhir = tugas * 0.30 + uts * 0.35 + uas * 0.35
        a[nama] = nim, tugas, uts, uas, n_akhir

    elif c .lower() == 'e':
        print("| EDIT DATA MAHASISWA |")
        nama = input("Masukkan Nama: ")
        if nama in a.keys():
            nim = input("Masukkan NIM          : ")
            tugas = int(input("Masukkan Nilai Tugas  : "))
            uts = int(input("Masukkan Nilai UTS   : "))
            uas = int(input("Masukkan Nilai UAS    : "))
            n_akhir = tugas * 0.30 + uts * 0.35 + uas * 0.35
            a[nama] = nim, tugas, uts, uas, n_akhir
        else:
            print("Nama{0} Tidak Ada" . format(nama))

    elif c.lower() == 'h':
        print("hapus data")
        nama = input("Masukan Nama : ")
        if nama is a.keys():
            del a[nama]
        else:
            print("Nama{0} Tidak Ada".format(nama))

    elif c.lower() == 'c':
        print("| CARI DATA MAHASISWA |")
        nama = input("Masukan Nama :  ")
        if nama in a.keys():
            print("="*80)
            print("|                  DAFTAR NILAI MAHASISWA                   |")
            print("="*80)
            print("|     Nama     |    NIM    | Tugas |  UTS  |  UAS  |  Akhir |")
            print("="*80)
            print("| {0:15s} | {1:15d} | {2:5d} | {3:5d} | {4:7d} | {5:7.2f} |"
                  .format(nama, nim, tugas, uts, uas, n_akhir))
            print("="*80)
        else:
            print("Nama {0} Tidak Ada ".format(nama))

    elif c.lower() == 'l':
        if a.items():
            print("="*80)
            print("                      DAFTAR NILAI MAHASISWA                    ")
            print("="*80)
            print("| No |     Nama     |    NIM    | Tugas |  UTS  |  UAS  |  Akhir |")
            print("="*80)
            i = 0
            for y in a.items():
                i += 1
                print("| {no:2d} | {0:15s} | {1:15d} | {2:5d} | {3:5d} | {4:7d} | {5:7.2f} |"
                      .format(y[0][:13], y[1][0], y[1][1], y[1][2], y[1][3], y[1][4], no=i))
                print("="*80)
        else:
            print("="*80)
            print("                      DAFTAR NILAI MAHASISWA                    ")
            print("="*80)
            print("| No |     Nama     |    NIM    | Tugas |  UTS  |  UAS  |  Akhir |")
            print("="*80)
            print("|                          TIDAK ADA DATA!                       |")
            print("="*80)

    elif c.lower() == 'k':
        break

    else:
        print("Pilih menu yang tersedia: ")
