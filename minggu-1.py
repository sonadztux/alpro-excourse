# string = ""
# line = 3

# while line >= 0:
#     height = line
#     while height > 0:
#         string = string + " * " 
#         height = height - 1
#     string = string + "\n"
#     line = line - 1
# print(string)

# hari = input('Nama hari: ')
# tanggal = int(input('Tanggal: '))
# tambah = 5 + tanggal

# print(hari)
# print(tanggal)
# print(tambah)

# for i in range(1, 10, 5):
#     print(i)

# x = 1
# a = 9
# star = '1202184077'

# while x < 10:
#     print('1202184077')
#     if x == 9:
#         while a <= x:
#             print(star, end="")
#             a = a + 1
# x = x + 1

# x = str(input('Masukkan username anda: '))
# if x == 'nanda':
#     print('username', x, 'benar')
# else:
#     print('username', x, 'salah')

# y = str(input('Masukkan password anda: '))
# if y == '1202184077':
#     print('Welcome to Ensyse Lab')
# else:
#     print('password salah')

hari = 'Senin'

if hari is not 'Minggu':
    print('kuliah libur')
elif hari == 'Senin':
    print('upacara')
else:
    print('kita kuliah')
