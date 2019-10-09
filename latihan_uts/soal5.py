nama = 'otong'

def nama_saya(name):
    nama = name
    return 'nama saya '+nama

print(nama)
# print(nama_saya('pak pol'))
# print(nama_saya('sule'))

# Guess the output and explain about
# global variable and local variable

"""
OUTPUT:
otong
# pak pol
# sule

Pembahasan:
#   Variabel nama pertama merupakan global variable
    yang bersifat independen dan dapat diakses
    langsung dalam file yang sama
#   Sedangkan variabel nama kedua merupakan local variable
    milik fungsi nama_saya() dan dapat diakses dengan
    menjalankan fungsi nama_saya('nama kamu di sini')
#   Sehingga ketika dilakukan print(nama) maka yang
    akan ditampilkan variabel nama pertama yaitu otong
"""