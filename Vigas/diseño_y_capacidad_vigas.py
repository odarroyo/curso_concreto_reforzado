#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 16:00:01 2026

@author: mac
"""

# Ejercicio # 1: Cálculo de capacidad de una viga existente

# Definición de la viga: 0.35 x 0.45 m con 4 # 6 en la parte inferior. Recubrimiento de 5 cm
import numpy as np
b = 0.35
h = 0.45
As = 4*2.86/10000 # area de las cuatro barras
r = 0.05 # recubrimiento al centro de la barra
fc = 28000 # esfuerzo del concreto en kN/m2
fy = 420000 # fluencia del acero en kN/m2
d = h - r

M = As*fy*(d - (As*fy)/(1.7*fc*b)) # capacidad nominal. 
fi = 0.9
Md = fi*M # capacidad de diseño de la viga

# Verificamos que funcione como viga
beta = 0.85 # según Whitney
ec = 0.003 # deformación del concreto
c = As*fy/(0.85*fc*b*beta)

et = ec*(d-c)/c # aplicando Euler Bernoulli (hacer gráfico)
# como et > 0.005 entonces cumple que funciona como viga


# Ejercicio # 2: Cálculo de cuantia requerida a 

M_actuante = 125
m = fy/(0.85*fc)
K = M_actuante/(b*d**2)
rho = 1/m * (1-np.sqrt(1-2*m*K/(fi*fy)))
area_acero = rho*b*d*10000 # area en cm2

# Verificamos que funcione como viga
beta = 0.85 # según Whitney
ec = 0.003 # deformación del concreto
c2 = area_acero/10000*fy/(0.85*fc*b*beta)

et2 = ec*(d-c2)/c2 # aplicando Euler Bernoulli (hacer gráfico)
# como et > 0.005 entonces cumple que funciona como viga

