for baris in range(1, 5):
    for isi in range(baris, 5):
        print(isi, end='')
    print('\r')

# Guess the output and explain the algorithm !

""" OUTPUT
1234
234
34
4

Pembahasan:
#   for pertama akan membuat perulangan untuk baris
    sebanyak 4 kali start 1 end 5-1=4
#   for kedua akan membuat perulangan untuk isi pola segitiga
    sebanyak dari perulangan baris pada saat itu sampai 5-1=4.
    Apabila pada saat itu merupakan perulangan baris ke-1 maka
    start 1, perulangan baris ke-2 start 2, dst.
#   Print pertama untuk menampilkan pola segitiga yang dibentuk
    dari nilai perulangan isi, maksud end='' adalah agar output
    menjadi satu baris / menghilangkan enter
#   Print kedua untuk menambahkan enter ketika 
    perulangan isi di setiap baris telah selesai 
"""