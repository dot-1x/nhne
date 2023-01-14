from itertools import combinations, permutations
from math import comb, perm
from time import time

ninja = [
  ["Flameplate Brigand","Hijau","Biru","Kuning","Merah"],
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
  ["Six Paths Madara","Merah","Merah","Merah","Merah"],
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
comboskill = [
  ["Team 7",0,0,0,0,"Naruto","Sakura","Sasuke"],
  ["Uchiha Clan",8,0,0,0,"Sasuke","Itachi","Obito","Madara"],
  ["Team 3",0,0,0,0,"Tenten","Lee","Nenji"],
  ["Team 10",0,0,0,0,"Ino","Choji","Shikamaru"],
  ["Team 8",0,0,0,0,"Hinata","Kiba Inuzuka","Shino"],
  ["Ramen Mentor and Apprentice",0,0,5,0,"Naruto","Iruka"],
  ["Duo Patrol",2,0,0,0,"Konoha Guard","Konoha Sentry"],
  ["Sarutobi Clan",4,0,0,0,"3rd Hokage","Asuma","Konohamaru"],
  ["Teacher Comes",0,0,0,0,"Kakashi","Guy","Asuma","Yuuhi Kurenai"],
  ["Hidden Sand Squad",0,0,0,0,"Gaara","Temari","Kankuro"],
  ["Special Jonin",12,0,0,0,"Ebisu","Ibiki","Gekkou Hayate","Aoba Yamashiro","Genma Shiranui","Anko Mitarashi"],
  ["Till Death",0,4,0,0,"Zabuza","Haku"],
  ["Hidden Sound Squad",0,0,0,0,"Kidomaru","Tayuya","Sakon and Ukon","Jirobo","Kimimaro"],
  ["I am a Girl",0,0,0,8,"Sakura","Ino","Tenten","Hinata","Temari","Shizune","Anko Mitarashi","Yuuhi Kurenai"],
  ["Konoha 12 Ninjas",10,10,10,10,"Naruto","Sakura","Sasuke","Tenten","Lee","Nenji","Ino","Choji","Shikamaru","Hinata","Kiba Inuzuka","Shino"],
  ["Worthy Opponent",3,0,0,0,"Naruto","Sasuke","Lee","Gaara"],
  ["Hyuga Clan",0,4,0,0,"Hinata","Nenji"],
  ["Hokage Anbu",0,0,0,0,"Danzo","Sai","Anbu Guard","Anbu Sentry"],
  ["Passerby",4,4,4,4,"Mizuki","Flameplate Brigand","Yoroi","Tsurugi Misumi","Kimada"],
  ["Secret Love?",0,4,0,0,"Hinata","Naruto"],
  ["Team Hawk",0,0,5,0,"Sasuke","Suigetsu","Karin","Jugo"],
  ["Power of the Cursed Seal",3,0,0,0,"Cursed Seal Sasuke","Jugo"],
  ["Almost Lover",0,5,0,0,"Yuuhi Kurenai","Asuma"],
  ["Naruto's Mentor",0,0,0,10,"Iruka","Kakashi","Yamato"],
  ["Wind Kingdom",0,10,0,0,"Gaara","Temari","Kankuro","Sasori","Baki","Granny Chiyo","4th Kazekage"],
  ["Puppeteer ",4,0,0,0,"Granny Chiyo","Sasori","Kankuro"],
  ["Tailed Beast Jinchuriki",10,10,10,10,"Gaara","Two Tails Jinchuriki","Three Tails Jinchuriki","Four Tails Jinchuriki","Five Tails Jinchuriki","Six Tails Jinchuriki","Seven Tails Jinchuriki","Killer Bee","Naruto"],
  ["Akatsuki",12,0,0,0,"Tobi","Zetsu","Pain","Konan","Itachi","Kisame","Orochimaru","Deidara","Sasori","Hidan","Kakuzu"],
  ["Power of the Nine Tails",8,0,0,0,"Naruto","Sage Naruto","Nine Tails Naruto"],
  ["Mystery Man",0,15,0,0,"Tobi","Obito","Six Paths Obito"],
  ["Nemesis",0,0,0,8,"Itachi","Orochimaru"],
  ["Thunder Kingdom",0,0,0,13,"A","Killer Bee","3rd Raikage","Darui"],
  ["Group of Zombies",0,0,0,0,"Mu","Hanzo","2nd Mizukage","3rd Raikage","4th Kazekage","3rd Hokage"],
  ["Fire's Will",12,0,0,0,"Hashirama","Tobirama","3rd Hokage","Minato","Tsunade"],
  ["Seven Swordsman of the Mist",4,0,0,0,"Zabuza","Suigetsu","Kisame"],
  ["Orochi",0,0,5,0,"Orochimaru","Kabuto","Kabuto Yakushi"],
  ["Mizukage Team",0,0,0,0,"Mei Terumi","Ao","Chojuro"],
  ["Five Kages",9,9,9,9,"Tsunade","A","Mei Terumi","Onoki","Kazekage Gaara"],
  ["Three Ninjas",6,6,6,6,"Jiraiya","Tsunade","Orochimaru"],
  ["Bloodboil Youth",4,0,0,0,"Lee","Guy"],
  ["Love Love Paradise",0,0,7,0,"Jiraiya","Kakashi"],
  ["The Same Eyes",0,0,0,7,"Kakashi","Obito"],
  ["Child of Destiny",0,7,0,0,"Pain","Sage Naruto"],
  ["Past Team",0,0,10,0,"Minato","Kakashi","Obito"],
  ["The First Generation",5,5,5,5,"Hashirama","Madara"],
  ["Lonely Childhood",0,7,0,0,"Naruto","Gaara","Haku","Kimimaro"],
  ["Female Go-getter",0,0,0,0,"Yuuhi Kurenai","Mei Terumi","Tsunade"],
  ["Secret Love Alliance",0,0,4,0,"Hinata","Karin"],
  ["Get Bento",0,0,10,0,"Zabuza","Kimimaro","Itachi","Asuma","Pain"],
  ["Hokage Candidate",0,9,0,0,"Danzo","Kakashi","Sage Naruto"],
  ["Tailed Beast Hunters",0,0,0,0,"Deidara","Sasori","Kakuzu","Hidan","Itachi","Kisame"],
  ["Raikage Team",0,0,0,0,"A","Killer Bee","Darui"],
  ["Body Guard",0,0,0,0,"Darui","Ao","Chojuro","Temari","Kankuro"],
  ["10 Years of Naruto",10,10,10,10,"Naruto","Sasuke","Sage Naruto","Cursed Seal Sasuke","Nine Tails Naruto","Mangekyo Sasuke"],
  ["Golden Bachelor",0,0,0,0,"Kazekage Gaara","Kakashi","Killer Bee"],
  ["Planet of the Apes",0,0,6,0,"3rd Hokage","Four Tails Jinchuriki"],
  ["I have a mount",0,0,0,5,"Deidara","Sai","Kiba Inuzuka"],
  ["Sage status",5,0,0,0,"Sage Naruto","Kabuto Yakushi"],
  ["Old Man",0,0,0,0,"3rd Hokage","Onoki","Danzo","Granny Chiyo"],
  ["Undying Shell",0,0,6,0,"Sasori","Kakuzu","Pain"],
  ["Medic Ninja",0,0,8,0,"Sakura","Shizune","Tsunade","Kabuto","Granny Chiyo","Karin"],
  ["Gold and Silver Brothers",0,7,0,0,"Kinkaku","Ginkaku"],
  ["A pot of balls",5,5,5,5,"Konohamaru","Shikamaru","Kidomaru","Orochimaru"],
  ["Hokage Traitor",0,0,0,0,"Orochimaru","Kabuto","Cursed Seal Sasuke","Itachi","Mizuki"],
  ["Instant kill",0,0,0,4,"Baki","Gekkou Hayate"],
  ["Death Debt",0,8,0,0,"Pain","Konan","Hanzo"],
  ["Cell of the First Hokage",0,0,14,0,"Hashirama","Six Paths Madara","Orochimaru","Kabuto Yakushi"],
  ["Traceless",0,0,0,10,"Zetsu","Tobi","Minato"],
  ["Full Brother",0,0,0,0,"Sasuke","Itachi","A","Killer Bee"],
  ["Kazekage Team",0,0,0,0,"Kazekage Gaara","Temari","Kankuro"],
  ["Die Together",0,0,0,0,"Mu","2nd Mizukage"],
  ["Apprenticeship",0,0,0,0,"Jiraiya","Pain","Konan"],
  ["Mangekyo",0,0,0,0,"Mangekyo Sasuke","Madara","Obito","Kakashi","Itachi"],
  ["The Rinnegan",8,8,8,8,"Pain","Six Paths Obito","Six Paths Madara"],
  ["Boruto Team 7",0,0,15,15,"Boruto Karma Mode","Uchiha Sarada","Sage Mitsuki"],
  ["Sasuke Family",0,0,0,14,"Uchiha Sarada","Rinegan Sasuke","Sakura"],
  ["Ootsuki Clan",11,11,11,11,"Otsutsuki Momoshiki","Otsutsuki Kaguya","Otsutsuki Isshiki"],
  ["Naruto Family",0,0,16,0,"Hinata","Byron Naruto","Boruto"],
  ["Kara Member",17,17,17,17,"Kashin Koji","Kawaki","Deruta","Boro","Garo","Jigen","Jigen Karma Mode","Amado"],
  ["Step Brother",0,15,0,0,"Boruto","Kawaki"],
  ["Karma Brother",18,0,0,0,"Kawaki","Boruto Karma Mode"],
  ["New Father and Son",16,0,0,16,"Byron Naruto","Kawaki","Boruto Karma Mode"],
  ["Uchiha Revenger",0,0,0,9,"Sasuke","Cursed Seal Sasuke","Mangekyo Sasuke","Rinegan Sasuke"],
  ["More than Blood",0,0,8,0,"Orochimaru","Kabuto Yakushi","Sage Mitsuki"],
  ["Nanadaime Path",11,0,0,0,"Naruto","Sage Naruto","Nine Tails Naruto","Byron Naruto"],
  ["Kurama Sacrifice",16,0,0,0,"Byron Naruto","Otsutsuki Isshiki"],
  ["Moon Eye Plan",0,15,15,0,"Six Paths Madara","Otsutsuki Kaguya","Six Paths Obito"],
  ["Hokage and Shadow",13,0,13,0,"Rinegan Sasuke","Byron Naruto"],
  ["Time Travel",0,0,9,9,"Rinegan Sasuke","Jiraiya","Boruto","Naruto"],
  ["Rokudaime Path",10,0,10,0,"Kakashi","Kakashi Double Sharingan"],
  ["Senju Clan",0,0,15,0,"Hashirama","Tobirama","Tsunade"],
  ["Perfect Clone",7,0,7,7,"Jiraiya","Kashin Koji"],
  ["Searching My Real Mother",0,0,10,0,"Uchiha Sarada","Sakura","Karin"],
  ["Creator Human Weapon",12,12,12,0,"Amado","Deruta","Kashin Koji"],
  ["Allied Shinobi Forces",8,8,8,8,"Gaara Shinobi Commander","Tsunade","Mei Terumi","A","Onoki"]
]

ninjateam = []
ninjadeploy = []

def kalkulasicomboskill():
    global ninjateam, ninjadeploy

    ownedcomboskill = []
    calonninjadeploy = []
    atributprioritas = [[], []]
    nilaiatributprioritas = 0

    while True:
        atributprioritas[0] = input("Atribut Combo Skill Utama (HP/Attack/Agility/Defense): ")

        if {atributprioritas[0]} <= {"HP", "Attack", "Agility", "Defense"}:
            if atributprioritas[0] == "HP":
                atributprioritas[1] = 3
            elif atributprioritas[0] == "Attack":
                atributprioritas[1] = 1
            elif atributprioritas[0] == "Agility":
                atributprioritas[1] = 4
            elif atributprioritas[0] == "Defense":
                atributprioritas[1] = 2
            break
        else:
            print("Atribut tidak diketahui")

    print(f"\nTidak semua combo skill akan dikalkulasi, akan tetapi hanya combo skill yang memiliki persentase atribut {atributprioritas[0]}")
    input("Tekan Enter untuk melanjutkan...")

    print("")
    for i in comboskill:
        if i[atributprioritas[1]] == 0:
            continue

        while True:
            yn = input(f"Punya combo skill {i[0]} (y/n)? ")

            if yn == "y":
                ownedcomboskill.append(i)
                break
            elif yn == "n":
                break
            else:
                print("Input tidak diketahui")

    for i in ownedcomboskill:
        calonninjadeploy += i[5:]
        calonninjadeploy = [*set(calonninjadeploy)]

    calonninjadeploy = list(set(calonninjadeploy) - set(ninjateam))

    if len(calonninjadeploy) < 12: print("Kekurangan ninja") and quit()
    kombinasi = combinations(calonninjadeploy, 12)

    waktuawal = time()
    for index, i in enumerate(kombinasi):
        i = set(list(i) + ninjateam)
        activecomboskill = []
        nilaiatributprioritasawal = 0

        for j in ownedcomboskill:
            if set(j[5:]) <= i:
                activecomboskill.append(j)

        for j in activecomboskill:
            nilaiatributprioritasawal += j[atributprioritas[1]]

            if nilaiatributprioritasawal >= nilaiatributprioritas:
                nilaiatributprioritas = nilaiatributprioritasawal
                ninjadeploy = i

        hitungwaktu = True
        if hitungwaktu and index + 1 == round(comb(len(calonninjadeploy), 12) / 100):
            print(f"\nEstimasi waktu: {round((time() - waktuawal) * 100 / 60)} menit")
            print("Harap tunggu...\n")
            hitungwaktu = False

    ninjadeploy = list(ninjadeploy - set(ninjateam))

    print("--- Atribut ---")
    print(f"{atributprioritas[0]}: {nilaiatributprioritas}%")
    print("---- Ninja ----")
    for i in ninjadeploy:
        print(i)
    for i in ninjateam:
        print(i)
def kalkulasideploy():
    global ninjateam, ninjadeploy
    prioritas = [None, None, None, None]
    nilaiprioritas = {
        "HP": [0, 0],
        "Attack": [0, 0],
        "Agility": [0, 0],
        "Defense": [0, 0]
    }
    deploy = None

    for index, i in enumerate(ninjadeploy):
        for j in ninja:
            if i in j:
                ninjadeploy[index] = j

    for index, i in enumerate(ninjateam):
        for j in ninja:
            if i in j:
                ninjateam[index] = j

    while True:
        prioritas = input("Prioritas 1  (Contoh: HP>Attack>Agility>Defense): ").split(">")

        if set(prioritas) == {"HP", "Attack", "Agility", "Defense"}:
            break
        else:
            print("Tidak sesuai")

    permutasi = permutations(ninjadeploy)

    waktuawal = time()
    for index, i in enumerate(permutasi):
        nilaiprioritastotal = nilaiprioritas["HP"][0] + nilaiprioritas["Attack"][0] + nilaiprioritas["Agility"][0] + nilaiprioritas["Defense"][0]

        if i[0][2] == i[1][4]:
            if i[0][2] == "Merah":
                nilaiprioritas["Attack"][1] += 10
            elif i[0][2] == "Biru":
                nilaiprioritas["Defense"][1] += 10
            elif i[0][2] == "Hijau":
                nilaiprioritas["HP"][1] += 10
            elif i[0][2] == "Kuning":
                nilaiprioritas["Agility"][1] += 10

        if i[1][2] == i[2][4]:
            if i[1][2] == "Merah":
                nilaiprioritas["Attack"][1] += 10
            elif i[1][2] == "Biru":
                nilaiprioritas["Defense"][1] += 10
            elif i[1][2] == "Hijau":
                nilaiprioritas["HP"][1] += 10
            elif i[1][2] == "Kuning":
                nilaiprioritas["Agility"][1] += 10

        if i[1][3] == ninjateam[0][1]:
            if i[1][3] == "Merah":
                nilaiprioritas["Attack"][1] += 10
            elif i[1][3] == "Biru":
                nilaiprioritas["Defense"][1] += 10
            elif i[1][3] == "Hijau":
                nilaiprioritas["HP"][1] += 10
            elif i[1][3] == "Kuning":
                nilaiprioritas["Agility"][1] += 10

        if i[2][2] == i[3][4]:
            if i[2][2] == "Merah":
                nilaiprioritas["Attack"][1] += 10
            elif i[2][2] == "Biru":
                nilaiprioritas["Defense"][1] += 10
            elif i[2][2] == "Hijau":
                nilaiprioritas["HP"][1] += 10
            elif i[2][2] == "Kuning":
                nilaiprioritas["Agility"][1] += 10

        if i[2][3] == ninjateam[1][1]:
            if i[2][3] == "Merah":
                nilaiprioritas["Attack"][1] += 10
            elif i[2][3] == "Biru":
                nilaiprioritas["Defense"][1] += 10
            elif i[2][3] == "Hijau":
                nilaiprioritas["HP"][1] += 10
            elif i[2][3] == "Kuning":
                nilaiprioritas["Agility"][1] += 10

        if i[3][2] == i[4][4]:
            if i[3][2] == "Merah":
                nilaiprioritas["Attack"][1] += 10
            elif i[3][2] == "Biru":
                nilaiprioritas["Defense"][1] += 10
            elif i[3][2] == "Hijau":
                nilaiprioritas["HP"][1] += 10
            elif i[3][2] == "Kuning":
                nilaiprioritas["Agility"][1] += 10

        if i[3][3] == ninjateam[2][1]:
            if i[3][3] == "Merah":
                nilaiprioritas["Attack"][1] += 10
            elif i[3][3] == "Biru":
                nilaiprioritas["Defense"][1] += 10
            elif i[3][3] == "Hijau":
                nilaiprioritas["HP"][1] += 10
            elif i[3][3] == "Kuning":
                nilaiprioritas["Agility"][1] += 10

        if i[5][1] == i[0][3]:
            if i[5][1] == "Merah":
                nilaiprioritas["Attack"][1] += 10
            elif i[5][1] == "Biru":
                nilaiprioritas["Defense"][1] += 10
            elif i[5][1] == "Hijau":
                nilaiprioritas["HP"][1] += 10
            elif i[5][1] == "Kuning":
                nilaiprioritas["Agility"][1] += 10

        if i[5][2] == ninjateam[0][4]:
            if i[5][2] == "Merah":
                nilaiprioritas["Attack"][1] += 10
            elif i[5][2] == "Biru":
                nilaiprioritas["Defense"][1] += 10
            elif i[5][2] == "Hijau":
                nilaiprioritas["HP"][1] += 10
            elif i[5][2] == "Kuning":
                nilaiprioritas["Agility"][1] += 10

        if i[6][1] == i[4][3]:
            if i[6][1] == "Merah":
                nilaiprioritas["Attack"][1] += 10
            elif i[6][1] == "Biru":
                nilaiprioritas["Defense"][1] += 10
            elif i[6][1] == "Hijau":
                nilaiprioritas["HP"][1] += 10
            elif i[6][1] == "Kuning":
                nilaiprioritas["Agility"][1] += 10

        if i[6][4] == ninjateam[2][2]:
            if i[6][4] == "Merah":
                nilaiprioritas["Attack"][1] += 10
            elif i[6][4] == "Biru":
                nilaiprioritas["Defense"][1] += 10
            elif i[6][4] == "Hijau":
                nilaiprioritas["HP"][1] += 10
            elif i[6][4] == "Kuning":
                nilaiprioritas["Agility"][1] += 10

        if i[7][1] == i[5][3]:
            if i[7][1] == "Merah":
                nilaiprioritas["Attack"][1] += 10
            elif i[7][1] == "Biru":
                nilaiprioritas["Defense"][1] += 10
            elif i[7][1] == "Hijau":
                nilaiprioritas["HP"][1] += 10
            elif i[7][1] == "Kuning":
                nilaiprioritas["Agility"][1] += 10

        if i[7][2] == i[8][4]:
            if i[7][2] == "Merah":
                nilaiprioritas["Attack"][1] += 10
            elif i[7][2] == "Biru":
                nilaiprioritas["Defense"][1] += 10
            elif i[7][2] == "Hijau":
                nilaiprioritas["HP"][1] += 10
            elif i[7][2] == "Kuning":
                nilaiprioritas["Agility"][1] += 10

        if i[8][1] == ninjateam[0][3]:
            if i[8][1] == "Merah":
                nilaiprioritas["Attack"][1] += 10
            elif i[8][1] == "Biru":
                nilaiprioritas["Defense"][1] += 10
            elif i[8][1] == "Hijau":
                nilaiprioritas["HP"][1] += 10
            elif i[8][1] == "Kuning":
                nilaiprioritas["Agility"][1] += 10

        if i[8][2] == i[9][4]:
            if i[8][2] == "Merah":
                nilaiprioritas["Attack"][1] += 10
            elif i[8][2] == "Biru":
                nilaiprioritas["Defense"][1] += 10
            elif i[8][2] == "Hijau":
                nilaiprioritas["HP"][1] += 10
            elif i[8][2] == "Kuning":
                nilaiprioritas["Agility"][1] += 10

        if i[9][1] == ninjateam[1][3]:
            if i[9][1] == "Merah":
                nilaiprioritas["Attack"][1] += 10
            elif i[9][1] == "Biru":
                nilaiprioritas["Defense"][1] += 10
            elif i[9][1] == "Hijau":
                nilaiprioritas["HP"][1] += 10
            elif i[9][1] == "Kuning":
                nilaiprioritas["Agility"][1] += 10

        if i[9][2] == i[10][4]:
            if i[9][2] == "Merah":
                nilaiprioritas["Attack"][1] += 10
            elif i[9][2] == "Biru":
                nilaiprioritas["Defense"][1] += 10
            elif i[9][2] == "Hijau":
                nilaiprioritas["HP"][1] += 10
            elif i[9][2] == "Kuning":
                nilaiprioritas["Agility"][1] += 10

        if i[10][1] == ninjateam[2][3]:
            if i[10][1] == "Merah":
                nilaiprioritas["Attack"][1] += 10
            elif i[10][1] == "Biru":
                nilaiprioritas["Defense"][1] += 10
            elif i[10][1] == "Hijau":
                nilaiprioritas["HP"][1] += 10
            elif i[10][1] == "Kuning":
                nilaiprioritas["Agility"][1] += 10

        if i[10][2] == i[11][4]:
            if i[10][2] == "Merah":
                nilaiprioritas["Attack"][1] += 10
            elif i[10][2] == "Biru":
                nilaiprioritas["Defense"][1] += 10
            elif i[10][2] == "Hijau":
                nilaiprioritas["HP"][1] += 10
            elif i[10][2] == "Kuning":
                nilaiprioritas["Agility"][1] += 10

        if i[11][1] == i[6][3]:
            if i[11][1] == "Merah":
                nilaiprioritas["Attack"][1] += 10
            elif i[11][1] == "Biru":
                nilaiprioritas["Defense"][1] += 10
            elif i[11][1] == "Hijau":
                nilaiprioritas["HP"][1] += 10
            elif i[11][1] == "Kuning":
                nilaiprioritas["Agility"][1] += 10

        if ninjateam[0][2] == ninjateam[1][4]:
            if ninjateam[0][2] == "Merah":
                nilaiprioritas["Attack"][1] += 10
            elif ninjateam[0][2] == "Biru":
                nilaiprioritas["Defense"][1] += 10
            elif ninjateam[0][2] == "Hijau":
                nilaiprioritas["HP"][1] += 10
            elif ninjateam[0][2] == "Kuning":
                nilaiprioritas["Agility"][1] += 10

        if ninjateam[1][2] == ninjateam[2][4]:
            if ninjateam[1][2] == "Merah":
                nilaiprioritas["Attack"][1] += 10
            elif ninjateam[1][2] == "Biru":
                nilaiprioritas["Defense"][1] += 10
            elif ninjateam[1][2] == "Hijau":
                nilaiprioritas["HP"][1] += 10
            elif ninjateam[1][2] == "Kuning":
                nilaiprioritas["Agility"][1] += 10

        nilaiprioritasawaltotal = nilaiprioritas["HP"][1] + nilaiprioritas["Attack"][1] + nilaiprioritas["Agility"][1] + nilaiprioritas["Defense"][1]

        if nilaiprioritasawaltotal > nilaiprioritastotal:
            nilaiprioritas[prioritas[0]][0] = nilaiprioritas[prioritas[0]][1]
            nilaiprioritas[prioritas[1]][0] = nilaiprioritas[prioritas[1]][1]
            nilaiprioritas[prioritas[2]][0] = nilaiprioritas[prioritas[2]][1]
            nilaiprioritas[prioritas[3]][0] = nilaiprioritas[prioritas[3]][1]
            deploy = i
        elif nilaiprioritasawaltotal == nilaiprioritastotal:
            if nilaiprioritas[prioritas[0]][1] > nilaiprioritas[prioritas[0]][0]:
                nilaiprioritas[prioritas[0]][0] = nilaiprioritas[prioritas[0]][1]
                nilaiprioritas[prioritas[1]][0] = nilaiprioritas[prioritas[1]][1]
                nilaiprioritas[prioritas[2]][0] = nilaiprioritas[prioritas[2]][1]
                nilaiprioritas[prioritas[3]][0] = nilaiprioritas[prioritas[3]][1]
                deploy = i
            elif nilaiprioritas[prioritas[0]][1] == nilaiprioritas[prioritas[0]][0]:
                if nilaiprioritas[prioritas[1]][1] > nilaiprioritas[prioritas[1]][0]:
                    nilaiprioritas[prioritas[0]][0] = nilaiprioritas[prioritas[0]][1]
                    nilaiprioritas[prioritas[1]][0] = nilaiprioritas[prioritas[1]][1]
                    nilaiprioritas[prioritas[2]][0] = nilaiprioritas[prioritas[2]][1]
                    nilaiprioritas[prioritas[3]][0] = nilaiprioritas[prioritas[3]][1]
                    deploy = i
                elif nilaiprioritas[prioritas[1]][1] == nilaiprioritas[prioritas[1]][0]:
                    if nilaiprioritas[prioritas[2]][1] > nilaiprioritas[prioritas[2]][0]:
                        nilaiprioritas[prioritas[0]][0] = nilaiprioritas[prioritas[0]][1]
                        nilaiprioritas[prioritas[1]][0] = nilaiprioritas[prioritas[1]][1]
                        nilaiprioritas[prioritas[2]][0] = nilaiprioritas[prioritas[2]][1]
                        nilaiprioritas[prioritas[3]][0] = nilaiprioritas[prioritas[3]][1]
                        deploy = i

        nilaiprioritas["Attack"][1], nilaiprioritas["Defense"][1], nilaiprioritas["HP"][1], nilaiprioritas["Agility"][1] = 0, 0, 0, 0

        hitungwaktu = True
        if hitungwaktu and index + 1 == round(perm(len(ninjadeploy)) / 100):
            print(f"\nEstimasi waktu: {round((time() - waktuawal) * 100 / 60)} menit")
            print("Harap tunggu...\n")
            hitungwaktu = False

    print("--- Atribut ---")
    print("Attack:", nilaiprioritas["Attack"][0])
    print("Defense:", nilaiprioritas["Defense"][0])
    print("HP:", nilaiprioritas["HP"][0] * 5)
    print("Agility:", nilaiprioritas["Agility"][0])
    print("---- Deploy ----")
    print("Baris 1:", deploy[0][0], ",", deploy[1][0], ",", deploy[2][0], ",", deploy[3][0], ",", deploy[4][0])
    print("Baris 2:", deploy[5][0], ",", ninjateam[0][0], ",", ninjateam[1][0], ",", ninjateam[2][0], ",", deploy[6][0])
    print("Baris 3:", deploy[7][0], ",", deploy[8][0], ",", deploy[9][0], ",", deploy[10][0], ",", deploy[11][0])

if __name__ == "__main__":
    print("--------------------------")
    print("Ninja Heroes Deploy Script")
    print("          v2.0.0          ")
    print("--------------------------")
    print("    FB: fb.com/tontasy    ")
    print("     DC: tontasy#4986     \n")

    print("Silahkan masukkan Nama Ninja Team terlebih dahulu")

    for i in range(3):
        while True:
            namaninjateam = input(f"Nama Ninja Team No. {i + 1}: ")

            for j in ninja:
                if namaninjateam in j:
                    ninjateam.append(namaninjateam)

            if len(ninjateam) == i + 1:
                break
            else:
                print("Nama ninja tidak ditemukan")

    print("\nEksekusi Script dilakukan secara urut mulai dari Kalkulasi Combo Skill ke Kalkulasi Deploy")
    while True:
        yn = input("Langsung ke Kalkulasi Deploy (y/n)? ")

        if yn == "y":
            print("")
            for i in range(12):
                while True:
                    namaninjadeploy = input(f"Nama Ninja Deploy {i + 1}: ")

                    for j in ninja:
                        if namaninjadeploy in j:
                            ninjadeploy.append(namaninjadeploy)

                    if len(ninjadeploy) == i + 1:
                        break
                    else:
                        print("Nama ninja tidak ditemukan")

            print("")
            kalkulasideploy()
            print("")
            input("Tekan Enter untuk mengakhiri...")
            break
        elif yn == "n":
            print("")
            kalkulasicomboskill()
            print("")
            input("Tekan Enter untuk melanjutkan...")
            print("")
            kalkulasideploy()
            print("")
            input("Tekan Enter untuk mengakhiri...")
            break
        else:
            print("Perintah tidak diketahui")