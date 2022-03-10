import json
from json import encoder
import os
from datetime import datetime as dt
datatrip = 'data.json'
databarang = 'data_barang.json'
data_trip = []
data_barang = []
items = []
val = []
wt = []
W = 0
n = 0
t = [[-1 for i in range(W + 1)] for j in range(n + 1)]
[]
[]
[]
[]



def clear() :
    os.system('cls')
def menu_utama() :
    clear()
    while True :
        print('='*30)
        print('{0:^30s}'.format('FRIEND TRIP'))
        print('-'*30)
        print('{0:^30s}'.format('SELAMAT DATANG'))
        print('='*30)
        print('{0:^30s}'.format('-'*30))
        print('{0:^30s}'.format('|       1. Tambah Trip       |'))
        print('{0:^30s}'.format('-'*30))
        print('{0:^30s}'.format('-'*30))
        print('{0:^30s}'.format('|       2. Daftar Trip       |'))
        print('{0:^30s}'.format('-'*30))
        print('{0:^30s}'.format('-'*30))
        print('{0:^30s}'.format('|      3. Tambah Barang      |'))
        print('{0:^30s}'.format('-'*30))
        print('{0:^30s}'.format('-'*30))
        print('{0:^30s}'.format('|      4. Daftar Barang      |'))
        print('{0:^30s}'.format('-'*30))
        print('{0:^30s}'.format('-'*30))
        print('{0:^30s}'.format('|       5. Hapus Trip        |'))
        print('{0:^30s}'.format('-'*30))
        print('{0:^30s}'.format('-'*30))
        print('{0:^30s}'.format('|       6. Hapus Barang      |'))
        print('{0:^30s}'.format('-'*30))
        print('{0:^30s}'.format('-'*30))
        print('{0:^30s}'.format('|          7. Keluar         |'))
        print('{0:^30s}'.format('-'*30))
        print('\n')
        item = int(input('Pilih menu :'))
        if (item == 1) :
            tambah_trip()
        elif (item == 2) :
            tampil_trip()
        elif (item == 3) :
            tambah_barang()
        elif (item == 4) :
            tampil_barang()
        elif (item == 5) :
            hapus_trip()
        elif (item == 6) :
            hapus_barang()
        elif (item==7) :
            exit()
        else :
            print('Menu tidak tersedia')
    

def tambah_trip() :
    clear()
    print('='*42)
    print('{0:^42}'.format('TAMBAH TRIP'))
    print('='*42)
    with open (datatrip, 'r') as file :
        data_trip = json.load(file)
        for x in file :
            data_trip.append(x)
        data = dict()
        data ['kota'] = input('Masukkan Nama Kota :')
        data ['lama'] = int(input('Masukkan lama perjalanan :'))
        data ['berangkat'] = int(input ('Masukkan Tanggal Berangkat :'))
        data ['pulang'] = int(input ('Masukkan Tanggal Pulang :'))
        data ['cost'] = int(input ('Masukkan Budget Perjalanan :'))
        data_trip.append(data)
        with open (datatrip, 'w') as file :
            json.dump(data_trip, file, indent=2)
    print('\n')
    print('Trip Berhasil Ditambahkan')
    input('Tekan ENTER Untuk Kembali Ke Menu Utama')
    menu_utama()

def tampil_trip() :
    clear()
    print('='*74)
    print('{0:^74}'.format('TAMPIL TRIP'))
    print('='*74)
    with open (datatrip, 'r') as file :
        data_trip = json.load(file)
        for x in file :
            data_trip.append(x)
        print('{0:3s}{1:16s}{2:16s}{3:16s}{4:16s}{5:16s}'.format(('NO'),('Nama Trip'),('Lama Prjln'),('Tgl. Brngkt'),('Tgl. Plg'),('Budget')))
        print('='*74)
        for x in range(len(data_trip)) :
            print('{0:1d}  {1:16s}{2:5d}   {3:16d}{4:16d}{5:15d}'.format((x+1),data_trip[x]["kota"],data_trip[x]["lama"],data_trip[x]["berangkat"],data_trip[x]["pulang"],data_trip[x]["cost"]))
        print('\n')
        print('Menu : 1. pilih berdasar budget anda   2. pilih berdasar hari anda  3. Menu utama')

        pilih = int(input('Pilih menu :'))
        if pilih == 1 :
            inputan_harga()
        elif pilih == 2 :
            inputan_hari()
        elif pilih == 3 :
            menu_utama()

