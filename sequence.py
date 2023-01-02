"""Ciąg Collatza zdefiniowany jest następująco:
Rozpoczynamy od podanej ze standardowego wejścia liczby x (od 1 do 100).
Jeśli x jest liczbą parzystą, to kolejny wyraz ciągu będzie obliczony jako x/2.
W przeciwnym przypadku kolejny wyraz ciągu będzie równy 3x+1.
W ten sam sposób obliczamy kolejne wyrazy ciągu, aż pojawi się liczba 1.

Napisz program, który wypisze długość ciągu Collatza dla podanego ze standardowego wejścia x.
X może przyjmować wartości od 1 do 100."""
import matplotlib.pyplot as plt

def main():
    number = input("Podaj liczbę z przedziału [1-100]: ")
    seq = []
    seq.append(int(number))
    #print(f"{number}")
    if int(number) >= 1 and int(number) <= 100:
        while number != 1:
            if (int(number) % 2) == 0:
                # print(f"{int(number) / 2}")
                number = int(number) / 2
                seq.append(int(number))
            else:
            # print(f"{3 * (int(number)) + 1}")
                number = 3 * (int(number)) + 1
                seq.append(int(number))

        print(f"seq: {seq}")
        print(f"Max: {max(seq)}")
        print(f"Steps: {len(seq)}")

        plt.plot(seq)
        plt.ylabel("Problem Collatza")
        plt.show()
    else:
        print(f"Zła wartość: [1-100] -> {number}")

if __name__ == "__main__":
    main()