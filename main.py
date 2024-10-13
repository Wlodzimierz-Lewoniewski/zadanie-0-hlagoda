import string

def sortowanie(macierz):
    posortowane_listy = []
    
    for lista in macierz:
        lista_bez_zer = [element for element in lista if element[1] != 0]
        
        n = len(lista_bez_zer)
        for i in range(n):
            for j in range(0, n-i-1):
                if lista_bez_zer[j][1] < lista_bez_zer[j+1][1]:
                    lista_bez_zer[j], lista_bez_zer[j+1] = lista_bez_zer[j+1], lista_bez_zer[j]
        
        posortowane_listy.append(lista_bez_zer)

    reduced_lists = [[sublist[0] for sublist in outer_list] for outer_list in posortowane_listy]
    for i in reduced_lists:
        print(i) 

def zadanie():

    liczba_zdan = int(input("Podaj liczbe zdan \n")).strip()
    zdania = []
    for i in range(0, liczba_zdan):
        zdanie_input = input(f"Podaj {i+1} zdanie: \n").strip()

        zdanie_bez_interpunkcji = zdanie_input.translate(str.maketrans('', '', string.punctuation))
        zdania.append(zdanie_bez_interpunkcji)

    liczba_slow = int(input("Podaj liczbę słów: \n")).strip()
    pusta_macierz = [[[i, 0] for i in range(liczba_zdan)] for _ in range(liczba_slow)]
    for i in range(0, liczba_slow): 
        slowo = input("Podaj słowo: \n").strip()
        for jedno_zdanie in range(0, len(zdania)):
            rozbite_zdanie = zdania[jedno_zdanie].strip().lower().split(" ")
            for j in range(0, len(rozbite_zdanie)):
                if rozbite_zdanie[j] == slowo:
                    pusta_macierz[i][jedno_zdanie][1] += 1

    sortowanie(pusta_macierz)

zadanie()