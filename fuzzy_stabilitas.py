import numpy as np
import pandas as pd
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Load data yang sudah dinormalisasi
df = pd.read_csv('D:/Tubes AI/normalized_data.csv')

# Definisi variabel fuzzy
beban = ctrl.Antecedent(np.arange(0, 1.01, 0.01), 'beban')
lateral = ctrl.Antecedent(np.arange(0, 1.01, 0.01), 'lateral')
aksial = ctrl.Antecedent(np.arange(0, 1.01, 0.01), 'aksial')
kemiringan = ctrl.Antecedent(np.arange(0, 1.01, 0.01), 'kemiringan')
stabilitas = ctrl.Consequent(np.arange(0, 101, 1), 'stabilitas')

# Membership Function (Triangular)
beban['rendah'] = fuzz.trimf(beban.universe, [0, 0, 0.4])
beban['sedang'] = fuzz.trimf(beban.universe, [0.3, 0.5, 0.7])
beban['tinggi'] = fuzz.trimf(beban.universe, [0.6, 1, 1])

lateral['rendah'] = fuzz.trimf(lateral.universe, [0, 0, 0.5])
lateral['tinggi'] = fuzz.trimf(lateral.universe, [0.4, 1, 1])

aksial['rendah'] = fuzz.trimf(aksial.universe, [0, 0, 0.5])
aksial['tinggi'] = fuzz.trimf(aksial.universe, [0.4, 1, 1])

kemiringan['rendah'] = fuzz.trimf(kemiringan.universe, [0, 0, 0.5])
kemiringan['tinggi'] = fuzz.trimf(kemiringan.universe, [0.4, 1, 1])

stabilitas['berbahaya'] = fuzz.trimf(stabilitas.universe, [0, 0, 40])
stabilitas['hati2'] = fuzz.trimf(stabilitas.universe, [30, 50, 70])
stabilitas['aman'] = fuzz.trimf(stabilitas.universe, [60, 100, 100])

# Rule Fuzzy
rule1 = ctrl.Rule(beban['rendah'] | kemiringan['tinggi'] | lateral['tinggi'], stabilitas['berbahaya'])
rule2 = ctrl.Rule(beban['sedang'] | aksial['tinggi'], stabilitas['hati2'])
rule3 = ctrl.Rule(beban['tinggi'] & kemiringan['rendah'] & aksial['rendah'], stabilitas['aman'])

# Bangun sistem kontrol
stabilitas_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
simulator = ctrl.ControlSystemSimulation(stabilitas_ctrl)

# Jalankan fuzzy untuk setiap baris
output = []
for i, row in df.iterrows():
    simulator.input['beban'] = row['beban_roda_depan(%)']
    simulator.input['lateral'] = row['percepatan_lateral(m/s)']
    simulator.input['aksial'] = row['percepatan_aksial(m/s)']
    simulator.input['kemiringan'] = row['sudut_kemiringan_bt(rad)']
    simulator.compute()
    nilai = simulator.output['stabilitas']
    if nilai < 40:
        label = 'Berbahaya'
    elif nilai < 70:
        label = 'Hati-Hati'
    else:
        label = 'Aman'
    output.append({'stabilitas': nilai, 'label_stabilitas': label})