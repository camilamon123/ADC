
import numpy as np
import scipy.fft
import matplotlib.pyplot as plt

# Crear un vector de ejemplo (puedes reemplazarlo con tus propios datos)
#vector = np.array([1, 0, 0, 0, 0,0,0,0], dtype=float)  #Ej 1.a
#vector = np.array([0, 0, 0, 1, 0,0,0,0], dtype=float)  #Ej 1.b

#vector = np.array([1, 0, 0, 0, 1,0,0,0,0,0], dtype=float)  #Ej 2.a
#vector = np.array([1, 1, 1, 1, 1,1,1,1,0,0], dtype=float)  #Ej 2.b
#vector = np.array([1, 1, 1, 0, 0,0,1,1,0,0], dtype=float)  #Ej 2.c

# Crear una señal de ejemplo (suma de dos senos)
N = 500
T = 1.0 / 600.0
x = np.linspace(0.0, N * T, N)
y = np.sin(60.0 * 2.0 * np.pi * x) + 0.5 * np.sin(90.0 * 2.0 * np.pi * x)

# Calcular la DFT de la señal
y_f = scipy.fft.fft(y)

# Graficar la magnitud del espectro
plt.figure(figsize=(8, 4))
plt.plot(np.abs(y_f))
plt.xlabel("Frecuencia")
plt.ylabel("Magnitud")
plt.title("Espectro de la señal")
plt.grid(True)
plt.show()










# Calcular la DFT utilizando la FFT
#dft_result = scipy.fft.fft(vector)

# Imprimir los coeficientes de la DFT
#print("Coeficientes de la DFT:", dft_result)