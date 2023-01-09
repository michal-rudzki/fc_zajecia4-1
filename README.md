# Napisz program do obsługi ładowarki paczek. Po uruchomieniu, aplikacja pyta ile paczek chcesz wysłać, a następnie wymaga podania wagi dla każdej z nich.

Na koniec działania program powinien wyświetlić w podsumowaniu:

- Liczbę paczek wysłanych
- Liczbę kilogramów wysłanych
- Suma "pustych" - kilogramów (brak optymalnego pakowania).  
  
  __Wzór: Liczba paczek * 20 - liczba kilogramów wysłanych__

- Która paczka miała najwięcej "pustych" kilogramów, jaki to był wynik

## Restrykcje:

* Waga elementów musi być z przedziału od 1 do 10 kg.
* Każda paczka może maksymalnie zmieścić 20 kilogramów towaru.
* W przypadku, jeżeli dodawany element przekroczy wagę towaru, ma zostać dodany do nowej paczki, a obecna wysłana.
* W przypadku podania wagi elementu mniejszej od 1kg lub większej od 10kg, dodawanie paczek zostaje zakończone i wszystkie paczki są wysłane. Wyświetlane jest podsumowanie.

# Przykład 1:

### Ilość elementów: 2
### Wagi elementów: 7, 9

## Podsumowanie:

### Wysłano 1 paczkę (7+9)
### Wysłano 16 kg
### Suma pustych kilogramów: 4kg
### Najwięcej pustych kilogramów ma paczka 1 (4kg)
---
# Przykład 2:

### Ilość elementów: 6
### Wagi elementów: 3, 6, 5, 8, 2, 4

## Podsumowanie:

### Wysłano 2 paczki (3+6+5, 8+2+3)
### Wysłano 27 kg
### Suma pustych kilogramów: 13kg
### Najwięcej pustych kilogramów ma paczka 2 (7kg)
---
# Przykład 3:
Ilość elementów: 8

### Wagi elementów: 7, 14

## Podsumowanie:

### Wysłano 1 paczkę (7)
### Wysłano 7 kg
### Suma pustych kilogramów: 13kg
### Najwięcej pustych kilogramów ma paczka 13
=======
## Ciąg Collatza

Ciąg Collatza zdefiniowany jest następująco:
Rozpoczynamy od podanej ze standardowego wejścia liczby x (od 1 do 100).
Jeśli x jest liczbą parzystą, to kolejny wyraz ciągu będzie obliczony jako x/2.
W przeciwnym przypadku kolejny wyraz ciągu będzie równy 3x+1.
W ten sam sposób obliczamy kolejne wyrazy ciągu, aż pojawi się liczba 1.

Napisz program, który wypisze długość ciągu Collatza dla podanego ze standardowego wejścia x.
X może przyjmować wartości od 1 do 100.

