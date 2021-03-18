# Menampilkan list nama 10 teman
list = ['Divana', 'Gea', 'Alifiana', 'Candrika', 'Angela', 'Ayu', 'Attar', 'Bagus', 'Hana', 'Funny']

# Menampilkan isi list indeks nama teman nomor 4, 6, dan 7
print("List indeks nama teman pada nomor 4,6, dan 7 yaitu", list[4], ",", list[6], ",", "dan", list[7])

# Mengganti nama teman pada list 3, 5, dan 9
list[3] = 'Hani'
list[5] = 'Rara'
list[9] = 'Fadhila'

# Menambahkan 2 nama teman ke dalam list
list.append('Erika')
list.append('Dhea')

# Menampilkan semua nama teman dengan pengulangan
hazelnut = 0
for caramel in range (0,12) :
    print (list[hazelnut])
    hazelnut+=1

# Menampilkan panjang list nama teman
print("Panjang indeks list nama teman adalah", len(list))
