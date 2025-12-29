import matplotlib.pyplot as plt
import numpy as np

# 1. Data hasil eksperimen Dilla (Rata-rata KS Stat dari hasil 25 soal tadi)
# Kita hitung rata-rata dari [0.60, 0.54, 0.79, 0.35] = 0.57
dilla_ks_average = 0.57

# 2. Data Baseline Paper untuk Japan (Estimasi visual dari Figure 2)
# Urutan: IPIP-120, IPIP-300, BFI, TRAIT, Big5Chat, CulturalPersonas (Paper)
baselines = {
    'IPIP-120': 0.32,
    'IPIP-300': 0.35,
    'BFI': 0.28,
    'TRAIT': 0.38,
    'Big5Chat': 0.37,
    'CulturalPersonas (Paper)': 0.21
}

# 3. Setup Plot
fig, ax = plt.subplots(figsize=(6, 5))

# Nama-nama kategori di sumbu X
categories = ['Psychometric Tests', 'LLM Benchmarks', 'CulturalPersonas']

# Warna yang mirip dengan di paper
colors = ['#4e91bc', '#67ab5d', '#d6534d', '#8664a3', '#e68a30', '#18acba']

# Plotting batang satu per satu sesuai kelompok
# Kelompok Psychometric (IPIP-120, IPIP-300, BFI)
ax.bar(0.2, baselines['IPIP-120'], width=0.1, color=colors[0], label='IPIP-120')
ax.bar(0.3, baselines['IPIP-300'], width=0.1, color=colors[1], label='IPIP-300')
ax.bar(0.1, baselines['BFI'], width=0.1, color=colors[2], label='BFI')

# Kelompok LLM Benchmarks (TRAIT, Big5Chat)
ax.bar(0.6, baselines['TRAIT'], width=0.1, color=colors[3], label='TRAIT', hatch='//')
ax.bar(0.7, baselines['Big5Chat'], width=0.1, color=colors[4], label='Big5Chat', hatch='\\')

# Kelompok Cultural Personas (Versi Dilla)
ax.bar(1.1, dilla_ks_average, width=0.15, color=colors[5], label='CulturalPersonas (Dilla)', hatch='--')

# 4. Dekorasi agar mirip aslinya
ax.set_title('Japan', fontsize=14, fontweight='bold')
ax.set_ylabel('KS Statistic', fontsize=12)
ax.set_ylim(0, 0.8) # Sesuaikan agar batang Dilla terlihat
ax.set_xlim(-0.1, 1.4)

# Menghilangkan garis frame atas dan kanan
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Custom X-axis labels
ax.set_xticks([0.2, 0.65, 1.1])
ax.set_xticklabels(['Psychometric', 'LLM Benchmarks', 'Dilla Repro'], fontsize=10)

# Grid horizontal tipis
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Tambahkan label keterangan di bawah (Legend)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=9)

plt.tight_layout()
plt.savefig('repro_figure2_style.png', dpi=300)
plt.show()