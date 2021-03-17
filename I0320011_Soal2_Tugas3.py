# Membuat dictionary pada python
dict = {'Nama':'Ara','Hobi1':'Memasak','Hobi2':'Menonton film','Hobi3':'Jalan-jalan','Sosmed1':'line:aratiakp_','Sosmed2':'ig:aratiakp_','Sosmed3':'twitter:cutieeberryy','Lagu1':'To the bone','Lagu2':'Blue Jeans','Lagu3':'Heartbreak Anniversary','Makanan1':'Mie', 'Makanan2':'Seblak','Makanan3':'Nasi Goreng'}

# Mengubah salah satu hobi dan sosmed, menghapus 2 makanan, dan menambah 1 hobi
dict['Hobi2'] = 'Mendengarkan musik'
dict['Sosmed2'] = 'ig:gmssrv_'
del dict['Makanan1']
del dict['Makanan2']
dict['Hobi4'] = 'Bersepeda'

print(dict)