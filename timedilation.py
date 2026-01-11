"""
Black Hole Time Dilation Calculator
Author: Jits Doomen
Description: Calculates gravitational time dilation near a Schwarzschild black hole.
"""

import math

# 1. CONSTANTS
GRAVIT_CONSTANT = 6.6743e-11
SOL = 299792458
SUN_MASS = 1.989e30

# 2. EVENT HORIZON FUNCTION
def calculate_schwarzschild_radius(mass_kg):
    rs = (2 * GRAVIT_CONSTANT * mass_kg) / (SOL**2)
    return rs

# 3. TIME DILATION FUNCTION
def calculate_time_dilation(r, rs):
    t_ratio = math.sqrt(1 - rs / r)
    return t_ratio

# 4. USER INPUT & PROCESSING
SOL_MASS = float(input("How many solar masses?: "))
MASS_KG = SOL_MASS * SUN_MASS
DIS = float(input("How many kilometers distance is there between the BH and you?: "))
DIS_M = DIS * 1000

# 5. CALCULATIONS
rs_value = calculate_schwarzschild_radius(MASS_KG)

# 6. THE RELATIVITY REPORT
if DIS_M <= rs_value:
    print(f"The Shwarzschild radius is {rs_value:.2f} meters.")
    print(f"You have crossed the event horizon. You will be spaghettified soon. Thank you for your patience.")
else:
    ratio = calculate_time_dilation(DIS_M, rs_value)
    earth_years = 1 / ratio

    if DIS_M < (rs_value * 1.5):
        print("WARNING: High tidal forces detected!")

    print(f"Answer:")
    print(f"For every 1 year you experience near the black hole,")
    print(f"{earth_years:.2f} years pass on Earth.")