# Circle_Square_2.py
# Läser in cirkelns radie, beräknar kvadratens sida och
# båda figurernas areor samt jämför dem med varandra

from math import pi             # Importerar modulen math
r = float(input('\n\tMata in cirkelns radie:\t'))
a = pi * r / 2                  # Kvadratens sida

A_circle = pi * r**2            # Cirkelns radie
A_square = a**2                 # Kvadratens area

if A_circle > A_square :
   print('\n\tCirkelns area är större än kvadratens.\n')
else :
   print('\n\tKvadratens area är större än cirkelns.\n')



