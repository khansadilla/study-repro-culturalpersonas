import pandas as pd

# Load data asli
df = pd.read_csv('../datasets/cp/answers/all_japan_mcs_ready.csv', engine='python')

# Ambil 5 baris pertama untuk setiap trait (Total 25 baris)
medium_df = df.groupby('trait').head(5)

# Simpan
medium_df.to_csv('../datasets/cp/answers/japan_medium.csv', index=False)
print("File 25 soal siap! Cuma butuh biaya sekitar 0.05 dollar.")