def tambah_barang() :
    counter = 0
    clear()
    print('='*42)
    print('{0:^42}'.format('TAMBAH BARANG'))
    print('='*42)
    with open (databarang, 'r') as file :
        data_barang = json.load(file)
        for x in file :
            data_barang.append(x)
        data = dict()
        data ['kota'] = input('Masukkan Nama Kota :')
        data ['barang'] = barang = dict()
        data ['berat'] = berat = dict()
        data ['jumlah'] = jumlah = dict()
        barang ['barang'] = input ('masukkan barang :')
        berat ['berat'] = int(input('masukkan berat barang(kg) :'))
        jumlah ['jumlah'] = int(input('masukkan jumlah barang :'))
        while True :
            counter +=1
            tanya = input('ingin menambah barang ?')
            if tanya == 'y' :
                barang ['barang'+str(counter)] = input ('masukkan barang :')
                berat ['berat'+str(counter)] = int(input('masukkan berat barang(kg) :'))
                jumlah ['jumlah'+str(counter)] = int(input('masukkan jumlah barang :'))
            else :
                break
        data_barang.append(data)
        with open (databarang, 'w') as file :
            json.dump(data_barang, file, indent=2)
        print('\n')
        print('barang Berhasil Ditambahkan')
        input('Tekan ENTER Untuk Kembali Ke Menu Utama')
        menu_utama()

def tampil_barang() :
    clear()
    global jumlah
    print('='*20)
    print('{0:^20}'.format('TAMPIL BARANG'))
    print('='*20)
    with open (databarang, 'r') as file :
        data_barang = json.load(file)
        for x in file :
            data_barang.append(x)
        print('{0:3s}{1:16s}'.format(('NO'),('Nama Trip')))
        print('='*20)
        for x in range(len(data_barang)) :
            print('{0:1d}  {1:16s}'.format((x+1),data_barang[x]["kota"]))
        print('\n')
        tanya = int(input('Pilih Nomer Trip yang ingin dilihat barangnya :'))
        tanya -= 1
        for x in range(len(data_barang)) :
            if data_barang[x]["kota"] == data_barang[tanya]["kota"] :
                clear()
                print('='*42)
                print('{0:^42}'.format('TAMPIL BARANG'))
                print('='*42)
                print('{0:^42}'.format(data_barang[x]['kota']))
                print('-'*42)
                print('{0:3s}{1:16s}{2:16s}{3:16s}'.format(('NO'),('Nama Barang'),('Berat'),('Jumlah')))
                print('='*42)
                for s in range(len(data_barang[x]["barang"])) :
                    jumlah = x
                    if s == 0 :
                        print('{0:2d} {1:16s}{2:2d}{3:14d}'.format((s+1),data_barang[x]["barang"]["barang"],data_barang[x]["berat"]["berat"],data_barang[x]["jumlah"]["jumlah"]))
                    elif s > 0 :
                        print('{0:2d} {1:16s}{2:2d}{3:14d}'.format((s+1),data_barang[x]["barang"]["barang"+str(s)],data_barang[x]["berat"]["berat"+str(s)],data_barang[x]["jumlah"]["jumlah"+str(s)]))
                print('\n')
                print('1. pindah ke tas  2. kembali ke menu utama')
                pilih = int(input('Pilih menu :'))
                if pilih == 1 :
                    inputan_barang(jumlah)
                else :
                    menu_utama()

def hapus_trip() :
    clear()
    print('='*58)
    print('{0:^58}'.format('HAPUS TRIP'))
    print('='*58)
    with open (datatrip, 'r') as file :
        data_trip = json.load(file)
        for x in file :
            data_trip.append(x)
        print('{0:3s}{1:16s}{2:16s}{3:16s}{4:16s}'.format(('NO'),('Nama Trip'),('Tgl. Brngkt'),('Tgl. Plg'),('Budget')))
        print('='*58)
        for x in range(len(data_trip)) :
            print('{0:1d}  {1:16s}{2:16d}{3:16d}{4:16d}'.format((x+1),data_trip[x]["kota"],data_trip[x]["berangkat"],data_trip[x]["pulang"],data_trip[x]["cost"]))
        print('\n')
        tanya = int(input('Pilih Nomer Trip yang ingin dihapus barangnya :'))
        tanya -= 1
        del data_trip[tanya]
        with open (datatrip, 'w') as file :
            json.dump(data_trip, file, indent=2)
        print('\n')
        print('Trip Berhasil Dihapus')
        input('Tekan ENTER Untuk Kembali Ke Menu Utama')
        menu_utama()

