import pandas as pd
import numpy as np
from scipy.stats import ks_2samp

def calculate_probs_safe(row_values):
    clean_values = np.array([float(x) if x != '-inf' else -50.0 for x in row_values])
    # Softmax conversion
    exp_v = np.exp(clean_values - np.max(clean_values)) 
    return exp_v / exp_v.sum()

def main():
    output_model_file = "out_medium.csv" 
    ground_truth_file = "../datasets/ground-truth/big-five-ocean.csv"
    results_destination = "results_MEDIUM_FINAL.csv"
    country_code = "Japan"

    print("--- Memulai Evaluasi Final (25 Soal) ---")
    
    data = pd.read_csv(output_model_file)
    gt_df = pd.read_csv(ground_truth_file)
    
    # Filter data manusia Jepang
    c_gt = gt_df[gt_df.country == country_code]
    if len(c_gt) == 0:
        c_gt = gt_df
    
    traits_list = ['O', 'C', 'E', 'A', 'N']
    probs_cols = ['a_prob', 'b_prob', 'c_prob', 'd_prob', 'e_prob']
    scores_map = [5, 4, 3, 2, 1] # Mapping standar CulturalPersonas

    final_results = {}

    for i, trait in enumerate(traits_list):
        # Ambil 5 baris untuk masing-masing trait
        start_idx = i * 5
        end_idx = start_idx + 5
        trait_rows = data.iloc[start_idx:end_idx]
        
        all_model_scores = []
        for _, row in trait_rows.iterrows():
            probs = calculate_probs_safe(row[probs_cols].values)
            # Hitung skor ekspektasi (1-5)
            q_score = np.sum(probs * np.array(scores_map))
            all_model_scores.append(q_score)
        
        model_mean = np.mean(all_model_scores)
        human_mean = c_gt[trait].mean()
        
        # Hitung KS Statistic
        # Membandingkan distribusi skor model vs distribusi skor manusia
        ks_stat, _ = ks_2samp(all_model_scores, c_gt[trait])
        
        final_results[trait] = {
            'Model_Mean': model_mean,
            'Human_Mean': human_mean,
            'KS_Stat': ks_stat
        }

    res_df = pd.DataFrame(final_results).T
    res_df.to_csv(results_destination)
    
    print("\n--- TABEL HASIL REPRO DILLA ---")
    print(res_df)
    print(f"\nRata-rata KS Stat: {res_df['KS_Stat'].mean():.4f}")
    print(f"\nFile berhasil disimpan ke: {results_destination}")

if __name__ == "__main__":
    main()