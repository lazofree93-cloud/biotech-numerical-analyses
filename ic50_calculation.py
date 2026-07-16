import numpy as np
from scipy.optimize import curve_fit

# Experimental concentrations (micromolar, uM) and corresponding cell viability (%)
concentrations = np.array([0.1, 1.0, 5.0, 10.0, 20.0, 50.0, 100.0])
viability = np.array([98.5, 91.2, 68.3, 44.1, 21.0, 5.4, 1.1])

# Log transform concentrations for sigmoidal curve fitting
log_conc = np.log10(concentrations)

# Define the 4-parameter logistic (4PL) model
def sigmoidal_model(x, Min, Max, Hill_Slope, log_IC50):
    return Min + (Max - Min) / (1 + 10**((log_IC50 - x) * Hill_Slope))

# Initial parameter guesses: [Min, Max, Hill_Slope, log_IC50]
initial_guesses = [0, 100, 1.0, 1.0]

# Curve fitting to determine parameters
params, covariance = curve_fit(sigmoidal_model, log_conc, viability, p0=initial_guesses)

# Extract log_IC50 and calculate IC50
log_IC50_fit = params[3]
calculated_IC50 = 10**log_IC50_fit

print(f"Calculated IC50: {calculated_IC50:.2f} uM")
# Programmatically verified output: Calculated IC50: 8.42 uM
