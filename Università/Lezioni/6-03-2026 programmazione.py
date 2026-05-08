#creazione array

#lista si usano parentesi quadri []
#set si usano parentesi graffe {}
#tupla si usano parentesi tonde ()

#creazione di una lista
lista = []
#aggiunta di elementi alla lista
lista.append('ciao')
lista.append('mamma')
lista.append(10)

print(lista)

#prendere un elemento dalla lista
x = lista[0]
print(x)

#cambiare un elemento della lista
lista[0] = 'hello'
print(lista)



#tupla è una struttura dati simile alla lista ma è immutabile, non si possono modificare gli elementi dopo la creazione
tupla = (1, 2, 3)

print(tupla)



#dizionario è una struttura dati che associa chiavi (nome stesso che viene usato come identificatore) a valori, si usano parentesi graffe {}
dizionario = {}

#aggiunta di elementi al dizionario
dizionario['nome'] = 'Mario'
dizionario['cognome'] = 'Rossi'

print(dizionario)

#lista si usa solitamente per i cicli
#dizionario è più efficiente per cercare un elemento, è più veloce rispetto alla lista e per descrivere i dati in modo più strutturato, è più facile da leggere e da capire rispetto alla lista.
particella = {'x': 0, 'y': 0, 'v': 12}

#posso richiamare la velocità della particella con particella['v']
print(particella['v'])