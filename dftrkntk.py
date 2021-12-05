daftarkontak = {"nama": "nomor telepon"}
kontak = {'faiz': '088834567', 'adit': '085834986'}

print("="*30)
print("  nama   |    nomor telepon  ")
print("="*30)
print("# faiz   |   ", kontak['faiz'])
print("# adit   |   ", kontak['adit'])
print("="*30)

# menampilkan kontak faiz
print("menampilkan kontak faiz")
print("="*30)
print(" # faiz  |  ", kontak['faiz'])
print("="*30)

# menambahkan kontak dengan nama fajar dan nomor 0834652577
print("menambahkan kontak dengan nama fajar dan nomor 0834652577")
kontak['fajar'] = '0834652577'
print("="*30)
print("  fajar  |  ", kontak['fajar'])
print('='*30)

# mengubah kontak adit dengan nomor baru 08756435
print("mengubah kontak adit dengan nomor baru 08756435")
kontak['adit'] = '0834652577'
print("="*30)
print("  adit  |  ", kontak['adit'])
print("="*30)

# menampilkan semua nama
print("menampilkan semua nama")
print("="*30)
print(kontak.keys())
print("="*30)

# menampilkan semua nomor
print("menampilkan semua nomor")
print("="*30)
print(kontak.values())
print("="*30)

# menampilkan semua daftar kontak beserta nomornya
print("menampilkan daftar nama dan nomor")
print("="*30)
print(kontak.items())
print("="*30)

# menghapus kontak adit
print("menghapus kontak adit")
kontak.pop('adit')
print("="*30)
print(kontak.items())
print("="*30)
