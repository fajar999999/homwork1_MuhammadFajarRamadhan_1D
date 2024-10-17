print('=================== topup =====================')
print('tidak ada biaya admin')
nama              = input(  'masukan nama             :')
nomer           = int(input('masukan nomer hp         :'))
jenis_rekening    = input(  'masukan jenis rekening   :')
awal            = int(input('masukan saldo awal       :'))
disetujui=True
topup         = int(input(  'masukan jumlah topup     :'))
berhasil='''selamat topup anda berhasil  ! saldo anda :'''
jumlah=(awal + topup)
rekening=['ovo','qris','gopay','dana']
hasil= ('topup anda berhasil' if jenis_rekening in rekening and disetujui==True and 
        topup <=1000000 else 'maaf topup anda gagal')
print('=================== hasil =====================')
print(berhasil, jumlah if awal + topup <=1000000 else  'maaf saldo gagal')
print(hasil)