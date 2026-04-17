
"""
Assignment 1: Neuron Voltage Simulator
Student Name: GENEVIEVE ONWU
Date: 27TH MARCH 2026
Course: NEUR 101 - Introduction to Programming with Python

This program simulates basic neuron voltage dynamics using Ohm's law.
It calculates how a neuron's membrane potential changes when current
is injected, and determines whether the neuron fires an action potential.

"""

import math

# ============================================================
# SECTION 1: WELCOME SCREEN
# ============================================================
print("=" * 60)
print(" " * 15 + "NEUROSCIENCE CALCULATOR v1.0")
print(" " * 10 + "Neuron Voltage Simulator")
print("=" * 60)
print()
print("This program models how a neuron's voltage changes")
print("when it receives an input current.")
print("Formula: ΔV = I × R  (Ohm's Law)")
print()

# ============================================================
# SECTION 2: GET USER INPUTS
# ============================================================
print("-" * 60)
print("Enter Neuron Parameters")
print("-" * 60)

# Get a neuron ID number from the user (whole number — use int)
# Example: neuron_id = int(input("Enter Neuron ID: "))
neuron_id = int(input("Enter Neuron ID (whole number): "))

# Get the neuron type as text — no conversion needed, stays a string
neuron_type = input("Enter Neuron Type (e.g., 'Pyramidal', 'Interneuron'): ").strip().title()

# Get the starting membrane voltage in mV (decimal — use float)
v_initial = float(input("Enter initial membrane voltage (mV, e.g., -70.0): "))
while v_initial < -100 or v_initial > 0:
    print("WARNING: Initial voltage should be between -100 and 0. Please enter a valid value.")
    v_initial = float(input("Enter initial membrane voltage (mV, e.g., -70.0): "))
else:
    print (v_initial)


# Get the injected current in nanoamps (decimal — use float)
i_current = float(input("Enter input current (nA, e.g., 0.5): "))
while i_current < -10 or i_current > 10:
    print("WARNING: Input current should be between -10 and 10 nA. Please enter a valid value.")
    i_current = float(input("Enter input current (nA, e.g., 0.5): "))
else:
    print(i_current)
# Get the membrane resistance in megaohms (decimal — use float)
r_membrane = float(input('Enter membrane resistance (MΩ, e.g., 100.0): '))
while r_membrane < 0:
    print("WARNING: Membrane resistance cannot be negative. Please enter a valid value.")
    r_membrane = float(input('Enter membrane resistance (MΩ, e.g., 100.0): '))
else:
    print(r_membrane)
# Get the duration of one time step in milliseconds (decimal — use float)
time_step = float(input("Enter time step duration (ms, e.g., 1.0): "))

print()

# ============================================================
# SECTION 3: CALCULATIONS
# ============================================================

# Calculate voltage change: ΔV = I × R
delta_v = i_current * r_membrane 

# Calculate new membrane potential: V_new = V_initial + ΔV
v_new = v_initial + delta_v

# Define the spike threshold (this one is done for you)
threshold = -55.0  # mV — the voltage at which an action potential fires

# Did the neuron spike? Create a boolean: True if v_new >= threshold
did_spike = True if v_new >= threshold else False

# How much more voltage is needed to reach threshold (only if no spike)?
if not did_spike:
    voltage_needed = threshold - v_new
else:
    voltage_needed = 0

# ============================================================
# SECTION 4: DISPLAY RESULTS
# ============================================================
print("=" * 60)
print(" " * 18 + "SIMULATION RESULTS")
print("=" * 60)
print()

print("NEURON INFORMATION:")
print(f"  Neuron ID:   {neuron_id}")
print(f"  Type:        {neuron_type}")
print()

print("INPUT PARAMETERS:")
print(f"  Initial voltage:     {v_initial} mV")
print(f"  Input current:       {i_current} nA")
print(f"  Membrane resistance: {r_membrane} MΩ")
print(f"  Time step:           {time_step} ms")
print()

