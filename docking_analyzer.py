"""
AutoDock Rescore & Statistical Screening Pipeline
Author: tabantavanmand
Role: Sole Developer & Script Author
Description:
    Automated Python tool for filtering, ranking, and visualizing
    molecular docking screening data against Human Histamine H2 Receptor (H2R).
"""

import pandas as pd
import matplotlib.pyplot as plt
import os

def load_and_preprocess_data(filepath):
    """Load docking data and sort by binding affinity."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Data file not found at: {filepath}")
    
    df = pd.read_csv(filepath)
    # Sort from strongest binding (most negative) to weakest
    df_sorted = df.sort_values(by="mean_binding_energy", ascending=True).reset_index(drop=True)
    return df_sorted

def filter_top_candidates(df, drug_threshold=-8.42):
    """
    Filter compounds showing stronger binding affinity than reference control.
    Default threshold: -8.42 kcal/mol (Icotidine).
    """
    top_hits = df[df["mean_binding_energy"] <= drug_threshold].copy()
    top_hits["relative_improvement"] = drug_threshold - top_hits["mean_binding_energy"]
    return top_hits

def plot_screening_results(df, output_path="docking_energy_comparison.png"):
    """Generate publication-ready comparative bar plot for screened ligands."""
    plt.figure(figsize=(10, 6), dpi=300)
    
    # Define color scheme for categories
    color_map = {
        "phytochemical": "#2ecc71",
        "control": "#3498db",
        "drug_control": "#e74c3c"
    }
    bar_colors = [color_map.get(cat, "#95a5a6") for cat in df["category"]]
    
    bars = plt.barh(df["compound"] + " (" + df["ligand_id"] + ")", 
                    df["mean_binding_energy"], 
                    color=bar_colors, 
                    edgecolor="black", 
                    alpha=0.85)
    
    plt.axvline(x=-8.42, color="red", linestyle="--", linewidth=1.5, label="Icotidine Benchmark (-8.42 kcal/mol)")
    plt.axvline(x=-4.73, color="blue", linestyle=":", linewidth=1.2, label="Histamine Baseline (-4.73 kcal/mol)")
    
    plt.xlabel("Mean Binding Energy (kcal/mol)", fontsize=12, fontweight="bold")
    plt.ylabel("Screened Ligands / Controls", fontsize=12, fontweight="bold")
    plt.title("AutoDock Screening Results: Phytochemical Candidates vs Controls (H2R Target)", fontsize=13, fontweight="bold")
    plt.gca().invert_yaxis()  # Best affinity on top
    plt.grid(axis="x", linestyle="--", alpha=0.6)
    plt.legend(loc="lower right", frameon=True)
    plt.tight_layout()
    
    # Save the plot
    plt.savefig(output_path, dpi=300)
    plt.close()
    print(f"[+] Plot successfully saved to: {output_path}")

def run_pipeline(csv_path="data/docking_results.csv"):
    """Execute complete analysis workflow."""
    print("="*60)
    print("AutoDock Rescore & Statistical Screening Toolkit")
    print("="*60)
    
    # 1. Load Data
    df = load_and_preprocess_data(csv_path)
    print(f"[+] Loaded {len(df)} docking records.")
    
    # 2. Filter Leads
    top_hits = filter_top_candidates(df, drug_threshold=-8.42)
    print(f"[+] Found {len(top_hits)} candidate(s) outperforming reference drug (-8.42 kcal/mol):")
    for idx, row in top_hits.iterrows():
        print(f"    - {row['compound']} ({row['ligand_id']}): {row['mean_binding_energy']} kcal/mol | Source: {row['source_plant']}")
        
    # 3. Export Top Hits to CSV
    os.makedirs("results", exist_ok=True)
    top_hits_path = "results/top_screened_hits.csv"
    top_hits.to_csv(top_hits_path, index=False)
    print(f"[+] Top hits exported to: {top_hits_path}")
    
    # 4. Generate Visualization
    plot_path = "results/docking_energy_comparison.png"
    plot_screening_results(df, output_path=plot_path)
    print("="*60)
    print("Analysis pipeline executed successfully!")
    print("="*60)

if name == "main":
    # Standard execution entry point
    run_pipeline()
