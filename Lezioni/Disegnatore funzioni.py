import numpy as np
import matplotlib.pyplot as plt


# Creiamo set funz
print("=== IL MIO PLOTTER MATEMATICO ===")
print("Scegli quale funzione vuoi graficare:")
print("1: Parabola (x^2)")
print("2: Cubo (x^3)")
print("3: Logaritmo naturale (ln(x))")
print("4: Iperbole (1/x)")
print("5: Seno (sin(x))")
print("5: Coseno (cos(x))")

# input n funz
scelta = input("\nInserisci il numero della funzione (1-6): ")

# Creo l'asse X 
x = np.linspace(-10, 10, 1000)

# impostazioni funz
if scelta == '1':
    nome_funzione = "a*x^2 + b*x + c"
    print(nome_funzione)
    a=float(input('coefficente a ='))
    b=float(input('coefficente b ='))
    c=float(input('coefficente c ='))
    y_Funz = a*(x**2) + b*(x) + c

elif scelta == '2':
    nome_funzione = "a * x^3 + b * x^2 + c * x + d"
    print(nome_funzione)
    a=float(input('coefficente a ='))
    b=float(input('coefficente b ='))
    c=float(input('coefficente c ='))
    d=float(input('coefficente d ='))
    y_Funz = a * x**3 + b * x**2 + c * x + d

elif scelta == '3':
    nome_funzione = "y = a*ln(b*x + c)"
    print(nome_funzione)
    a=float(input('coefficente moltiplicativo a ='))
    b=float(input('coefficente b ='))
    c=float(input('traslazione su x, coeff c ='))
    y_Funz = a*np.log(b*x + c)
    
elif scelta == '4':
    nome_funzione = "y = c + a/(x-b)"
    print(nome_funzione)
    a=float(input('costante di proporzionalità inversa a ='))
    b=float(input('traslazione su asse x,coef b ='))
    c=float(input('traslazione su y, coeff c ='))
    y_Funz = c + a / (x+b)
    
elif scelta == '5':
    nome_funzione = "y = a*sin(b*x + c)"
    print(nome_funzione)
    a=float(input('Ampiezza a ='))
    b=float(input('Pulsazione,coef b ='))
    c=float(input('Fase iniziale (per coseno c=), coeff c ='))
    y_Funz = a*np.sin(b*x + c)

elif scelta == '6':
    nome_funzione = "y = a*cos(b*x + c)"
    print(nome_funzione)
    a=float(input('Ampiezza a ='))
    b=float(input('Pulsazione,coef b ='))
    c=float(input('Fase iniziale (per coseno c=), coeff c ='))
    y_Funz = a*np.cos(b*x + c)
    
else:
    print("Errore")


figura, grafico = plt.subplots(num= 'By Gianmario Pelanda', figsize=(12,12))


# Centratura
y_min = np.min(y_Funz)
y_max = np.max(y_Funz)

if y_max > 100 or y_min < -100:
    grafico.set_ylim(-20, 20)
else:
    
    grafico.set_ylim(y_min - abs(y_min) - 1, y_max + abs(y_max) + 1)




plt.plot(x, y_Funz, label=f'Funzione {nome_funzione}', color='blue')



plt.legend()
plt.title("Funzioni Matematiche")
plt.grid(True, linestyle='--')


plt.show()