print("CALCULATED RESULTS:")
# Display voltage change formatted to 2 decimal places
print(f"  Voltage change (ΔV):     {delta_v:.2f} mV")
# Display new voltage formatted to 2 decimal places
print(f"  New membrane potential:  {v_new:.2f} mV")
print(f"  Spike threshold:         {threshold} mV")
print()

print("SPIKE STATUS:")
if did_spike:
    print("  ⚡ SPIKE DETECTED!")
    print("  The neuron fired an action potential.")
    print(f"  Voltage exceeded threshold by {v_new - threshold:.2f} mV")
else:
    print("  ✗ No spike.")
    print(f"  Voltage is {threshold - v_new:.2f} mV below threshold.")
    # If resistance is valid, calculate how much more current would be needed
    if r_membrane > 0:
        current_needed = voltage_needed / r_membrane
        print(f"  Would need {current_needed:.2f} more nA to reach threshold.")

print()

# ============================================================
# SECTION 5: BIOLOGICAL INTERPRETATION
# ============================================================
print("-" * 60)
print("BIOLOGICAL INTERPRETATION:")
print("-" * 60)

if v_new <= -80:
    print("The neuron is hyperpolarized — more negative than resting.")
    print("Inhibitory inputs (or open K⁺ channels) are suppressing activity.")
elif v_new <= -65:
    print("The neuron is near its resting potential.")
    print("This is a normal, quiet state — no significant input received.")
elif v_new <= -55:
    print("The neuron is depolarized but has not yet reached threshold.")
    print("It's receiving excitatory input but not enough to fire.")
else:
    print("The neuron reached threshold and fired an action potential.")
    print("The spike will propagate down the axon to downstream neurons.")

print()

# ============================================================
# SECTION 6: FOOTER
# ============================================================
print("=" * 60)
print("Simulation complete.")
print("Keep exploring — one neuron at a time.")
print("=" * 60)

# ============================================================
# BONUS: Additional Calculations
# ============================================================
# BONUS 1: If the neuron fired, calculate the approximate firing rate.
# Firing rate (Hz) = 1000 / time_step (converts ms to spikes per second)
if did_spike:
    firing_rate = 1000 / time_step
    print(f"BONUS: Estimated firing rate: {firing_rate:.2f} Hz")

# BONUS 2: Handle division by zero if r_membrane = 0
# Add a check before the delta_v calculation that prints a warning
# and sets delta_v = 0 if r_membrane is zero.
if r_membrane == 0:
    print("WARNING: Membrane resistance cannot be zero. Setting voltage change to 0.")
    delta_v = 0




print('=' * 60)
print("CHALLENGE 2")
print('=' * 60)

print()

THRESHOLD = -55.0  # mV
Neuron1_current = float(input("Enter the current for Neuron 1 (nA): "))
Neuron1_resistance = 20
Neuron2_voltage = -52
Neuron3_voltage = -92
Neuron1_voltage = Neuron1_current * Neuron1_resistance
print(f"Neuron 1 new voltage: {Neuron1_voltage} mV")

if Neuron1_voltage >= THRESHOLD:
    print("Neuron 1 did spike an action potential! and triggered Neuron 2 to fire.")
    if Neuron2_voltage >= THRESHOLD:
        print("Neuron 2 did spike an action potential! and triggered Neuron 3 to fire.")
        if Neuron3_voltage >= THRESHOLD:
            print("Neuron 3 did spike an action potential!")
        else:
            print("There was not enough current from Neuron 2 to Neuron 3 to spike an action potential. The chain ended here.")
    else:
        print("There was not enough current from neuron 1 for Neuron 2 to spike an action potential. So it didn't trigger Neuron 3 and the chain ended here.")
else:
    print("Neuron 1 did not spike an action potential. So it didn't trigger Neuron 2 and the chain ended here.")