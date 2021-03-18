# Membuat dictionary pada python
dict = {'Nama':'Ara','Hobi 1':'Memasak','Hobi 2':'Menonton film','Hobi 3':'Jalan-jalan','Sosmed 1':'line:aratiakp_'
,'Sosmed 2':'ig:aratiakp_','Sosmed 3':'twitter:cutieeberryy','Lagu 1':'To the bone','Lagu 2':'Blue Jeans'
,'Lagu 3':'Heartbreak Anniversary','Makanan 1':'Mie', 'Makanan 2':'Seblak','Makanan 3':'Nasi Goreng'}

# Mengubah salah satu hobi dan sosial media
dict['Hobi 2'] = 'Mendengarkan musik'
dict['Sosmed 2'] = 'ig:gmssrv_'

# Menghapus 2 makanan kesukaan
del dict['Makanan 1']
del dict['Makanan 2']

# Menambah satu hobi
dict['Hobi 4'] = 'Bersepeda'

print(dict)