from itertools import permutations
import time

m = "Merah"
b = "Biru"
h = "Hijau"
k = "Kuning"

dataninja = [
  ["Yoroi","Biru","Kuning","Hijau","Merah"],
  ["Konoha Guard","Hijau","Merah","Kuning","Kuning"],
  ["Tsurugi Misumi","Kuning","Hijau","Merah","Biru"],
  ["Anbu Guard","Hijau","Biru","Merah","Biru"],
  ["Anbu Sentry","Kuning","Merah","Biru","Biru"],
  ["Konoha Sentry","Hijau","Hijau","Biru","Merah"],
  ["Karui","Kuning","Hijau","Merah","Hijau"],
  ["Kimada","Hijau","Kuning","Biru","Biru"],
  ["Konohamaru","Kuning","Hijau","Hijau","Biru"],
  ["Misthide Guard","Biru","Biru","Kuning","Merah"],
  ["Sandhide Sentry","Hijau","Hijau","Kuning","Merah"],
  ["Omoi","Kuning","Biru","Kuning","Merah"],
  ["Misthide Sentry","Hijau","Merah","Biru","Hijau"],
  ["Mizuki","Kuning","Biru","Merah","Biru"],
  ["Sandhide Guard","Hijau","Merah","Biru","Biru"],
  ["Temari","Hijau","Biru","Hijau","Kuning"],
  ["Iruka","Hijau","Kuning","Merah","Biru"],
  ["Kankuro","Biru","Kuning","Hijau","Kuning"],
  ["Lee","Merah","Biru","Biru","Merah"],
  ["Shikamaru","Merah","Hijau","Kuning","Biru"],
  ["Nenji","Kuning","Hijau","Biru","Merah"],
  ["Sasuke","Kuning","Merah","Biru","Hijau"],
  ["Hinata","Kuning","Biru","Biru","Biru"],
  ["Shizune","Hijau","Hijau","Biru","Kuning"],
  ["Kiba Inuzuka","Biru","Biru","Merah","Merah"],
  ["Shino","Hijau","Hijau","Biru","Biru"],
  ["Tenten","Kuning","Merah","Biru","Biru"],
  ["Ino","Biru","Hijau","Merah","Hijau"],
  ["Naruto","Kuning","Hijau","Hijau","Merah"],
  ["Choji","Hijau","Biru","Hijau","Hijau"],
  ["Sakura","Biru","Biru","Merah","Kuning"],
  ["Kabuto","Hijau","Biru","Biru","Merah"],
  ["Karin","Merah","Hijau","Hijau","Biru"],
  ["Jugo","Merah","Merah","Biru","Biru"],
  ["Kimimaro","Merah","Biru","Biru","Merah"],
  ["Sakon and Ukon","Kuning","Hijau","Hijau","Biru"],
  ["Sai","Hijau","Merah","Kuning","Biru"],
  ["Suigetsu","Biru","Merah","Biru","Kuning"],
  ["Jirobo","Biru","Hijau","Hijau","Biru"],
  ["Tayuya","Hijau","Merah","Hijau","Merah"],
  ["Zabuza","Biru","Merah","Kuning","Biru"],
  ["Gaara","Biru","Merah","Biru","Kuning"],
  ["Haku","Kuning","Kuning","Merah","Merah"],
  ["Kidomaru","Hijau","Kuning","Hijau","Biru"],
  ["Raido Ashinami","Kuning","Hijau","Biru","Hijau"],
  ["Gekkou Hayate","Kuning","Merah","Biru","Kuning"],
  ["Genma Shiranui","Merah","Hijau","Kuning","Merah"],
  ["Anko Mitarashi","Hijau","Merah","Merah","Kuning"],
  ["Aoba Yamashiro","Biru","Merah","Biru","Biru"],
  ["Ebisu","Biru","Merah","Merah","Biru"],
  ["Ibiki","Hijau","Hijau","Merah","Kuning"],
  ["Darui","Kuning","Merah","Biru","Biru"],
  ["Danzo","Hijau","Biru","Hijau","Merah"],
  ["Hanzo","Merah","Hijau","Biru","Biru"],
  ["Ao","Biru","Merah","Kuning","Hijau"],
  ["Chojuro","Merah","Merah","Hijau","Hijau"],
  ["Kisame","Kuning","Biru","Biru","Merah"],
  ["Zetsu","Kuning","Hijau","Biru","Merah"],
  ["Deidara","Kuning","Merah","Merah","Kuning"],
  ["Konan","Biru","Kuning","Kuning","Kuning"],
  ["Sasori","Hijau","Merah","Biru","Merah"],
  ["Hidan","Biru","Biru","Biru","Hijau"],
  ["Kakuzu","Hijau","Hijau","Biru","Hijau"],
  ["Seven Tails Jinchuriki","Biru","Hijau","Hijau","Biru"],
  ["Four Tails Jinchuriki","Kuning","Merah","Merah","Biru"],
  ["Six Tails Jinchuriki","Kuning","Biru","Biru","Merah"],
  ["Five Tails Jinchuriki","Hijau","Kuning","Hijau","Hijau"],
  ["Granny Chiyo","Kuning","Merah","Biru","Hijau"],
  ["Three Tails Jinchuriki","Merah","Biru","Hijau","Merah"],
  ["Two Tails Jinchuriki","Merah","Merah","Kuning","Hijau"],
  ["Yamato","Biru","Biru","Hijau","Biru"],
  ["Yuuhi Kurenai","Kuning","Merah","Biru","Kuning"],
  ["Asuma","Biru","Merah","Hijau","Kuning"],
  ["Baki","Merah","Hijau","Merah","Merah"],
  ["Cursed Seal Sasuke","Merah","Biru","Kuning","Merah"],
  ["Kazekage Gaara","Kuning","Hijau","Biru","Merah"],
  ["Obito","Hijau","Biru","Hijau","Hijau"],
  ["2nd Mizukage","Hijau","Kuning","Hijau","Biru"],
  ["Onoki","Biru","Biru","Biru","Biru"],
  ["A","Merah","Merah","Merah","Merah"],
  ["Mu","Hijau","Hijau","Kuning","Hijau"],
  ["Orochimaru","Merah","Kuning","Merah","Biru"],
  ["Jiraiya","Biru","Kuning","Merah","Hijau"],
  ["Mei Terumi","Kuning","Hijau","Hijau","Kuning"],
  ["Tsunade","Hijau","Hijau","Hijau","Hijau"],
  ["4th Kazekage","Biru","Merah","Biru","Hijau"],
  ["Kinkaku","Merah","Merah","Kuning","Kuning"],
  ["3rd Raikage","Biru","Hijau","Merah","Merah"],
  ["Guy","Merah","Kuning","Merah","Kuning"],
  ["Itachi","Kuning","Merah","Merah","Merah"],
  ["Kakashi","Kuning","Biru","Merah","Merah"],
  ["Ginkaku","Hijau","Kuning","Hijau","Merah"],
  ["Tobi","Hijau","Biru","Kuning","Merah"],
  ["Kabuto Yakushi","Hijau","Merah","Hijau","Merah"],
  ["Pain","Kuning","Hijau","Merah","Hijau"],
  ["Sage Naruto","Merah","Biru","Merah","Kuning"],
  ["Killer Bee","Hijau","Kuning","Kuning","Merah"],
  ["Boruto","Hijau","Biru","Kuning","Merah"],
  ["Six Path Madara","Merah","Merah","Merah","Merah"],
  ["Mangekyo Sasuke","Merah","Merah","Merah","Kuning"],
  ["Nine Tails Naruto","Hijau","Merah","Merah","Merah"],
  ["Six Paths Obito","Merah","Merah","Kuning","Hijau"],
  ["Hashirama","Biru","Merah","Merah","Biru"],
  ["Madara","Biru","Hijau","Merah","Merah"],
  ["Gaara Shinobi Commander","Kuning","Merah","Hijau","Kuning"],
  ["Jigen","Kuning","Merah","Biru","Hijau"],
  ["Tobirama","Kuning","Merah","Kuning","Biru"],
  ["3rd Hokage","Kuning","Hijau","Merah","Merah"],
  ["Minato","Kuning","Kuning","Kuning","Kuning"],
  ["Kakashi Double Sharingan","Biru","Merah","Hijau","Hijau"],
  ["Garo","Merah","Kuning","Hijau","Merah"],
  ["Amado","Biru","Hijau","Merah","Kuning"],
  ["Otsutsuki Isshiki","Hijau","Merah","Kuning","Hijau"],
  ["Byron Naruto","Biru","Hijau","Biru","Kuning"],
  ["Jigen Karma Mode","Kuning","Biru","Merah","Kuning"],
  ["Otsutsuki Kaguya","Merah","Kuning","Hijau","Kuning"],
  ["Rinegan Sasuke","Kuning","Merah","Hijau","Kuning"],
  ["Boruto Karma Mode","Hijau","Biru","Biru","Merah"],
  ["Kawaki","Biru","Kuning","Merah","Kuning"],
  ["Otsutsuki Momoshiki","Kuning","Biru","Hijau","Merah"],
  ["Kashin Koji","Hijau","Merah","Merah","Biru"],
  ["Sage Mitsuki","Biru","Biru","Kuning","Merah"],
  ["Boro","Merah","Hijau","Biru","Kuning"],
  ["Deruta","Hijau","Kuning","Merah","Biru"],
  ["Uchiha Sarada","Merah","Hijau","Hijau","Biru"]
]

