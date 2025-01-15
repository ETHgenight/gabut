my_list = [10, 20, 30, 40]
print(my_list[0])  # Output: 10
print(my_list[-1]) # Output: 40 (indeks negatif dari belakang)

my_list = [10, 20, 30, 40, 50]
print(my_list[1:4])  # Output: [20, 30, 40]
print(my_list[:3])   # Output: [10, 20, 30]
print(my_list[::2])  # Output: [10, 30, 50] (2 langkah)

# Mengganti elemen tertentu dengan indeks.
my_list = [10, 20, 30]
my_list[1] = 99
print(my_list)  # Output: [10, 99, 30]

# Append: Tambahkan elemen di akhir.
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]

# Insert: Sisipkan elemen ke indeks tertentu.
my_list = [1, 2, 4]
my_list.insert(2, 3)
print(my_list)  # Output: [1, 2, 3, 4]

#Menghapus elemen berdasarkan nilai.
my_list = [1, 2, 3, 2]
my_list.remove(2)
print(my_list)  # Output: [1, 3, 2]

# Menghapus elemen berdasarkan indeks atau seluruh list.
my_list = [1, 2, 3]
del my_list[1]
print(my_list)  # Output: [1, 3]
del my_list     # Menghapus seluruh list

# Menghapus elemen terakhir (atau elemen tertentu) dan mengembalikannya.
my_list = [1, 2, 3]
popped = my_list.pop()
print(popped)  # Output: 3
print(my_list)  # Output: [1, 2]

# Menghapus seluruh elemen, tetapi list tetap ada.
my_list = [1, 2, 3]
my_list.clear()
print(my_list)  # Output: []