# import library
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# menyiapkan himpunan fuzzy 
biaya = ctrl.Antecedent(np.arange(0, 1001, 1), 'biaya')
permintaan = ctrl.Antecedent(np.arange(0, 61, 1), 'permintaan')
produksi = ctrl.Consequent(np.arange(0, 101, 1), 'produksi')

# biaya produksi
biaya['Rendah'] = fuzz.zmf(biaya.universe, 0, 500)
biaya['Standar'] = fuzz.pimf(biaya.universe, 0, 500, 500, 1000)
biaya['Tinggi'] = fuzz.smf(biaya.universe, 500, 1000)

# permintaan
permintaan['Turun'] = fuzz.trapmf(permintaan.universe, [0, 0, 10, 30])
permintaan['Biasa'] = fuzz.trimf(permintaan.universe, [10, 30, 50])
permintaan['Naik'] = fuzz.trapmf(permintaan.universe, [30, 50, 60, 60]) 

# produksi
produksi['Sedikit'] = fuzz.trimf(produksi.universe, [0, 0, 50])
produksi['Banyak'] = fuzz.trimf(produksi.universe, [50, 100, 100])

# visualisasi
biaya.view()
permintaan.view()
produksi.view()

plt.show()