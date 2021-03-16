# Menampilkan list 10 teman
list = ['Divana', 'Gea', 'Alifiana', 'Candrika', 'Angela', 'Ayu', 'Attar', 'Bagus', 'Hana', 'Funny']

# Menampilkan isi list indeks nomor 4, 6, dan 7
print("List indesk nomor 4,6, dan 7 yaitu", list[4], ",", list[6], ",", "dan", list[7])

# Mengganti nama teman di list 3, 5, dan 9
list[3] = 'Hani'
list[5] = 'Rara'
list[9] = 'Fadhila'

# Menambahkan 2 nama teman
list.append('Erika')
list.append('Dhea')

# Menampilkan semua teman dengan pengulangan
print(list*2)

# Menampilkan panjang list
print(len(list))
