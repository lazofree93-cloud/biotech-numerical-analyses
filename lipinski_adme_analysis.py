# Lipinski's Rule of 5 Analysis for Novel Triazole-Quinolone Hybrids
# This script evaluates the drug-likeness parameters of synthesized compounds.

def evaluate_lipinski(compound_name, mw, logp, hbd, hba):
    """
    Evaluates if a compound complies with Lipinski's Rule of 5.
    Criteria:
    1. Molecular Weight (MW) <= 500 Da
    2. Octanol-water partition coefficient (LogP) <= 5
    3. Hydrogen Bond Donors (HBD) <= 5
    4. Hydrogen Bond Acceptors (HBA) <= 10
    """
    violations = 0
    report = []

    # Check Molecular Weight
    if mw <= 500:
        report.append(f"  [PASS] Molecular Weight: {mw} Da (Limit: <= 500)")
    else:
        report.append(f"  [FAIL] Molecular Weight: {mw} Da (Limit: <= 500)")
        violations += 1

    # Check LogP
    if logp <= 5.0:
        report.append(f"  [PASS] LogP (Lipophilicity): {logp} (Limit: <= 5)")
    else:
        report.append(f"  [FAIL] LogP (Lipophilicity): {logp} (Limit: <= 5)")
        violations += 1

    # Check Hydrogen Bond Donors
    if hbd <= 5:
        report.append(f"  [PASS] Hydrogen Bond Donors: {hbd} (Limit: <= 5)")
    else:
        report.append(f"  [FAIL] Hydrogen Bond Donors: {hbd} (Limit: <= 5)")
        violations += 1

    # Check Hydrogen Bond Acceptors
    if hba <= 10:
        report.append(f"  [PASS] Hydrogen Bond Acceptors: {hba} (Limit: <= 10)")
    else:
        report.append(f"  [FAIL] Hydrogen Bond Acceptors: {hba} (Limit: <= 10)")
        violations += 1

    # Conclusion
    is_drug_like = "YES" if violations <= 1 else "NO"
    
    print(f"--- ADME Evaluation Report for {compound_name} ---")
    for line in report:
        print(line)
    print(f"Total Violations: {violations}")
    print(f"Suitable for Oral Bioavailability: {is_drug_like}")
    print("-" * 50)

# Example data representing a synthesized Triazole-Quinolone Hybrid (Compound 4b)
# These represent typical computed values for such molecular scaffolds
evaluate_lipinski(
    compound_name="Triazole Hybrid Compound 4b",
    mw=458.5,    # Molecular Weight in Daltons
    logp=3.82,   # Partition coefficient
    hbd=1,       # Number of hydrogen bond donors
    hba=7        # Number of hydrogen bond acceptors (including triazole & methoxyquinolone nitrogens/oxygens)
)
