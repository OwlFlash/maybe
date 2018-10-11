
class Calculator():
 # METORY - FUNKCJE KTORE SA CZESCI AKLASY


    def __init__(self): # metoda magiczna, to taka ktora ma __ przed i po sobie - wykonywne przez pythona
        print("init")

    def __del__(self):
        print("DEL")# służy żeby pozamykac pliki pootwierane

    # def __str__(self):# zwraca reprezenstacje w formie str
         #return "Hello"

    def __len__(self):
        return 5


    def dodaj(self, a, b):
        wynik = a +b
        print(wynik)

    def odejmij(self, a, b):
        wynik = a - b
        print(wynik)


calc = Calculator()# utworzylas obiekt zapisany do zmiennej calc- to tak jakbys stworzyla osobny plik z tymi def (bez self) jak z lekcja z foo.
calc_2 = Calculator()
calc.liczba = 10
calc.liczba += 5
print(calc.liczba)

calc.dodaj(10,15)
calc_2.dodaj(20,20)

calc.odejmij(16,3)
print(len(calc))