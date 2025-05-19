#
# Praca domowa
# Wojciech Borowski-Dobrowolski
# 2025-05-19

# Napisz program do obsługi ładowarki paczek. Po uruchomieniu, aplikacja pyta ile paczek chcesz wysłać, a następnie wymaga podania wagi dla każdej z nich.
# Na koniec działania program powinien wyświetlić w podsumowaniu:
#     Liczbę paczek wysłanych
#     Liczbę kilogramów wysłanych
#     Suma "pustych" - kilogramów (brak optymalnego pakowania). Liczba paczek * 20 - liczba kilogramów wysłanych
#     Która paczka miała najwięcej "pustych" kilogramów, jaki to był wynik
# Restrykcje:
#     Waga elementów musi być z przedziału od 1 do 10 kg.
#     Każda paczka może maksymalnie zmieścić 20 kilogramów towaru.
#     W przypadku, jeżeli dodawany element przekroczy wagę towaru, ma zostać dodany do nowej paczki, a obecna wysłana.
#     W przypadku podania wagi elementu mniejszej od 1kg lub większej odl 10kg, dodawanie paczek zostaje zakończone i wszystkie paczki są wysłane. Wyświetlane jest podsumowanie.

# Przykład 1:
#     Ilość elementów: 2
#     Wagi elementów: 7, 9
# Podsumowanie:
#     Wysłano 1 paczkę (7+9)
#     Wysłano 16 kg
#     Suma pustych kilogramów: 4kg
#     Najwięcej pustych kilogramów ma paczka 1 (4kg)
#
# Przykład 2:
#     Ilość elementów: 6
#     Wagi elementów: 3, 6, 5, 8, 2, 3
# Podsumowanie:
#     Wysłano 2 paczki (3+6+5, 8+2+3)
#     Wysłano 27 kg
#     Suma pustych kilogramów: 13kg
#     Najwięcej pustych kilogramów ma paczka 2 (7kg)
#
# Przykład 3:
#     Ilość elementów: 8
#     Wagi elementów: 7, 14
#     Podsumowanie:
#     Wysłano 1 paczkę (7)
#     Wysłano 7 kg
#     Suma pustych kilogramów: 13kg
#     Najwięcej pustych kilogramów ma paczka 13

liczba_elementow_do_wyslania = int(input("Podaj liczbę elementów do wysłania : "))
kg_wyslane = 0
paczka_z_najwiekszymi_pustymi_kg = 0
biezaca_paczka = 0
max_puste_kg = 0
suma_pustych_kg = 0
waga_paczki = 0

for element in range(liczba_elementow_do_wyslania):
    waga_elementu = int(input(f"Podaj wagę {element + 1} elementu : "))

    if waga_elementu < 1 or waga_elementu > 10:
        # waga elementu poza dozwolonym zakresem
        print(f"Waga_elementu {waga_elementu} kg poza dozwolonym zakresem <1,10> kg")
        break
    puste_kg = 20 - waga_paczki
    kg_wyslane += waga_elementu
    if waga_paczki+waga_elementu > 20:
        # zamknięcie poprzedniej paczki
        suma_pustych_kg += puste_kg
        if 20 - waga_paczki > max_puste_kg:
            # weryfikacja pustych kg
            max_puste_kg = puste_kg
            paczka_z_najwiekszymi_pustymi_kg = biezaca_paczka
        # nowa paczka
        biezaca_paczka += 1
        waga_paczki = waga_elementu
    else:
        # dopakowanie bieżącej paczki
        waga_paczki += waga_elementu
# zamknięcie ostatniej paczki
puste_kg = 20 - waga_paczki
suma_pustych_kg += puste_kg
if puste_kg > max_puste_kg:
    # weryfikacja pustych kg
    max_puste_kg = puste_kg
    paczka_z_najwiekszymi_pustymi_kg = biezaca_paczka

# gdy od razu pierwsza paczka nie spełnia kryteriów
if kg_wyslane == 0:
    biezaca_paczka = -1
    suma_pustych_kg = 0
    paczka_z_najwiekszymi_pustymi_kg = -1

print(f"Paczki wysłane : {biezaca_paczka + 1}")
print(f"kg wysłane : {kg_wyslane} kg")
print(f"puste kg : {suma_pustych_kg} kg")
print(f"Paczka z największą liczbą pustych kg : {paczka_z_najwiekszymi_pustymi_kg + 1} ({max_puste_kg} kg)")
