"""
Verify the tax bunching calculator for specific scenario
"""

# Inputs
income = 250000
charity_pct = 10
property_tax = 8000
mortgage_interest = 10000

# Calculate CA state tax
ca_std_deduction = 11080
ca_taxable = income - ca_std_deduction

# CA MFJ brackets
if ca_taxable <= 21512:
    state_tax = ca_taxable * 0.01
elif ca_taxable <= 50998:
    state_tax = 215 + (ca_taxable - 21512) * 0.02
elif ca_taxable <= 80490:
    state_tax = 805 + (ca_taxable - 50998) * 0.04
elif ca_taxable <= 111732:
    state_tax = 1985 + (ca_taxable - 80490) * 0.06
elif ca_taxable <= 141212:
    state_tax = 3860 + (ca_taxable - 111732) * 0.08
else:
    state_tax = 6220 + (ca_taxable - 141212) * 0.093

print(f"California State Tax: ${state_tax:,.2f}")

# Federal tax calculation function
def calc_federal_tax(taxable_income):
    if taxable_income <= 23850:
        return taxable_income * 0.10
    elif taxable_income <= 96950:
        return 2385 + (taxable_income - 23850) * 0.12
    elif taxable_income <= 206700:
        return 11157 + (taxable_income - 96950) * 0.22
    elif taxable_income <= 394600:
        return 35301 + (taxable_income - 206700) * 0.24
    else:
        return 80405 + (taxable_income - 394600) * 0.32

# Traditional approach
charity_per_year = income * charity_pct / 100
standard_deduction = 31500

traditional_itemized = charity_per_year + property_tax + state_tax + mortgage_interest
traditional_deduction = max(traditional_itemized, standard_deduction)
traditional_federal_tax = calc_federal_tax(income - traditional_deduction)
traditional_2year = traditional_federal_tax * 2

print(f"\n=== TRADITIONAL APPROACH ===")
print(f"Charity per year: ${charity_per_year:,.2f}")
print(f"Property tax: ${property_tax:,.2f}")
print(f"State tax: ${state_tax:,.2f}")
print(f"Mortgage interest: ${mortgage_interest:,.2f}")
print(f"Total itemized: ${traditional_itemized:,.2f}")
print(f"Using deduction: ${traditional_deduction:,.2f}")
print(f"Federal taxable income: ${income - traditional_deduction:,.2f}")
print(f"Federal tax per year: ${traditional_federal_tax:,.2f}")
print(f"2-year total federal tax: ${traditional_2year:,.2f}")

# Bunching approach
bunched_y1_itemized = (charity_per_year * 2) + (property_tax * 1.5) + state_tax + mortgage_interest
bunched_y1_federal = calc_federal_tax(income - bunched_y1_itemized)

bunched_y2_itemized = 0 + (property_tax * 0.5) + state_tax + mortgage_interest
bunched_y2_deduction = max(bunched_y2_itemized, standard_deduction)
bunched_y2_federal = calc_federal_tax(income - bunched_y2_deduction)

bunched_2year = bunched_y1_federal + bunched_y2_federal

print(f"\n=== BUNCHING APPROACH ===")
print(f"Year 1 charity: ${charity_per_year * 2:,.2f}")
print(f"Year 1 property tax: ${property_tax * 1.5:,.2f}")
print(f"Year 1 state tax: ${state_tax:,.2f}")
print(f"Year 1 mortgage: ${mortgage_interest:,.2f}")
print(f"Year 1 total itemized: ${bunched_y1_itemized:,.2f}")
print(f"Year 1 federal taxable income: ${income - bunched_y1_itemized:,.2f}")
print(f"Year 1 federal tax: ${bunched_y1_federal:,.2f}")

print(f"\nYear 2 charity: $0.00")
print(f"Year 2 property tax: ${property_tax * 0.5:,.2f}")
print(f"Year 2 state tax: ${state_tax:,.2f}")
print(f"Year 2 mortgage: ${mortgage_interest:,.2f}")
print(f"Year 2 total itemized: ${bunched_y2_itemized:,.2f}")
print(f"Year 2 using deduction: ${bunched_y2_deduction:,.2f}")
print(f"Year 2 federal taxable income: ${income - bunched_y2_deduction:,.2f}")
print(f"Year 2 federal tax: ${bunched_y2_federal:,.2f}")

print(f"\n2-year total federal tax: ${bunched_2year:,.2f}")

# Savings
savings = traditional_2year - bunched_2year
savings_pct = (savings / traditional_2year) * 100

print(f"\n=== RESULT ===")
print(f"Tax Savings: ${savings:,.2f}")
print(f"Savings percentage: {savings_pct:.2f}%")
print(f"Worth it? {'YES ✓' if savings > 100 else 'Marginal ⚠️' if savings > 0 else 'NO ✗'}")
