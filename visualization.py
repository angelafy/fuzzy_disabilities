import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load hasil fuzzy inference
df = pd.read_csv('D:/Tubes AI/stabilitas_output.csv')

st.title("Visualisasi Fuzzy Logic untuk Stabilitas Kursi Roda")

# Sidebar filter kategori
kategori = st.sidebar.multiselect(
    "Pilih Kategori Stabilitas",
    options=df['label_stabilitas'].unique(),
    default=df['label_stabilitas'].unique()
)

filtered_df = df[df['label_stabilitas'].isin(kategori)]

# Pie chart distribusi kategori
st.subheader("Distribusi Kategori Stabilitas")
fig1, ax1 = plt.subplots()
sizes = filtered_df['label_stabilitas'].value_counts()
ax1.pie(sizes, labels=sizes.index, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')
st.pyplot(fig1)

# Scatter plot sudut kemiringan vs stabilitas
st.subheader("Sudut Kemiringan vs Nilai Stabilitas")
fig2, ax2 = plt.subplots()
color_map = {'Aman': 'green', 'Hati-Hati': 'yellow', 'Berbahaya': 'red'}
for label in filtered_df['label_stabilitas'].unique():
    subset = filtered_df[filtered_df['label_stabilitas'] == label]
    ax2.scatter(subset['sudut_kemiringan_bt(rad)'], subset['stabilitas'], label=label,
                alpha=0.7, color=color_map[label])
ax2.set_xlabel('Sudut Kemiringan (rad)')
ax2.set_ylabel('Nilai Stabilitas')
ax2.legend()
st.pyplot(fig2)

# Contoh fungsi keanggotaan segitiga (simplified)
import numpy as np

def triangular_mf(x, a, b, c):
    return np.maximum(np.minimum((x - a) / (b - a), (c - x) / (c - b)), 0)

x = np.linspace(0, 1, 200)
params = {
    "Rendah": (0, 0, 0.4),
    "Sedang": (0.3, 0.5, 0.7),
    "Tinggi": (0.6, 1, 1)
}

st.subheader("Contoh Fungsi Keanggotaan Fuzzy (Beban Roda Depan)")
fig3, ax3 = plt.subplots()
for label, (a, b, c) in params.items():
    y = triangular_mf(x, a, b, c)
    ax3.plot(x, y, label=label)
ax3.set_xlabel("Nilai Beban Roda Depan (normalisasi)")
ax3.set_ylabel("Derajat Keanggotaan")
ax3.legend()
st.pyplot(fig3)

st.subheader("🔍 Input Data Numerik Kursi Roda (IF-THEN)")

with st.form("form_input_manual"):
    beban_input = st.slider("Beban Roda Depan (0–1)", 0.0, 1.0, 0.5, 0.01)
    lateral_input = st.slider("Percepatan Lateral (0–1)", 0.0, 1.0, 0.5, 0.01)
    aksial_input = st.slider("Percepatan Aksial (0–1)", 0.0, 1.0, 0.5, 0.01)
    kemiringan_input = st.slider("Sudut Kemiringan (0–1)", 0.0, 1.0, 0.5, 0.01)
    submitted = st.form_submit_button("Hitung Stabilitas")

if submitted:
    import skfuzzy as fuzz
    from skfuzzy import control as ctrl

    # Definisi variabel fuzzy
    beban = ctrl.Antecedent(np.arange(0, 1.01, 0.01), 'beban')
    lateral = ctrl.Antecedent(np.arange(0, 1.01, 0.01), 'lateral')
    aksial = ctrl.Antecedent(np.arange(0, 1.01, 0.01), 'aksial')
    kemiringan = ctrl.Antecedent(np.arange(0, 1.01, 0.01), 'kemiringan')
    stabilitas = ctrl.Consequent(np.arange(0, 101, 1), 'stabilitas')

    # Membership functions
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

    # Fuzzy Rules
    rule1 = ctrl.Rule(beban['rendah'] | kemiringan['tinggi'] | lateral['tinggi'], stabilitas['berbahaya'])
    rule2 = ctrl.Rule(beban['sedang'] | aksial['tinggi'], stabilitas['hati2'])
    rule3 = ctrl.Rule(beban['tinggi'] & kemiringan['rendah'] & aksial['rendah'], stabilitas['aman'])

    stabilitas_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
    sim = ctrl.ControlSystemSimulation(stabilitas_ctrl)

    sim.input['beban'] = beban_input
    sim.input['lateral'] = lateral_input
    sim.input['aksial'] = aksial_input
    sim.input['kemiringan'] = kemiringan_input
    sim.compute()

    hasil = sim.output['stabilitas']
    if hasil < 40:
        label = '❗ Berbahaya'
    elif hasil < 70:
        label = '⚠️ Hati-Hati'
    else:
        label = '✅ Aman'

    st.success(f"Hasil Fuzzy: {hasil:.2f} → {label}")