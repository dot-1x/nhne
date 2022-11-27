from itertools import permutations
import time

m = "m"
b = "b"
h = "h"
k = "k"

warna = {
    m: "merah",
    b: "biru",
    h: "hijau",
    k: "kuning"
}

print("\n--- Ninja Heroes Deploy ---\n")

print("----------")
for c, desc in warna.items():
    print(f"{c} = {desc}")
print("----------")

ninja = [[None, None, None, None, None], [None, None, None, None, None], [None, None, None, None, None], [None, None, None, None, None], [None, None, None, None, None], [None, None, None, None, None], [None, None, None, None, None], [None, None, None, None, None], [None, None, None, None, None], [None, None, None, None, None], [None, None, None, None, None], [None, None, None, None, None]]
ninjautama = [[None, None, None, None, None], [None, None, None, None, None], [None, None, None, None, None]]

for i in range(12):
    ninja[i][0] = input(f"Nama Ninja Deploy {i + 1}: ")

    while True:
        ninja[i][1] = input(f"- atas (m/b/h/k): ")
        ninja[i][2] = input(f"- kanan (m/b/h/k): ")
        ninja[i][3] = input(f"- bawah (m/b/h/k): ")
        ninja[i][4] = input(f"- kiri (m/b/h/k): ")

        if {ninja[i][1], ninja[i][2], ninja[i][3], ninja[i][4]} <= warna.keys():
            break
        else:
            print("Pilih m/b/h/k")
            print(ninja[i][1], ninja[i][2], ninja[i][3], ninja[i][4])      

for i in range(3):
    ninjautama[i][0] = input(f"Nama Ninja Utama Slot {i + 1}: ")

    while True:
        ninjautama[i][1] = input(f"- atas (m/b/h/k): ")
        ninjautama[i][2] = input(f"- kanan (m/b/h/k): ")
        ninjautama[i][3] = input(f"- bawah (m/b/h/k): ")
        ninjautama[i][4] = input(f"- kiri (m/b/h/k): ")

        if {ninjautama[i][1], ninjautama[i][2], ninjautama[i][3], ninjautama[i][4]} <= warna.keys():
            break
        else:
            print("Pilih m/b/h/k")
            print(ninjautama[i][1], ninjautama[i][2], ninjautama[i][3], ninjautama[i][4])

atribut = {
    "HP": "HP",
    "At": "Attack",
    "Ag": "Agility",
    "D": "Defense"
}

print("----------")
for c, desc in atribut.items():
    print(f"{c} = {desc}")
print("----------")

prioritas = [None, None, None, None]

while True:
    prioritas[0], prioritas[1], prioritas[2], prioritas[3] = input("Prioritas (Contoh: HP>At>Ag>D): ").split(">")

    if {prioritas[0], prioritas[1], prioritas[2], prioritas[3]} == atribut.keys():
        break
    else:
        print("Tidak sesuai")

perm = permutations([ninja[0], ninja[1], ninja[2], ninja[3], ninja[4], ninja[5], ninja[6], ninja[7], ninja[8], ninja[9], ninja[10], ninja[11]])
b = [ninjautama[0], ninjautama[1], ninjautama[2]]

prio = {
    "HP": [0, 0],
    "At": [0, 0],
    "Ag": [0, 0],
    "D": [0, 0]
}

total = 0
deploy = ()

