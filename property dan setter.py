'''
property(@) berfungsi untuk memanggil metode sebagai atribut
'''
class mahasiswa():
    def __init__(self, awal, akhir):
        self.awal = awal
        self.akhir = akhir
    
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.awal, self.akhir)
    
    def namalengkap(self):
        return '{} {}'.format(self.awal, self.akhir)

p1 = mahasiswa('noval', 'arman')
p1.akhir = 'saputra' #mengubah nilai dari atribute
print(p1.awal)
print(p1.email) #email dipanggil sebagai atribute bukan fungsi (tanpa tanda kurung)
print(p1.namalengkap()) # pakai () jika tidak pakai decorator

'''
setter berfungsi mengubah nilai atribute yang didefinisikan didalam property
'''
class mahasiswa():
    def __init__(self, awal, akhir):
        self.awal = awal
        self.akhir = akhir
    
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.awal, self.akhir)
    
    @property
    def namalengkap(self):
        return '{} {}'.format(self.awal, self.akhir)
    
    @namalengkap.setter
    def namalengkap(self, nama):
        awal, akhir = nama.split(' ')
        self.awal = awal
        self.akhir = akhir

p1 = mahasiswa('noval', 'saputra')
p1.namalengkap = 'joko widodo'  #mengubah nilai atribute
print(p1.awal)
print(p1.email)
print(p1.namalengkap) 

class mahasiswa():
    def __init__(self, awal, akhir):
        self.awal = awal
        self.akhir = akhir
    
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.awal, self.akhir)
    
    @property
    def namalengkap(self):
        return '{} {}'.format(self.awal, self.akhir)
    
    @namalengkap.setter
    def namalengkap(self, nama):
        awal, akhir = nama.split(' ')
        self.awal = awal
        self.akhir = akhir
    
    @namalengkap.deleter
    def namalengkap(self):
        print('menghapus nama')
        self.awal = None
        self.akhir = None
        
p1 = mahasiswa('noval', 'saputra')
p1.namalengkap = 'joko widodo'  #mengubah nilai atribute
print(p1.awal)
print(p1.email)
print(p1.namalengkap)
del p1.namalengkap
print(p1.awal)
print(p1.email)
print(p1.namalengkap)