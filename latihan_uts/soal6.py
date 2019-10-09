data = [5, 7, 5, 2, 9, 2, 3, 9, 10]
print(data)

data.sort()
print(data)

x = data[1:4]
print(x)

# Guess the three output that will displayed
# explain the logic

"""
OUTPUT:
[5, 7, 5, 2, 9, 2, 3, 9, 10]
[2, 2, 3, 5, 5, 7, 9, 9, 10]
[2, 3, 5]

Pembahasan:
#   Print pertama akan mencetak list/array
    dengan bentuk aslinya
#   data.sort() merupakan fungsi built-in python
    untuk mengurutkan nilai-nilai pada list/array
    dari yang terkecil ke terbesar
#   Print kedua akan mencetak list/array
    dengan bentuk yang sudah urut terkecil ke terbesar
#   Variabel x untuk menyimpan nilai-nilai pada list
    dimulai dari index ke-1 hingga index ke-3 (1 sebelum 4)
#   Kemudian akan dicetak oleh print(x) dalam
    bentuk list berisi 3 nilai
"""