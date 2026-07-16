import numpy as np

# Ligand Efficiency (LE) Calculator for Novel Triazole-Quinolone Hybrids
# This script computes the binding efficiency per heavy atom based on experimental IC50 values.

def calculate_ligand_efficiency(compound_name, ic50_uM, heavy_atom_count):
    """
    Calculates the Ligand Efficiency (LE) of a compound.
    LE is defined as the Gibbs free energy of binding (delta G) divided by the number of heavy atoms (N).
    LE = -delta G / N
    
    Where:
    - delta G = R * T * ln(Kd) -> Approximated using IC50 (in Molar) at T = 298.15 K (25 degrees C).
    - R (Gas constant) = 0.0019872 kcal/(mol*K)
    - Target LE for a promising drug candidate is typically >= 0.3 kcal/mol per heavy atom.
    """
    # Convert IC50 from micromolar (uM) to Molar (M)
    ic50_molar = ic50_uM * 1e-6
    
    # Constants
    R = 0.0019872  # kcal/(mol * K)
    T = 298.15     # Temperature in Kelvin (25 C)
    
    # Calculate Gibbs Free Energy of binding (delta G) in kcal/mol
    # Using Ki approximation where Ki ~ IC50
    delta_g = R * T * np.log(ic50_molar)
    
    # Calculate Ligand Efficiency (LE)
    ligand_efficiency = -delta_g / heavy_atom_count
    
    # Evaluation
    status = "EXCELLENT (>= 0.3)" if ligand_efficiency >= 0.3 else "MODERATE (< 0.3)"
    
    print(f"--- Ligand Efficiency Report for {compound_name} ---")
    print(f"  Experimental IC50: {ic50_uM} uM")
    print(f"  Heavy Atom Count (N): {heavy_atom_count}")
    print(f"  Calculated delta G: {delta_g:.2f} kcal/mol")
    print(f"  Ligand Efficiency (LE): {ligand_efficiency:.3f} kcal/mol per heavy atom")
    print(f"  Evaluation Status: {status}")
    print("-" * 60)

# Example: Run calculation for Triazole Hybrid Compound 4b
# N = 33 heavy atoms (excluding Hydrogens) for a typical 7-methoxyquinolone-triazole scaffold
calculate_ligand_efficiency(
    compound_name="Triazole Hybrid Compound 4b",
    ic50_uM=8.42,          # From our experimental cytotoxicity assay
    heavy_atom_count=33    # Number of C, N, O atoms in the hybrid core
)
