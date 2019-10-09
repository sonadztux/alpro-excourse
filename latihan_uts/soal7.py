data = [1,1,2,4,5,8,13,6,7]
print(data[data[4]])

# Guess the output and explain the logic

""" 
OUTPUT:
8

Pembahasan:
#   Fokus pada data[] yang terdalam yaitu data[4]
    --nilai di index ke-4 pada list data--
    berisi nilai 5 / data[4] = 5.
#   Sehingga data[data[4]] dapat direpresentasikan
    menjadi data[5]
#   print akan mencetak nilai di index ke-5 pada list data
"""