print("\n--- Ninja Heroes Deploy ---")
print("by fb.com/tontasy || tontasy#4986\n")

ninja = [[None, None, None, None, None], [None, None, None, None, None], [None, None, None, None, None], [None, None, None, None, None], [None, None, None, None, None], [None, None, None, None, None], [None, None, None, None, None], [None, None, None, None, None], [None, None, None, None, None], [None, None, None, None, None], [None, None, None, None, None], [None, None, None, None, None]]
ninjautama = [[None, None, None, None, None], [None, None, None, None, None], [None, None, None, None, None]]

for i in range(12):
    ulang = True

    while ulang:
        ninja[i][0] = input(f"Nama Ninja Deploy {i + 1}: ")

        for j in range(len(dataninja)):
            if ninja[i][0] in dataninja[j] and ulang:
                ulang = False
                ninja[i] = dataninja[j]
                break
        
        if ulang: print("Nama tidak ditemukan")

for i in range(3):
    ulang = True

    while ulang:
        ninjautama[i][0] = input(f"Nama Ninja Utama Slot {i + 1}: ")

        for j in range(len(dataninja)):
            if ninjautama[i][0] in dataninja[j] and ulang:
                ulang = False
                ninjautama[i] = dataninja[j]
                break
    
        if ulang: print("Nama tidak ditemukan")

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
nu = [ninjautama[0], ninjautama[1], ninjautama[2]]

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
    
    if i[1][3] == nu[0][1]:
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
    
    if i[2][3] == nu[1][1]:
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

    if i[3][3] == nu[2][1]:
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
    
    if i[5][2] == nu[0][4]:
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
    
    if i[6][4] == nu[2][2]:
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
    
    if i[8][1] == nu[0][3]:
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
    
    if i[9][1] == nu[1][3]:
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

    if i[10][1] == nu[2][3]:
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
    
    if nu[0][2] == nu[1][4]:
        if nu[0][2] == m:
            prio["At"][1] += 10
        elif nu[0][2] == b:
            prio["D"][1] += 10
        elif nu[0][2] == h:
            prio["HP"][1] += 10
        elif nu[0][2] == k:
            prio["Ag"][1] += 10

    if nu[1][2] == nu[2][4]:
        if nu[1][2] == m:
            prio["At"][1] += 10
        elif nu[1][2] == b:
            prio["D"][1] += 10
        elif nu[1][2] == h:
            prio["HP"][1] += 10
        elif nu[1][2] == k:
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
    
    if index == 4790016:
        end = time.time()
        print(f"estimasi waktu: {round((end - start) * 100 / 60)} menit")
        print(f"waktu terlampaui: {round((end - start) / 60)} menit", end="\r")
    
    if index == 47900160:
        end = time.time()
        print(f"waktu terlampaui: {round((end - start) / 60)} menit", end="\r")

    if index == 47900160*2:
        end = time.time()
        print(f"waktu terlampaui: {round((end - start) / 60)} menit", end="\r")

    if index == 47900160*3:
        end = time.time()
        print(f"waktu terlampaui: {round((end - start) / 60)} menit", end="\r")

    if index == 47900160*4:
        end = time.time()
        print(f"waktu terlampaui: {round((end - start) / 60)} menit", end="\r")

    if index == 47900160*5:
        end = time.time()
        print(f"waktu terlampaui: {round((end - start) / 60)} menit", end="\r")

    if index == 47900160*6:
        end = time.time()
        print(f"waktu terlampaui: {round((end - start) / 60)} menit", end="\r")

    if index == 47900160*7:
        end = time.time()
        print(f"waktu terlampaui: {round((end - start) / 60)} menit", end="\r")
    
    if index == 47900160*8:
        end = time.time()
        print(f"waktu terlampaui: {round((end - start) / 60)} menit", end="\r")
        
    if index == 47900160*9:
        end = time.time()
        print(f"waktu terlampaui: {round((end - start) / 60)} menit", end="\n")

    if index == 47900160*10:
        end = time.time()
        print(f"waktu terlampaui: {round((end - start) / 60)} menit")
        print(f"selesai")
        
print("--- Atribut ---")
print("Attack:", prio["At"][0])
print("Defense:", prio["D"][0])
print("HP:", prio["HP"][0] * 5)
print("Agility:", prio["Ag"][0])
print("--- Deploy ---")
print("Baris 1:", deploy[0][0], ",", deploy[1][0], ",", deploy[2][0], ",", deploy[3][0], ",", deploy[4][0])
print("Baris 2:", deploy[5][0], ",", nu[0][0], ",", nu[1][0], ",", nu[2][0], ",", deploy[6][0])
print("Baris 3:", deploy[7][0], ",", deploy[8][0], ",", deploy[9][0], ",", deploy[10][0], ",", deploy[11][0])