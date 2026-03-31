# import library
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt  # ← tambah ini

# menyiapkan himpunan fuzzy
makanan = ctrl.Antecedent(np.arange(0,11), 'makanan')
pelayanan = ctrl.Antecedent(np.arange(0,11), 'pelayanan')
nilai = ctrl.Consequent(np.arange(0,11),'nilai')

# rasa makanan
makanan['TidakEnak'] = fuzz.trimf(makanan.universe, [0,2,4])
makanan['Sedang'] = fuzz.trimf(makanan.universe, [3, 5, 7])
makanan['Enak'] = fuzz.trimf(makanan.universe, [6, 8, 10])

# nilai pelayanan
pelayanan['Ketus'] = fuzz.trimf(pelayanan.universe, [0, 2, 4])
pelayanan['Biasa'] = fuzz.trimf(pelayanan.universe, [3, 5, 7])
pelayanan['Ramah'] = fuzz.trimf(pelayanan.universe, [6, 8, 10])

# nilai restoran
nilai['Buruk'] = fuzz.trimf(nilai.universe, [0, 2, 4])
nilai['Cukup'] = fuzz.trimf(nilai.universe, [3, 5, 7])
nilai['Baik'] = fuzz.trimf(nilai.universe, [6, 8, 10])

aturan1 = ctrl.Rule(makanan['TidakEnak'] & pelayanan['Ketus'],
nilai['Buruk'])
aturan2 = ctrl.Rule(makanan['Sedang'] | pelayanan['Biasa'],
nilai['Cukup'])
aturan3 = ctrl.Rule(makanan['Enak'] | pelayanan['Ramah'], nilai['Baik'])

engine = ctrl.ControlSystem([aturan1, aturan2, aturan3])
system = ctrl.ControlSystemSimulation(engine)

# pengujian
system.input['makanan'] = 5.5
system.input['pelayanan'] = 7
system.compute()
print(system.output['nilai'])

# tampilkan grafik         ← tambahkan ini
makanan.view()
pelayanan.view()
nilai.view(sim=system)     # sim=system supaya area hasil ikut ter-shaded

plt.show()  # ← tambah ini, gantiin input("Tekan ENTER...")