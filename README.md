# 🦽 Sistem Fuzzy Logic untuk Analisis Stabilitas Kursi Roda

Sistem cerdas berbasis logika fuzzy untuk menganalisis dan mengevaluasi tingkat stabilitas kursi roda berdasarkan parameter dinamis seperti beban roda depan, percepatan lateral, percepatan aksial, dan sudut kemiringan. Made by **Angela**, **Filliana**, **Sihub**

## 📋 Deskripsi Proyek

Proyek ini mengimplementasikan sistem inferensi fuzzy untuk menentukan tingkat keamanan penggunaan kursi roda dalam berbagai kondisi. Sistem ini dapat membantu:

- **Pengguna kursi roda** untuk memahami kondisi keamanan saat berkendara
- **Terapis fisik** dalam memberikan rekomendasi penggunaan kursi roda
- **Peneliti** dalam bidang teknologi assistive dan rehabilitasi
- **Pengembang** perangkat medis untuk validasi desain

## ✨ Fitur Utama

### 🔍 Analisis Data
- Pembersihan dan normalisasi data sensor kursi roda
- Implementasi fuzzy inference system dengan aturan IF-THEN
- Klasifikasi stabilitas: **Aman**, **Hati-Hati**, **Berbahaya**

### 📊 Visualisasi Interaktif
- Dashboard web menggunakan Streamlit
- Grafik distribusi kategori stabilitas
- Scatter plot korelasi parameter vs stabilitas
- Visualisasi fungsi keanggotaan fuzzy

### ⚡ Input Real-time
- Interface untuk input manual parameter kursi roda
- Perhitungan stabilitas secara langsung
- Rekomendasi keamanan berdasarkan hasil analisis

## 🛠️ Instalasi

### Prasyarat
- Python 3.8 atau lebih baru
- pip (Python package manager)

### Langkah Instalasi

1. **Clone repository**
   ```bash
   git clone https://github.com/angelafy/fuzzy_disabilities.git
   cd fuzzy-wheelchair-stability
   ```

2. **Buat virtual environment (opsional tapi direkomendasikan)**
   ```bash
   python -m venv venv
   
   # Windows
   venv\\Scripts\\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Cara Penggunaan

### 1. Preprocessing Data
Jalankan script untuk membersihkan dan menormalisasi data:
```bash
python app.py
```

### 2. Analisis Fuzzy Logic
Eksekusi sistem inferensi fuzzy:
```bash
python fuzzy_stabilitas.py
```

### 3. Dashboard Visualisasi
Jalankan aplikasi web interaktif:
```bash
streamlit run visualization.py
```

Buka browser dan akses `http://localhost:8501` untuk melihat dashboard.

## 📁 Struktur File

```
fuzzy-wheelchair-stability/
│
├── app.py                    # Script preprocessing data
├── fuzzy_stabilitas.py       # Implementasi fuzzy logic
├── visualization.py          # Dashboard Streamlit
├── data.csv                  # Data mentah sensor kursi roda
├── normalized_data.csv       # Data yang sudah dinormalisasi
├── stabilitas_output.csv     # Hasil analisis fuzzy
├── requirements.txt          # Dependencies Python
└── README.md                # Dokumentasi proyek
```

## 🧮 Metodologi Fuzzy Logic

### Variabel Input
- **Beban Roda Depan (%)**: Distribusi beban pada roda depan
- **Percepatan Lateral (m/s²)**: Percepatan ke samping
- **Percepatan Aksial (m/s²)**: Percepatan maju/mundur
- **Sudut Kemiringan (rad)**: Sudut kemiringan kursi roda

### Fungsi Keanggotaan
- **Triangular Membership Function** untuk setiap variabel
- Kategori: Rendah, Sedang, Tinggi (untuk input)
- Output: Berbahaya (0-40), Hati-Hati (30-70), Aman (60-100)

### Aturan Fuzzy
1. **IF** beban rendah **OR** kemiringan tinggi **OR** lateral tinggi **THEN** berbahaya
2. **IF** beban sedang **OR** aksial tinggi **THEN** hati-hati  
3. **IF** beban tinggi **AND** kemiringan rendah **AND** aksial rendah **THEN** aman

## 📊 Contoh Output

```
Input:
- Beban Roda Depan: 0.75
- Percepatan Lateral: 0.30
- Percepatan Aksial: 0.25
- Sudut Kemiringan: 0.20

Output: 
- Nilai Stabilitas: 72.5
- Kategori: ✅ Aman
```

## 🤝 Kontribusi

Kami menyambut kontribusi dari komunitas! Untuk berkontribusi:

1. Fork repository ini
2. Buat branch fitur baru (`git checkout -b fitur-baru`)
3. Commit perubahan (`git commit -am 'Menambah fitur baru'`)
4. Push ke branch (`git push origin fitur-baru`)
5. Buat Pull Request

### Panduan Kontribusi
- Pastikan kode mengikuti PEP 8 style guide
- Tambahkan unit test untuk fitur baru
- Update dokumentasi jika diperlukan
- Gunakan commit message yang deskriptif

## 📝 Lisensi

Proyek ini dilisensikan di bawah [MIT License](LICENSE) - lihat file LICENSE untuk detail lengkap.

## 👥 Tim Pengembang

- **Nama Developer** - *Initial work* - [GitHub](https://github.com/username)

## 🙏 Acknowledgments

- Terima kasih kepada komunitas scikit-fuzzy untuk library yang luar biasa
- Inspirasi dari penelitian di bidang teknologi assistive
- Dataset kursi roda dari [sumber dataset]

## 📞 Kontak & Support

- **Issues**: [GitHub Issues](https://github.com/angelafy/fuzzy_disabilities/issues)
- **Discussions**: [GitHub Discussions](https://github.com/angelafy/fuzzy_disabilities/discussions)

---

⭐ **Jika proyek ini bermanfaat, jangan lupa berikan star di GitHub!**

*Dibuat dengan ❤️ untuk meningkatkan kualitas hidup pengguna kursi roda*