def hapus_barang() :
    clear()
    print('='*20)
    print('{0:^20}'.format('HAPUS BARANG'))
    print('='*20)
    with open (databarang, 'r') as file :
        data_barang = json.load(file)
        for x in file :
            data_barang.append(x)
        print('{0:3s}{1:16s}'.format(('NO'),('Nama Trip')))
        print('='*20)
        for x in range(len(data_barang)) :
            print('{0:1d}  {1:16s}'.format((x+1),data_barang[x]["kota"]))
        print('\n')
        tanya = int(input('Pilih Nomer Trip yang ingin dihapus barangnya :'))
        tanya -= 1
        del data_barang[tanya]
        with open (databarang, 'w') as file :
            json.dump(data_barang, file, indent=2)
        print('\n')
        print('Barang telah berahsil dihapus')
        input('Tekan ENTER Untuk Kembali Ke Menu Utama')
        menu_utama()

def knapsack(wt, val, W, n):
	# base conditions
	if n == 0 or W == 0:
		return 0
	if t[n][W] != -1:
		return t[n][W]
	# choice diagram code
	if wt[n - 1] <= W:
		t[n][W] = max(val[n - 1] + knapsack(wt, val, W - wt[n - 1], n - 1),
		              knapsack(wt, val, W, n - 1))
		return t[n][W]
	elif wt[n - 1] > W:
		t[n][W] = knapsack(wt, val, W, n - 1)
		return t[n][W]
def inputan_hari() :
    global wt
    global val
    global W
    global n
    global items
    global t
    with open (datatrip, 'r') as file :
        data_trip = json.load(file)
        for x in file :
            data_trip.append(x)
        for a in range(len(data_trip)) :
            items.append(data_trip[a]["kota"])
            wt.append(data_trip[a]["lama"])
            val.append(data_trip[a]["cost"])
        n = len(data_trip)
        W = int(input('Masukkan berapa lama hari liburan anda :'))
        t = [[-1 for i in range(W + 1)] for j in range(n + 1)]
        []
        []
        []
        []
        filter_hari(wt, val, W, n)

def inputan_harga() :
    global wt
    global val
    global W
    global n
    global items
    global t
    with open (datatrip, 'r') as file :
        data_trip = json.load(file)
        for x in file :
            data_trip.append(x)
        for a in range(len(data_trip)) :
            items.append(data_trip[a]["kota"])
            val.append(data_trip[a]["lama"])
            wt.append(data_trip[a]["cost"])
        n = len(data_trip)
        W = int(input('Masukkan berapa budget liburan anda :'))
        t = [[-1 for i in range(W + 1)] for j in range(n + 1)]
        []
        []
        []
        []
        filter_harga(wt, val, W, n)

def filter_hari(wt, val, W, n) :
    value = knapsack(wt, val, W, n)

    thingsItems = []
    idx = W

    for i in range(len(val), 0, -1):
        if value <= 0:
            break
        if value == t[i - 1][idx]:
            continue
        else:
            pickItems = items[i - 1]
            thingsItems.append(pickItems)

            value = value - val[i - 1]
            idx = idx - wt[i - 1]
    print(thingsItems)
    with open (datatrip, 'r') as file :
        data_trip = json.load(file)
        for x in file :
            data_trip.append(x)
        clear()
        print('='*74)
        print('{0:^74}'.format('TAMPIL TRIP'))
        print('{0:^74}'.format('FILTER HARI'))
        print('='*74)
        print('{0:3s}{1:16s}{2:16s}{3:16s}{4:16s}{5:16s}'.format(('NO'),('Nama Trip'),('Lama Prjln'),('Tgl. Brngkt'),('Tgl. Plg'),('Budget')))
        print('='*74)
        for x in range(len(data_trip)) :
            for a in thingsItems :
                if a == data_trip[x]["kota"] : 
                    print('{0:1d}  {1:16s}{2:5d}   {3:16d}{4:16d}{5:15d}'.format((x+1),data_trip[x]["kota"],data_trip[x]["lama"],data_trip[x]["berangkat"],data_trip[x]["pulang"],data_trip[x]["cost"]))
        print('Total Harga :',knapsack(wt, val, W, n))
        print('\n')
        input('Tekan ENTER Untuk Kembali Ke Menu')
        reset()
        tampil_trip()

