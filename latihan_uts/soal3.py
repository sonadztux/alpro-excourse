kuis = 70
uts = 60
uas = 65
na = ((kuis*0.20)+(uts*0.30)+(uas*0.30))
print(na)

if na > 80:
    print('A')
elif 75 <= 80 and na > 75:
    print('B')
elif na <= 75 and na > 70:
    print('C')
elif na <= 70 and na > 60:
    print('D')
else:
    print('E')

# Guess the output and explain the algorithm !

"""
OUTPUT:
E

Pembahasan:
#   Hasil perhitungan nilai-nilai di variabel kuis, uts, dan uas
    adalah 51.5 disimpan pad variabel na.
#   Kemudian dilakukan algoritma seleksi menggunakan if-elif-else
    untuk menentukan grade yang sesuai dengan nilai pada na.
#   Karena seluruh kondisi if-elif tidak terpenuhi, maka akan 
    langsung dijalankan fungsi else dengan output 'E'
"""
