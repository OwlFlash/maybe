
try:
    plik = open("test.txt", "r+")
    plik.write("HELLO")
    plik.close()

except FileNotFoundError as e:
    print(" Plik nie istenieje. utworz plik")
    print(e)
except Exception as e: #chodzi o dziedziczenie
    print("nieznay blad")

print("asdasd")

