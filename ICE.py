# ICE Simulation Notebook

# This notebook simulates reducing-balance loans under conventional EMI and ICE-aligned repayment strategies.


import numpy as np
import pandas as pd

# Loan parameters
loan_amount = 500000  # principal
annual_rate = 0.10    # interest rate
tenure_months = 60    # 5 years
EMI = 10600           # monthly EMI

# Function to simulate conventional EMI repayment
def simulate_emi(principal, rate, months, EMI):
    balance = principal
    monthly_rate = rate / 12
    history = []
    for month in range(1, months+1):
        interest = balance * monthly_rate
        principal_payment = EMI - interest
        balance -= principal_payment
        history.append([month, EMI, interest, principal_payment, balance])
    return pd.DataFrame(history, columns=['Month','EMI Paid','Interest','Principal','Outstanding Principal'])

# Function to simulate ICE-aligned repayment
def simulate_ice(principal, rate, months, EMI, extra_payment=0):
    balance = principal
    monthly_rate = rate / 12
    history = []
    for month in range(1, months+1):
        # Assume EMI paid at start of month + extra payment
        total_payment = EMI + extra_payment
        interest = balance * monthly_rate
        principal_payment = total_payment - interest
        balance -= principal_payment
        history.append([month, total_payment, interest, principal_payment, balance])
    return pd.DataFrame(history, columns=['Month','EMI Paid','Interest','Principal','Outstanding Principal'])

# Simulate
emi_df = simulate_emi(loan_amount, annual_rate, 12, EMI)
ice_df = simulate_ice(loan_amount, annual_rate, 12, EMI, extra_payment=1000)

# Display results
print("Conventional EMI Repayment (12 months)")
print(emi_df)

print("\nICE-Aligned Repayment (12 months)")
print(ice_df)