start = time.time()
end = None
for index, i in enumerate(perm):
    if i[0][2] == i[1][4]:
        if i[0][2] == m:
            prio["At"][1] += 10
        elif i[0][2] == b:
            prio["D"][1] += 10
        elif i[0][2] == h:
            prio["HP"][1] += 10
        elif i[0][2] == k:
            prio["Ag"][1] += 10

    if i[1][2] == i[2][4]:
        if i[1][2] == m:
            prio["At"][1] += 10
        elif i[1][2] == b:
            prio["D"][1] += 10
        elif i[1][2] == h:
            prio["HP"][1] += 10
        elif i[1][2] == k:
            prio["Ag"][1] += 10
    
    if i[1][3] == b[0][1]:
        if i[1][3] == m:
            prio["At"][1] += 10
        elif i[1][3] == b:
            prio["D"][1] += 10
        elif i[1][3] == h:
            prio["HP"][1] += 10
        elif i[1][3] == k:
            prio["Ag"][1] += 10
    
    if i[2][2] == i[3][4]:
        if i[2][2] == m:
            prio["At"][1] += 10
        elif i[2][2] == b:
            prio["D"][1] += 10
        elif i[2][2] == h:
            prio["HP"][1] += 10
        elif i[2][2] == k:
            prio["Ag"][1] += 10
    
    if i[2][3] == b[1][1]:
        if i[2][3] == m:
            prio["At"][1] += 10
        elif i[2][3] == b:
            prio["D"][1] += 10
        elif i[2][3] == h:
            prio["HP"][1] += 10
        elif i[2][3] == k:
            prio["Ag"][1] += 10
    
    if i[3][2] == i[4][4]:
        if i[3][2] == m:
            prio["At"][1] += 10
        elif i[3][2] == b:
            prio["D"][1] += 10
        elif i[3][2] == h:
            prio["HP"][1] += 10
        elif i[3][2] == k:
            prio["Ag"][1] += 10

    if i[3][3] == b[2][1]:
        if i[3][3] == m:
            prio["At"][1] += 10
        elif i[3][3] == b:
            prio["D"][1] += 10
        elif i[3][3] == h:
            prio["HP"][1] += 10
        elif i[3][3] == k:
            prio["Ag"][1] += 10

    if i[5][1] == i[0][3]:
        if i[5][1] == m:
            prio["At"][1] += 10
        elif i[5][1] == b:
            prio["D"][1] += 10
        elif i[5][1] == h:
            prio["HP"][1] += 10
        elif i[5][1] == k:
            prio["Ag"][1] += 10
    
    if i[5][2] == b[0][4]:
        if i[5][2] == m:
            prio["At"][1] += 10
        elif i[5][2] == b:
            prio["D"][1] += 10
        elif i[5][2] == h:
            prio["HP"][1] += 10
        elif i[5][2] == k:
            prio["Ag"][1] += 10
    
    if i[6][1] == i[4][3]:
        if i[6][1] == m:
            prio["At"][1] += 10
        elif i[6][1] == b:
            prio["D"][1] += 10
        elif i[6][1] == h:
            prio["HP"][1] += 10
        elif i[6][1] == k:
            prio["Ag"][1] += 10
    
    if i[6][4] == b[2][2]:
        if i[6][4] == m:
            prio["At"][1] += 10
        elif i[6][4] == b:
            prio["D"][1] += 10
        elif i[6][4] == h:
            prio["HP"][1] += 10
        elif i[6][4] == k:
            prio["Ag"][1] += 10
    
    if i[7][1] == i[5][3]:
        if i[7][1] == m:
            prio["At"][1] += 10
        elif i[7][1] == b:
            prio["D"][1] += 10
        elif i[7][1] == h:
            prio["HP"][1] += 10
        elif i[7][1] == k:
            prio["Ag"][1] += 10
    
    if i[7][2] == i[8][4]:
        if i[7][2] == m:
            prio["At"][1] += 10
        elif i[7][2] == b:
            prio["D"][1] += 10
        elif i[7][2] == h:
            prio["HP"][1] += 10
        elif i[7][2] == k:
            prio["Ag"][1] += 10
    
    if i[8][1] == b[0][3]:
        if i[8][1] == m:
            prio["At"][1] += 10
        elif i[8][1] == b:
            prio["D"][1] += 10
        elif i[8][1] == h:
            prio["HP"][1] += 10
        elif i[8][1] == k:
            prio["Ag"][1] += 10
    
    if i[8][2] == i[9][4]:
        if i[8][2] == m:
            prio["At"][1] += 10
        elif i[8][2] == b:
            prio["D"][1] += 10
        elif i[8][2] == h:
            prio["HP"][1] += 10
        elif i[8][2] == k:
            prio["Ag"][1] += 10
    
    if i[9][1] == b[1][3]:
        if i[9][1] == m:
            prio["At"][1] += 10
        elif i[9][1] == b:
            prio["D"][1] += 10
        elif i[9][1] == h:
            prio["HP"][1] += 10
        elif i[9][1] == k:
            prio["Ag"][1] += 10
    
    if i[9][2] == i[10][4]:
        if i[9][2] == m:
            prio["At"][1] += 10
        elif i[9][2] == b:
            prio["D"][1] += 10
        elif i[9][2] == h:
            prio["HP"][1] += 10
        elif i[9][2] == k:
            prio["Ag"][1] += 10

    if i[10][1] == b[2][3]:
        if i[10][1] == m:
            prio["At"][1] += 10
        elif i[10][1] == b:
            prio["D"][1] += 10
        elif i[10][1] == h:
            prio["HP"][1] += 10
        elif i[10][1] == k:
            prio["Ag"][1] += 10
    
    if i[10][2] == i[11][4]:
        if i[10][2] == m:
            prio["At"][1] += 10
        elif i[10][2] == b:
            prio["D"][1] += 10
        elif i[10][2] == h:
            prio["HP"][1] += 10
        elif i[10][2] == k:
            prio["Ag"][1] += 10
    
    if i[11][1] == i[6][3]:
        if i[11][1] == m:
            prio["At"][1] += 10
        elif i[11][1] == b:
            prio["D"][1] += 10
        elif i[11][1] == h:
            prio["HP"][1] += 10
        elif i[11][1] == k:
            prio["Ag"][1] += 10
    
    if b[0][2] == b[1][4]:
        if i[11][1] == m:
            prio["At"][1] += 10
        elif i[11][1] == b:
            prio["D"][1] += 10
        elif i[11][1] == h:
            prio["HP"][1] += 10
        elif i[11][1] == k:
            prio["Ag"][1] += 10

    if b[1][2] == b[2][4]:
        if i[11][1] == m:
            prio["At"][1] += 10
        elif i[11][1] == b:
            prio["D"][1] += 10
        elif i[11][1] == h:
            prio["HP"][1] += 10
        elif i[11][1] == k:
            prio["Ag"][1] += 10
            
    totalawal = prio["At"][1] + prio["D"][1] + prio["HP"][1] + prio["Ag"][1]

    if totalawal > total:
        total = totalawal
        prio[prioritas[0]][0] = prio[prioritas[0]][1]
        prio[prioritas[1]][0] = prio[prioritas[1]][1]
        prio[prioritas[2]][0] = prio[prioritas[2]][1]
        prio[prioritas[3]][0] = prio[prioritas[3]][1]
        deploy = i
    elif totalawal == total:
        if prio[prioritas[0]][1] > prio[prioritas[0]][0]:
            total = totalawal
            prio[prioritas[0]][0] = prio[prioritas[0]][1]
            prio[prioritas[1]][0] = prio[prioritas[1]][1]
            prio[prioritas[2]][0] = prio[prioritas[2]][1]
            prio[prioritas[3]][0] = prio[prioritas[3]][1]
            deploy = i
        elif prio[prioritas[0]][1] == prio[prioritas[0]][0]:
            if prio[prioritas[1]][1] > prio[prioritas[1]][0]:
                total = totalawal
                prio[prioritas[0]][0] = prio[prioritas[0]][1]
                prio[prioritas[1]][0] = prio[prioritas[1]][1]
                prio[prioritas[2]][0] = prio[prioritas[2]][1]
                prio[prioritas[3]][0] = prio[prioritas[3]][1]
                deploy = i
            elif prio[prioritas[1]][1] == prio[prioritas[1]][0]:
                if prio[prioritas[2]][1] > prio[prioritas[2]][0]:
                    total = totalawal
                    prio[prioritas[0]][0] = prio[prioritas[0]][1]
                    prio[prioritas[1]][0] = prio[prioritas[1]][1]
                    prio[prioritas[2]][0] = prio[prioritas[2]][1]
                    prio[prioritas[3]][0] = prio[prioritas[3]][1]
                    deploy = i

    prio["At"][1], prio["D"][1], prio["HP"][1], prio["Ag"][1] = 0, 0, 0, 0
    
    if index == 479001:
        end = time.time()
        print(f"estimasi waktu: {round((end - start) * 1000 / 60)} menit")
        print(f"Harap tunggu...")
    
print("--- Atribut ---")
print("Attack:", prio["At"][0])
print("Defense:", prio["D"][0])
print("HP:", prio["HP"][0] * 5)
print("Agility:", prio["Ag"][0])
print("--- Deploy ---")
print("Baris 1:", deploy[0][0], ",", deploy[1][0], ",", deploy[2][0], ",", deploy[3][0], ",", deploy[4][0])
print("Baris 2:", deploy[5][0], ",", b[0][0], ",", b[1][0], ",", b[2][0], ",", deploy[6][0])
print("Baris 3:", deploy[7][0], ",", deploy[8][0], ",", deploy[9][0], ",", deploy[10][0], ",", deploy[11][0])