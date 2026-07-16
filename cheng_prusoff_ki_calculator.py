# Cheng-Prusoff Ki Calculator for Enzyme Inhibition Assays
# This script computes the absolute inhibition constant (Ki) from experimental IC50 values.

def calculate_ki_cheng_prusoff(compound_name, ic50_uM, substrate_conc_uM, Km_uM, inhibition_type="competitive"):
    """
    Calculates the absolute inhibition constant (Ki) using the Cheng-Prusoff equation.
    
    Formulas:
    1. For Competitive Inhibition:
       Ki = IC50 / (1 + [S] / Km)
    
    Where:
    - IC50: Half-maximal inhibitory concentration.
    - [S] (substrate_conc_uM): Substrate concentration used in the assay.
    - Km (Km_uM): Michaelis-Menten constant of the substrate for the enzyme.
    """
    if inhibition_type.lower() == "competitive":
        # Ki = IC50 / (1 + [S]/Km)
        ki = ic50_uM / (1 + (substrate_conc_uM / Km_uM))
    else:
        raise ValueError("This calculator currently supports standard competitive inhibition modeling.")
        
    print(f"--- Cheng-Prusoff Ki Calculation Report for {compound_name} ---")
    print(f"  Inhibition Model: {inhibition_type.capitalize()}")
    print(f"  Experimental IC50: {ic50_uM:.2f} uM")
    print(f"  Substrate Concentration [S]: {substrate_conc_uM:.2f} uM")
    print(f"  Enzyme Michaelis Constant (Km): {Km_uM:.2f} uM")
    print(f"  Calculated Inhibition Constant (Ki): {ki:.3f} uM")
    print("-" * 65)
    return ki

# Example: Calculate Ki for Triazole Hybrid Compound 4b
# Assuming a competitive enzyme assay where [S] = 150 uM and Km = 50 uM
calculate_ki_cheng_prusoff(
    compound_name="Triazole Hybrid Compound 4b",
    ic50_uM=8.42,              # From our biological evaluation
    substrate_conc_uM=150.0,   # Substrate concentration in micromolar
    Km_uM=50.0                 # Michaelis constant in micromolar
)
