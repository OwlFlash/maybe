import os
lista = os.listdir("asd")# wypisuja ci sie wszystkie pliki ktore masz na sciezce- w tym wypadku masz tu ytlk o1 plik 'asdfg'. Jesli dasz C:/Windows - wypisze ci sie wszystko co tam masz
liszt = os.listdir(".")# wyswietl si ewszytsko co mamy - wylistujesz liste plikow i katalogow ktore znajduja sie w danym skrypcie
# nie mozesz zostawic pustego nawiasu, bo wtedy ni eokreslasz zadnej scieszki i wyskoczy Error
# jesli dasz ( ".." ) - to wylistujesz katalog w "góre"- jesli ("../..") to dwa w gore itp.
print(lista)
print(liszt)
print("______________________")

for item in os.listdir("."):
    if os.path.isfile(item): # submoduł
        print("{} jest plikiem". format(item))
    if  os.path.isdir(item):
        print("{} nie jest plikiem".format(item))# dla pewnosci robimy tak z isfile i z isdir, a nie z jednym tylko i else bo jakis element moze nie byc ani plikiem ani katalogiem i bysmy mieli problemos


print("____________________________")


#os.mkdir("pliki")# tworzy foldery
os.rename("plik.txt", "text.txt")# zmienia nazwy oczywiscie
#os.remove("text.txt") # - nie dziala na foldery
os.rmdir("pliki")