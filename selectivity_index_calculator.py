# Selectivity Index (SI) Calculator for Anticancer Compounds
# This script computes the Selectivity Index to evaluate the safety profile of synthesized hybrids.

def calculate_selectivity_index(compound_name, healthy_ic50, cancer_ic50):
    """
    Calculates the Selectivity Index (SI) of a compound.
    SI = IC50 on normal (healthy) cell line / IC50 on cancer cell line
    
    An SI value >= 10.0 is globally recognized as highly selective and safe,
    indicating that the compound is significantly more toxic to cancer cells than healthy host cells.
    """
    si = healthy_ic50 / cancer_ic50
    
    if si >= 10.0:
        evaluation = "EXCELLENT: HIGHLY SELECTIVE & SAFE (SI >= 10)"
    elif si >= 2.0:
        evaluation = "MODERATE: MODERATELY SELECTIVE (2 <= SI < 10)"
    else:
        evaluation = "POOR: HIGHLY TOXIC TO HEALTHY CELLS (SI < 2)"
        
    print(f"--- Selectivity Index (SI) Report for {compound_name} ---")
    print(f"  Healthy Cell Line IC50: {healthy_ic50:.2f} uM")
    print(f"  Cancer Cell Line IC50: {cancer_ic50:.2f} uM")
    print(f"  Calculated Selectivity Index (SI): {si:.2f}")
    print(f"  Safety Evaluation: {evaluation}")
    print("-" * 65)
    return si

# Example: Triazole Hybrid Compound 4b
# Assuming IC50 on normal fibroblast cells (L929) is 112.5 uM
# and IC50 on cancer cells (HeLa) is 8.42 uM
calculate_selectivity_index(
    compound_name="Triazole Hybrid Compound 4b",
    healthy_ic50=112.5,  # IC50 on normal cells (uM)
    cancer_ic50=8.42     # IC50 on HeLa cancer cells (uM)
)
