import copy

from gestionale.core.prodotti import ProdottoRecord

p1 = ProdottoRecord("Laptop", 1200.0)
p2 = ProdottoRecord("Mouse", 20.0)
p3 = ProdottoRecord("Auricolari", 250.0)

carrello = [p1, p2, p3, ProdottoRecord("Tablet", 700.0)]

print("Prodotti nel carrello:")
for i, p in enumerate(carrello):
    print(f"{i}) {p.name} - {p.prezzo_unitario}")

# Aggiungere ad una lista
carrello.append(ProdottoRecord("Monitor", 150.0))

carrello.sort(key=lambda x: x.prezzo_unitario, reverse=True)
print(60*"-")

print("Prodotti nel carrello:")
for i, p in enumerate(carrello):
    print(f"{i+1}) {p.name} - {p.prezzo_unitario}")
print(60*"-")

tot = sum(p.prezzo_unitario for p in carrello)
print (f"Totale del carrello: {tot} euro.")

#Aggiungere
carrello.append(ProdottoRecord("Propdo", 100.0))
carrello.extend([ProdottoRecord("bbb", 250.0),ProdottoRecord("aaa", 150.0) ])
carrello.insert(2, ProdottoRecord("ccc", 200.0))

print(60*"-")
print("Prodotti nel carrello:")
for i, p in enumerate(carrello):
    print(f"{i+1}) {p.name} - {p.prezzo_unitario}")

#Rimuovere
carrello.pop() # rimuove l'ultimo elemento
carrello.pop(2) # rimuove l'elemento in posizione 2
carrello.remove(p1) # elimino la prima occorrenza di p1
#carrello.clear() # elimina tutto

#Sorting
#carrello.sort() # ordina seguendo Ordinamento naturale -- questo non funziona se gli oggetti contenuti non definiscono un metodo __lt__ --
#carrello.sort(reverse=True) # ordina al contrario
#carrello.sort(key= function)
#carrello_ordinato = sorted(carrello)

#Copie ed altro
carrello.reverse() # inverte l'ordine
carrello_copia = carrello.copy() # shallow copy (se modifico p1 del carrello --> modifico anche p1 di carrello_copia)
carrello_copia2 = copy.deepcopy(carrello) # deep copy (copio anche il contenuto)  chiedi meglio a chat

#Tuple
sede_principale = (45,8) # lat e long della sede di torino
sede_milano = (45, 9) # lat e long della sede di milano

print(60*"-")
print(f"Sede principale lat: {sede_principale[0]}, long: {sede_principale[1]}")
print(60*"-")

AliquoteIVA = (
    ("Standard", 0.22),
    ("Ridotta", 0.10),
    ("Alimentari", 0.04),
    ("Esente", 0.0)
    )

for descr, valore in AliquoteIVA:
    print(f"IVA {descr}: {valore*100}%")

def calcola_statistiche_carrello(carrello):
    """Restituisce prezzo totale, prezzo medio, massimo e minimo"""
    prezzi = [p.prezzo_unitario for p in carrello]
    return (sum(prezzi), sum(prezzi)/len(prezzi), max(prezzi), min(prezzi))

#tot, media, max, min = calcola_statistiche_carrello(carrello)

#tot, *altri_campi = calcola_statistiche_carrello(carrello)

#print(tot)

#SET
print(60*"-")
categorie = {"Gold", "Silver", "Bronze", "Gold"}
print (categorie)
print (len(categorie))
categorie2 = {"Platinum", "elite", "Gold"}
#categorie_all = categorie.union(categorie2)
categorie_all = categorie | categorie2  # unione
print (categorie_all)

categorie_comuni = categorie & categorie2 #solo elementi comuni
print (categorie_comuni)

categorie_esclusive = categorie - categorie2  # solo li elementi presenti in uno dei due
print (categorie_esclusive)

categorie_esclusive_symm = categorie ^ categorie2 # differenza simmetrica
print (categorie_esclusive_symm)

prodotti_ordine_A = {ProdottoRecord("Laptop", 1200),
                     ProdottoRecord("Mouse", 20),
                     ProdottoRecord("Tablet", 700)}

prodotti_ordine_B = {ProdottoRecord("Laptop2", 1200),
                     ProdottoRecord("Mouse2", 20),
                     ProdottoRecord("Tablet2", 700)}
print(60*"-")

#Metodi utili per i set
s = set()
s.add(ProdottoRecord("aaa", 20.0)) # aggiunge un elemento
s.update([ProdottoRecord("aaa", 20.0), ProdottoRecord("bbb", 20.0)]) # aggiungere più elementi

#togliere
#s.remove(elem) # rimuove un elemento. Se non esiste l'errore rileva un errore Raise KeyError
s.discard(elem) # rimuove un elemento senza arrabbiarsi se non esiste
s.pop() # rimuove e restituisce un elemento arbitrario
s.clear()

#Operazioni insiemistiche
s.union(s1) # s | s1, ovvero genera un set che unisce i set di partenza
s.intersection(s1) # s & s1, ovvero solo elementi comuni
s.difference (s1) # s-s1, ovvero elementi di s che non sono contenuti in s1
s.symmetric_difference(s1) # s^s1 ovvero elementi di s non contenuti in s1 e elementi di s1 non contenuti in s

s1.issubset(s) # se gli elementi di s1 sono contenuti in s
s1.issuperset(s)  # se gli elementi di s sono contenuti in s1
s1.isdisjoint(s)  # se gli elementi di s sono diversi da quelli di s1

#Dictionary





