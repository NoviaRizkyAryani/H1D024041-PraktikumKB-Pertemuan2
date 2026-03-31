# import library
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# menyiapkan variabel fuzzy 
suhu       = ctrl.Antecedent(np.arange(0, 41, 1),  'suhu')
kelembapan = ctrl.Antecedent(np.arange(0, 101, 1), 'kelembapan')
kecepatan  = ctrl.Consequent(np.arange(0, 101, 1), 'kecepatan')

# suhu
suhu['Dingin'] = fuzz.zmf(suhu.universe, 10, 20)
suhu['Hangat'] = fuzz.trapmf(suhu.universe, [15, 20, 25, 30])
suhu['Panas']  = fuzz.smf(suhu.universe, 25, 35)

# kelembapan
kelembapan['Rendah'] = fuzz.trimf(kelembapan.universe, [0, 0, 40])
kelembapan['Sedang'] = fuzz.trimf(kelembapan.universe, [30, 50, 70])
kelembapan['Tinggi'] = fuzz.trapmf(kelembapan.universe, [60, 80, 100, 100])

# kecepatan
kecepatan['Lambat'] = fuzz.zmf(kecepatan.universe, 20, 50)
kecepatan['Sedang'] = fuzz.trimf(kecepatan.universe, [40, 60, 80])
kecepatan['Cepat']  = fuzz.smf(kecepatan.universe, 70, 100)

# rule base
aturan1 = ctrl.Rule(suhu['Dingin'] & kelembapan['Rendah'], kecepatan['Lambat'])
aturan2 = ctrl.Rule(suhu['Hangat'] | kelembapan['Sedang'], kecepatan['Sedang'])
aturan3 = ctrl.Rule(suhu['Panas'], kecepatan['Cepat'])
aturan4 = ctrl.Rule(kelembapan['Tinggi'], kecepatan['Cepat'])

# inference engine dan sistem fuzzy
engine = ctrl.ControlSystem([aturan1, aturan2, aturan3, aturan4])
system = ctrl.ControlSystemSimulation(engine)

# memberikan input atau pengujian
system.input['suhu'] = 30
system.input['kelembapan'] = 70

# perhitungan fuzzy
system.compute()

# menampilkan output dan visualisasi (tamplilkan grafik)
print(f"Hasil Kecepatan: {system.output['kecepatan']}")
suhu.view()
kelembapan.view()
kecepatan.view()
kecepatan.view(sim=system)
plt.show()