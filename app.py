import pandas as pd

# File input dan output
INPUT_PATH = 'data.csv'
OUTPUT_PATH = 'normalized_data.csv'

# Kolom yang diperlukan
needed_cols = ['beban_roda_depan(%)', 'percepatan_lateral(m/s)', 'percepatan_aksial(m/s)', 'sudut_kemiringan_bt(rad)']

def clean_column(col):
    return col.str.replace('.', '', regex=False).str.replace(',', '.', regex=False).astype(float)

def normalize_column(col):
    return (col - col.min()) / (col.max() - col.min())

def clean_and_normalize():
    data = pd.read_csv(INPUT_PATH, sep=';', encoding='latin-1')

    # Ambil hanya kolom yang dibutuhkan
    data = data[needed_cols]

    # Drop missing value
    data = data.dropna()

    # Convert ke float jika masih object
    for col in needed_cols:
        if data[col].dtype == object:
            data[col] = clean_column(data[col])

    # Normalisasi semua kolom
    normalized = data.copy()
    for col in needed_cols:
        normalized[col] = normalize_column(data[col])

    normalized.to_csv(OUTPUT_PATH, index=False)
    print(f"Data berhasil dibersihkan & dinormalisasi ke: {OUTPUT_PATH}")

if __name__ == "__main__":
    clean_and_normalize()

