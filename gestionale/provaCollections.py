import copy
from collections import Counter

from gestionale.core.clienti import ClienteRecord
from gestionale.core.prodotti import ProdottoRecord
from gestionale.vendite.ordini import Ordine

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
# s.discard(elem) # rimuove un elemento senza arrabbiarsi se non esiste
s.pop() # rimuove e restituisce un elemento arbitrario
s.clear()

#Operazioni insiemistiche
#s.union(s1) # s | s1, ovvero genera un set che unisce i set di partenza
#s.intersection(s1) # s & s1, ovvero solo elementi comuni
#s.difference (s1) # s-s1, ovvero elementi di s che non sono contenuti in s1
#s.symmetric_difference(s1) # s^s1 ovvero elementi di s non contenuti in s1 e elementi di s1 non contenuti in s

#s1.issubset(s) # se gli elementi di s1 sono contenuti in s
#s1.issuperset(s)  # se gli elementi di s sono contenuti in s1
#s1.isdisjoint(s)  # se gli elementi di s sono diversi da quelli di s1

#Dictionary
catalogo = {
    "LAP001" : ProdottoRecord("Laptop", 1200),
    "LAP002" : ProdottoRecord("Laptop PRO", 2300),
    "MAU001" : ProdottoRecord("Mouse", 20.0),
    "AUR001" : ProdottoRecord("Auricolari", 250.0),
}

cod = "LAP002"
prod = catalogo[cod]

print (f"Il prodotto con codice {cod} è {prod}")

#print (f"Cerco un altro oggetto {catalogo["NonEsiste"]}")

prod1 = catalogo.get("NonEsiste")

if prod1 is None:
    print("Prodotto non trovato")

prod2 = catalogo.get("NonEsiste2", ProdottoRecord("Sconosciuto", 0))

print (prod2)

#Ciclare su un dizionario
keys = list(catalogo.keys())
values = list(catalogo.values())

for k in keys:
    print (k)

for v in values:
    print (v)

for key, val in catalogo.items():
    print (f"Cod {key} è associata a: {val} ")

#rimuovere dal dizionario
rimosso = catalogo.pop("LAP002")
print  (rimosso)

#dict comprehesion
prezzi = {codice: prod.prezzo_unitario for codice, prod in catalogo.items()}

#DA RICORDARE PER DICT
#d[key] = v # scrivo sul dizionario
#v = d[key] # leggere -- restituisce KeyError se non esiste
#v = d.get(key, default) # legge senza rischiare KeyError. Se non esiste rende il default
#d.pop() # restituisce un valore e lo cancella dal dizionario
#d.cleare # elimina tutto
#d.keys() # mi restituisce tutte le chiavi definite nel dizionario
#d.values() # mi restituisce tutti i valori salvati nel dizionario
#d.items() # mi restituisce le coppie chiave-valore
#key in d # condizione che verifica se key è presente nel dizionario

"""Esercizio live
Per ciascuno dei seguenti casi, decidere quale struttura usare: """

"""1) Memorizzare una lista di ordini che dovranno poi essere processati in ordine di arrivo"""
#Collection? Lista
ordini_da_processare = []
o1 = Ordine([], ClienteRecord("Mario Rossi", "mario@polito.it", "Gold"))
o2 = Ordine([], ClienteRecord("Mario Bianchi", "bianchi@polito.it", "Silver"))
o3 = Ordine([], ClienteRecord("Fulvio Rossi", "fulvio@polito.it", "Bronze"))
o4 = Ordine([], ClienteRecord("Carlo Masone", "carlo@polito.it", "Gold"))

ordini_da_processare.append((o1, 0))
ordini_da_processare.append((o2, 10))
ordini_da_processare.append((o3, 3))
ordini_da_processare.append((o4, 45))

"""2) Memorizzare i codici fiscali dei clienti (univoco per ogni cliente)"""
#Collection? Univoco --> la lista non va bene
codici_fiscali = {"adjhl234", "ajfhlh556", "jsdfgl6849", "ajfhlh556"}
print (codici_fiscali)

"""3) Creare un database dei prodotti che posso cercare con un codice univoco"""
#Collection?
listino_prodotti = {"LAP001" : ProdottoRecord("Laptop", 1200.0),
                    "KEY001" : ProdottoRecord("KEYBOARD", 20.0),}

"""4) Memorizzare le coordinate GPS della nuova sede di Roma"""
#Collection?
magazzino_roma = (45, 6)

"""5) Tenere traccia delle categorie di clienti che hanno fatto un ordine in un certo range temporale"""
#Collection?
categorie_periodo = set()
categorie_periodo.add("Gold")
categorie_periodo.add("Bronze")

print(60*"-")

#COUNTER
lista_clienti = [
    ClienteRecord("Mario Rossi", "mario@polito.it", "Gold"),
    ClienteRecord("Mario Bianchi", "bianchi@polito.it", "Silver"),
    ClienteRecord("Fulvio Rossi", "fulvio@polito.it", "Bronze"),
    ClienteRecord("Carlo Masone", "carlo@polito.it", "Gold"),
    ClienteRecord("Simone Gambina", "simo@polito.it", "Gold"),
    ClienteRecord("James Harden", "thebeard13@polito.it", "Silver"),
    ClienteRecord("Alberto Angela", "pieroson@polito.it", "Bronze"),
    ClienteRecord("Maduro", "madhard@polito.it", "Gold"),
    ClienteRecord("AHAHA", "ahaha@polito.it", "Silver")
]

categorie = [c.categoria for c in lista_clienti]
categorie_counter = Counter(categorie)
print("Distribuzione categorie clienti:")
print(categorie_counter)

print ("Le 2 categoria più frequenti: ")
print(categorie_counter.most_common(2))

print("Totale clienti:")
print(categorie_counter.total())
print(60*"-")

vendite_gennaio = Counter(
    {"Laptop" : 13, "Tablet" : 15}
)

vendite_febbraio = Counter(
    {"Laptop" : 3, "Stampante" : 1}
)

#Aggregare informazione
vendite_bimestre = vendite_gennaio + vendite_febbraio
print(f"Vendite gennaio: {vendite_gennaio}")
print(f"Vendite febbraio: {vendite_febbraio}")
print(f"Vendite bimestre: {vendite_bimestre}")

#Fare la differenza
print(f"Differenza di vendite: {vendite_gennaio - vendite_febbraio}")

#Modificare i valori in the fly
vendite_gennaio["Laptop"] +=4
print(f"Vendite gennaio: {vendite_gennaio}")
print(60*"-")

#Metodi da ricordare
#c.most_common(n) #restituisce gli n elementi più frequenti
#c.total()  # somma dei conteggi

#Defaultdicts
