import random

def jatek():
    print("Üdvözölek a Kő, Papír, Olló játékban!")


    győzelmek = 0
    vesztések = 0
    döntetlenek = 0

    while True:

        valasztas = input("Válasz karaktert: Kő, Papír, Olló -> ").strip().lower()

        if valasztas not in ["kő", "papír", "olló"]:
            print("Érvénytelen választás! Kérlek, válassz a 'kő', 'papír' vagy 'olló' közül.")
            continue

        gep_valasztasa = random.choice(["kő", "papír", "olló"])
        print(f"Gép választása: {gep_valasztasa}")

        if valasztas == gep_valasztasa:
            print("Döntetlen!")
            döntetlenek += 1
        elif (valasztas == "kő" and gep_valasztasa == "olló") or \
             (valasztas == "papír" and gep_valasztasa == "kő") or \
             (valasztas == "olló" and gep_valasztasa == "papír"):
            print("Nyertél!")
            győzelmek += 1
        else:
            print("Vesztettél!")
            vesztések += 1

        print(f"nyerések: {győzelmek}, vesztések: {vesztések}, döntetlenek: {döntetlenek}")

        válasz = input("Akarsz még játszani? (i/n) ").strip().lower()
        if válasz != 'i':
            print(f"Köszönjük a játékot! A végső eredmény: {győzelmek} győzelem, {vesztések} vereség, {döntetlenek} döntetlen.")
            break

jatek()