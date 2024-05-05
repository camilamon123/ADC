import numpy as np
import matplotlib.pyplot as plt
from math import *

# Valores dados
u_t = 0.01
UI_s = 0.0499
t_r_UI = 4
V_H_min = 0.028
V_H = 0.0350
V_H_max = 0.051

#mis omegas reals
alpha = 300
omega_d= 675

#Calculo de mis parametros
#Para subamortiguada y criticamente amortiguada:
A_1 = - V_H
A_2 = -(alpha*V_H)/omega_d

                                                                #OMEGAS Y ALPHAS DE PRUEBA

#s_1 = -2
#s_2 = -1
#A_1 = 0.01
#A_2 = -A_1 - V_H
                                                                
V_10porciento = 0.0035
V_90porciento = 0.0315

# Creación de un arreglo de tiempo
plt.figure(figsize=(10, 6))
t = np.linspace(0, 0.09,1000) #tiempo de muestreo para la grafica de la subamor
#t = np.linspace(0, 10,1000)


# Cálculo de la señal
#y = A_1 * np.exp(s_1 * t) + A_2 * np.exp(s_2 * t) + V_H #sobreamortiguada
#y = (A_1 + A_2 * t)* np.exp(-alpha * t) + V_H #criticamente amortiguada

y = np.exp(-alpha * t)*(A_1* np.cos(omega_d * t) + A_2 * np.sin(omega_d *t)) +  V_H #subamortiguada


plt.axhline(y= V_H_max, color ='black', linestyle= '--') #V_H MAX
plt.axhline(y= V_H, color ='red', linestyle= '--' ) #VH
plt.axhline(y= V_H_min, color ='black', linestyle= '--') #V_H MIN
plt.axhline(y= V_10porciento,xmin = 0, xmax= 0.013, color ='black') #10 porciento de V_H

plt.axhline(y= V_90porciento,xmin = 0 , xmax=0.0455, color ='black') #90 porciento de V_H
plt.axhline(y= 0,xmin = 0.000646 , xmax=0.00262 , color ='black') #tr

plt.vlines(x = UI_s,ymin= 0,ymax= V_H_max, color = 'green',) #UI
plt.vlines(x = 5/alpha ,ymin= 0,ymax= V_H, color = 'black',linestyle = '--') #5 tau
plt.vlines(x = 0.00262,ymin= 0,ymax= V_90porciento, color = 'black',) #%90
plt.vlines(x = 0.000646,ymin= 0,ymax= V_10porciento, color = 'black',) #%10



# Ajustar límites para "zoom"
plt.xlim(0, 0.06)  # Limita el eje X entre 0 y 1
plt.ylim(0, V_H*1.5 )  # Limita el eje Y entre 0 y 0.01


plt.plot(t, y, label='V(t)')
punto_90 = plt.plot(0.0026,V_90porciento  , 'bo', color = 'red')
punto_10 = plt.plot(0.000646,V_10porciento  , 'bo', color = 'red')
plt.axhline(y= 0,xmin = 0.015 , xmax=0.04 ,linewidth = 7, color ='green') #tr
texto1 = plt.text(0.0010, 0.0015, r'$t_r$', fontsize=10,bbox = {'facecolor': 'oldlace', 'alpha': 0.5,'boxstyle': "square,pad=0.2"} ) #marcador del t_r
texto1 = plt.text(0.0005, V_H , r'$V_H$', fontsize=10, bbox = {'facecolor': 'oldlace', 'alpha': 0.5,'boxstyle': "square,pad=0.2"}) #marcador de V_H
texto1 = plt.text(0.03, V_H_max -0.002, r'$V_{H_{max}}$', fontsize= 15,bbox = {'facecolor': 'oldlace', 'alpha': 0.5,'boxstyle': "square,pad=0.4"}) #marcador de V_H_max
texto1 = plt.text(0.03, V_H_min +0.002, r'$V_{H_{min}}$', fontsize= 15,bbox = {'facecolor': 'oldlace', 'alpha': 0.5,'boxstyle': "square,pad=0.4"}) #marcador de V_H_min
texto1 = plt.text(UI_s, 0, r'$UI$', fontsize= 10,bbox = {'facecolor': 'oldlace', 'alpha': 0.5,'boxstyle': "square,pad=0.4"}) #marcador para UI
plt.annotate('($5\\tau = 0.016 $ , $V_H\,=\,0.035$ )', #marcador del punto tau y vh
            xy = (5/alpha, V_H),
             xytext = (0.02, 0.04),
             arrowprops = dict(facecolor = 'black', width = 0.2, headwidth = 8),
             horizontalalignment = 'center')
# Banda horizontal de y=0 a y=2 de color azul (b)
# y 30% de transparencia (alpha=0.3)
plt.axhspan(- 0.02*V_H + V_H , 0.02*V_H + V_H , alpha=0.3, color='blue')
plt.axhspan(V_H_min , V_H_max , alpha=0.3, color='pink') #resalto un intervalo 



plt.xlabel('Tiempo [s]')
plt.ylabel('V(t)')
plt.title('Respuesta subamortiguada')
plt.grid(True)
plt.legend()
plt.show()



