import os

# Funkcija za lijepi ispis matrice
def ispis(polje_matrice):
    for i in range(len(polje_matrice)):
        for j in range(len(polje_matrice[i])):
            broj = polje_matrice[i][j]
            if broj == int(broj):
                print(int(broj), end=" ")
            else:
                print(broj, end=" ")
        print()
    print()

# Funkcija za provjeru komutativnosti
def provjeri_komutativnost(polje_matrice1, polje_matrice2):
    def mnozenje_matrica(A, B):
        if len(A[0]) != len(B):
            return None
        rezultat = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
        for i in range(len(A)):
            for j in range(len(B[0])):
                for k in range(len(B)):
                    rezultat[i][j] += A[i][k] * B[k][j]
        return rezultat

    AB = mnozenje_matrica(polje_matrice1, polje_matrice2)
    BA = mnozenje_matrica(polje_matrice2, polje_matrice1)

    if AB is None or BA is None:
        print("Množenje nije komutativno jer jedno od množenja nije moguće.")
        return False

    if AB == BA:
        print("Množenje matrica JE komutativno (A*B = B*A).")
    else:
        print("Množenje matrica NIJE komutativno (A*B ≠ B*A).")

    print("\nA * B:")
    ispis(AB)
    print("B * A:")
    ispis(BA)
    return AB == BA

# Funkcija za unos matrice
def unos_matrice(redovi, stupci, ime="A"):
    matrica = [['X' for _ in range(stupci)] for _ in range(redovi)]
    for i in range(redovi):
        for j in range(stupci):
            matrica[i][j] = float(input(f"Upiši vrijednost za {ime}_{i+1},{j+1}: "))
            os.system('cls' if os.name == 'nt' else 'clear')
            ispis(matrica)
    return matrica

# UNOS PRVE MATRICE
stupci1 = int(input("Koliko stupaca ima prva matrica? "))
retci1 = int(input("Koliko redova želiš u prvoj matrici? "))
print(f"Prva matrica će imati {retci1} redova i {stupci1} stupaca.")
polje_matrice1 = unos_matrice(retci1, stupci1, "A")
print("Uspješno upisana prva matrica")
ispis(polje_matrice1)

# UNOS DRUGE MATRICE
stupci2 = int(input("Koliko stupaca ima druga matrica? "))
retci2 = int(input("Koliko redova želiš u drugoj matrici? "))
print(f"Druga matrica će imati {retci2} redova i {stupci2} stupaca.")
polje_matrice2 = unos_matrice(retci2, stupci2, "B")
print("Uspješno upisana druga matrica")
ispis(polje_matrice2)

# Provjera komutativnosti
provjeri_komutativnost(polje_matrice1, polje_matrice2)