def filter_harga(wt, val, W, n) :
    value = knapsack(wt, val, W, n)

    thingsItems = []
    idx = W

    for i in range(len(val), 0, -1):
        if value <= 0:
            break
        if value == t[i - 1][idx]:
            continue
        else:
            pickItems = items[i - 1]
            thingsItems.append(pickItems)

            value = value - val[i - 1]
            idx = idx - wt[i - 1]
    print(thingsItems)
    with open (datatrip, 'r') as file :
        data_trip = json.load(file)
        for x in file :
            data_trip.append(x)
        clear()
        print('='*74)
        print('{0:^74}'.format('TAMPIL TRIP'))
        print('{0:^74}'.format('FILTER HARGA'))
        print('='*74)
        print('{0:3s}{1:16s}{2:16s}{3:16s}{4:16s}{5:16s}'.format(('NO'),('Nama Trip'),('Lama Prjln'),('Tgl. Brngkt'),('Tgl. Plg'),('Budget')))
        print('='*74)
        for x in range(len(data_trip)) :
            for a in thingsItems :
                if a == data_trip[x]["kota"] : 
                    print('{0:1d}  {1:16s}{2:5d}   {3:16d}{4:16d}{5:15d}'.format((x+1),data_trip[x]["kota"],data_trip[x]["lama"],data_trip[x]["berangkat"],data_trip[x]["pulang"],data_trip[x]["cost"]))
        print('Total Lama perjalanan :',knapsack(wt, val, W, n))        
        print('\n')
        input('Tekan ENTER Untuk Kembali Ke Menu')
        reset()
        tampil_trip()
        
def reset() :
    global items
    global val
    global wt
    global t
    items = []
    val = []
    wt = []
    W = 0
    n = 0
    t = [[-1 for i in range(W + 1)] for j in range(n + 1)]
    []
    []
    []
    []
def inputan_barang(jumlah) :
    global val
    global W
    global n
    global items
    global t
    with open (databarang, 'r') as file :
        data_barang = json.load(file)
        for x in file :
            data_barang.append(x)
        
        for a in range(len(data_barang[jumlah]["barang"])) :
            if a == 0 :
                items.append(data_barang[jumlah]["barang"]["barang"])
            elif a > 0 :
                items.append(data_barang[jumlah]["barang"]["barang"+str(a)])
        for b in range(len(data_barang[jumlah]["berat"])) :
            if b == 0 :
                wt.append(data_barang[jumlah]["berat"]["berat"])
            elif b > 0 :
                wt.append(data_barang[jumlah]["berat"]["berat"+str(b)])
        for c in range(len(data_barang[jumlah]["jumlah"])) :
            if c == 0 :
                val.append(data_barang[jumlah]["jumlah"]["jumlah"])
            elif c > 0 :
                val.append(data_barang[jumlah]["jumlah"]["jumlah"+str(c)])
        n = len(data_barang[jumlah]["barang"])
        W = int(input('Masukkan berapa kapasitas tas anda :'))
        t = [[-1 for i in range(W + 1)] for j in range(n + 1)]
        []
        []
        []
        []
        filter_barang(wt, val, W, n)
def filter_barang(wt, val, W, n) :
    value = knapsack(wt, val, W, n)

    thingsItems = []
    idx = W

    for i in range(len(val), 0, -1):
        if value <= 0:
            break
        if value == t[i - 1][idx]:
            continue
        else:
            pickItems = items[i - 1]
            thingsItems.append(pickItems)

            value = value - val[i - 1]
            idx = idx - wt[i - 1]
    print(thingsItems)
    with open (databarang, 'r') as file :
        data_barang = json.load(file)
        for x in file :
            data_barang.append(x)
        clear()
        print('='*42)
        print('{0:^42}'.format('TAMPIL BARANG'))
        print('{0:^42}'.format('FILTER BARANG'))
        print('='*42)
        print('{0:^42}'.format(data_barang[jumlah]['kota']))
        print('-'*42)
        print('{0:3s}{1:16s}{2:16s}{3:16s}'.format(('NO'),('Nama Barang'),('Berat'),('Jumlah')))
        print('='*42)
        for a in range(len(data_barang[jumlah]["barang"])) :
            for b in thingsItems :
                if a == 0 :
                    if data_barang[jumlah]["barang"]["barang"] == b :
                        print('{0:2d} {1:16s}{2:3d}{3:14d}'.format((a+1),data_barang[jumlah]["barang"]["barang"],data_barang[jumlah]["berat"]["berat"],data_barang[jumlah]["jumlah"]["jumlah"]))
                elif a > 0 :
                    if data_barang[jumlah]["barang"]["barang"+str(a)] == b  :
                        print('{0:2d} {1:16s}{2:3d}{3:14d}'.format((a+1),data_barang[jumlah]["barang"]["barang"+str(a)],data_barang[jumlah]["berat"]["berat"+str(a)],data_barang[jumlah]["jumlah"]["jumlah"+str(a)]))
        print('\n')
        input('Tekan ENTER Untuk Kembali Ke Menu')

menu_utama()
