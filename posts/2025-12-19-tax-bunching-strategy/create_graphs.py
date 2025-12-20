"""
Create visualizations for tax bunching blog post
"""

import matplotlib.pyplot as plt
import numpy as np

# Set style
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 11

# Create output directory if it doesn't exist
import os
os.makedirs('images', exist_ok=True)

# Graph 1: Total Deductions Comparison (2-Year Total)
def create_deductions_comparison():
    strategies = ['Traditional\n(No Bunching)', 'Bunching\nStrategy']
    year1 = [36035, 53535]  # Year 1 deductions
    year2 = [36035, 31500]  # Year 2 deductions

    fig, ax = plt.subplots(figsize=(10, 6))

    x = np.arange(len(strategies))
    width = 0.35

    bars1 = ax.bar(x - width/2, year1, width, label='Year 1 Deductions',
                   color='#3498db', alpha=0.8)
    bars2 = ax.bar(x + width/2, year2, width, label='Year 2 Deductions',
                   color='#e74c3c', alpha=0.8)

    # Add total labels on top
    totals = [y1 + y2 for y1, y2 in zip(year1, year2)]
    for i, (bar1, bar2, total) in enumerate(zip(bars1, bars2, totals)):
        height = bar1.get_height() + bar2.get_height()
        ax.text(bar1.get_x() + width/2, height + 1000,
                f'Total: ${total:,}',
                ha='center', va='bottom', fontweight='bold', fontsize=12)

    ax.set_ylabel('Total Deductions ($)', fontsize=12, fontweight='bold')
    ax.set_title('Total Deductions Over 2 Years: Traditional vs Bunching',
                 fontsize=14, fontweight='bold', pad=20)
    ax.set_xticks(x)
    ax.set_xticklabels(strategies, fontsize=12)
    ax.legend(fontsize=11)
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x:,.0f}'))

    # Add annotation for extra deductions
    ax.annotate('Extra $7,035\nin deductions!',
                xy=(1, totals[1]), xytext=(0.5, totals[1] + 5000),
                arrowprops=dict(arrowstyle='->', color='green', lw=2),
                fontsize=11, color='green', fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.5', facecolor='lightgreen', alpha=0.7))

    plt.tight_layout()
    plt.savefig('images/deductions_comparison.png', dpi=300, bbox_inches='tight')
    print("Created: images/deductions_comparison.png")
    plt.close()


# Graph 2: Tax Savings Comparison (Old SALT Cap vs New SALT Cap)
def create_salt_cap_comparison():
    scenarios = ['Old SALT Cap\n($10k limit)\n2017-2024',
                 'New SALT Cap\n($40k limit)\n2025-2029']
    savings = [2530, 2803]

    fig, ax = plt.subplots(figsize=(10, 6))

    colors = ['#e74c3c', '#2ecc71']
    bars = ax.bar(scenarios, savings, color=colors, alpha=0.8, edgecolor='black', linewidth=1.5)

    # Add value labels on bars
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 30,
                f'${height:,.0f}',
                ha='center', va='bottom', fontsize=14, fontweight='bold')

    ax.set_ylabel('Tax Savings Over 2 Years ($)', fontsize=12, fontweight='bold')
    ax.set_title('Impact of SALT Cap Increase on Bunching Strategy Tax Savings',
                 fontsize=14, fontweight='bold', pad=20)
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x:,.0f}'))

    # Add percentage increase annotation
    pct_increase = ((1548 - 770) / 770) * 100
    ax.annotate(f'+{pct_increase:.0f}% increase\nin savings!',
                xy=(1, savings[1]), xytext=(0.5, savings[1] - 200),
                arrowprops=dict(arrowstyle='->', color='darkgreen', lw=2),
                fontsize=12, color='darkgreen', fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.5', facecolor='lightgreen', alpha=0.7))

    ax.set_ylim(0, max(savings) * 1.2)

    plt.tight_layout()
    plt.savefig('images/salt_cap_comparison.png', dpi=300, bbox_inches='tight')
    print("Created: images/salt_cap_comparison.png")
    plt.close()


# Graph 3: Itemized Deductions Breakdown (Year 1 Bunched vs Year 2 Light)
def create_deductions_breakdown():
    categories = ['Charity', 'Property Tax', 'State Income Tax', 'Mortgage Interest']
    year1_bunched = [30000, 7500, 6035, 10000]
    year2_light = [0, 2500, 6035, 10000]

    fig, ax = plt.subplots(figsize=(12, 7))

    colors = ['#3498db', '#e74c3c', '#f39c12', '#9b59b6']
    x = ['Year 1\n(Heavy Year)', 'Year 2\n(Light Year)']

    # Create stacked bar chart
    bottoms = [0, 0]

    for i, (category, color) in enumerate(zip(categories, colors)):
        values = [year1_bunched[i], year2_light[i]]
        bars = ax.bar(x, values, bottom=bottoms, label=category, color=color,
                      alpha=0.85, edgecolor='white', linewidth=2)

        # Add value labels for non-zero values
        for j, (bar, val) in enumerate(zip(bars, values)):
            if val > 0:
                height = bar.get_height()
                ax.text(bar.get_x() + bar.get_width()/2., bottoms[j] + height/2,
                        f'${val:,}',
                        ha='center', va='center', fontsize=11, fontweight='bold',
                        color='white')

        bottoms = [bottoms[j] + values[j] for j in range(len(values))]

    # Add total labels on top
    totals = [sum(year1_bunched), sum(year2_light)]
    for i, (total, bottom) in enumerate(zip(totals, bottoms)):
        ax.text(i, bottom + 1000, f'Total: ${total:,}',
                ha='center', va='bottom', fontsize=13, fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.5', facecolor='lightblue', alpha=0.8))

    # Add standard deduction reference line
    standard_deduction = 31500
    ax.axhline(y=standard_deduction, color='red', linestyle='--',
               linewidth=2, label=f'Standard Deduction: ${standard_deduction:,}', alpha=0.7)

    # Add annotation for Year 2
    ax.annotate('Use Standard\nDeduction Instead',
                xy=(1, standard_deduction), xytext=(1.3, standard_deduction + 3000),
                arrowprops=dict(arrowstyle='->', color='red', lw=2),
                fontsize=11, color='red', fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.5', facecolor='lightyellow', alpha=0.8))

    ax.set_ylabel('Deductions ($)', fontsize=12, fontweight='bold')
    ax.set_title('Itemized Deductions Breakdown: Year 1 (Bunched) vs Year 2 (Light)',
                 fontsize=14, fontweight='bold', pad=20)
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x:,.0f}'))
    ax.legend(loc='upper left', fontsize=11, framealpha=0.9)
    ax.set_ylim(0, max(bottoms) * 1.15)

    plt.tight_layout()
    plt.savefig('images/deductions_breakdown.png', dpi=300, bbox_inches='tight')
    print("Created: images/deductions_breakdown.png")
    plt.close()


# Graph 4: Threshold Analysis - When Does Bunching Start to Work?
def create_threshold_analysis():
    # Different mortgage interest scenarios
    mortgage_interest = np.array([0, 5000, 10000, 15000, 20000])

    # Fixed components
    charity_bunched = 30000
    property_tax_accelerated = 7500
    state_tax = 6035

    # Calculate total itemized deductions for each scenario
    total_itemized = charity_bunched + property_tax_accelerated + state_tax + mortgage_interest

    standard_deduction = 31500

    fig, ax = plt.subplots(figsize=(12, 7))

    # Plot the line
    ax.plot(mortgage_interest, total_itemized, marker='o', linewidth=3,
            markersize=10, color='#3498db', label='Total Itemized Deductions')

    # Add horizontal line for standard deduction
    ax.axhline(y=standard_deduction, color='#e74c3c', linestyle='--',
               linewidth=2, label='Standard Deduction ($31,500)')

    # Shade the region where bunching works
    ax.fill_between(mortgage_interest, standard_deduction, total_itemized,
                     where=(total_itemized >= standard_deduction),
                     alpha=0.3, color='green', label='Bunching Works Here!')

    # Add value labels on each point
    for x, y in zip(mortgage_interest, total_itemized):
        ax.text(x, y + 1000, f'${y:,}', ha='center', va='bottom',
                fontsize=10, fontweight='bold')

    ax.set_xlabel('Annual Mortgage Interest ($)', fontsize=12, fontweight='bold')
    ax.set_ylabel('Total Year 1 Itemized Deductions ($)', fontsize=12, fontweight='bold')
    ax.set_title('When Does Bunching Make Sense?\n(Charity: $30k over 2 years, Accelerated Property Tax: $7.5k, State Tax: $6k)',
                 fontsize=14, fontweight='bold', pad=20)
    ax.legend(fontsize=11, loc='lower right')
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x:,.0f}'))
    ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x:,.0f}'))
    ax.grid(True, alpha=0.3)

    # Add annotation
    ax.annotate('With $10k mortgage interest,\nyou beat the standard deduction\nby $22,035!',
                xy=(10000, total_itemized[2]), xytext=(12000, 50000),
                arrowprops=dict(arrowstyle='->', color='green', lw=2),
                fontsize=11, color='darkgreen', fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.5', facecolor='lightgreen', alpha=0.8))

    plt.tight_layout()
    plt.savefig('images/threshold_analysis.png', dpi=300, bbox_inches='tight')
    print("Created: images/threshold_analysis.png")
    plt.close()


# Graph 5: Tax Comparison Table (as an image)
def create_tax_comparison_table():
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.axis('tight')
    ax.axis('off')

    table_data = [
        ['', 'Traditional Approach', 'Bunching Strategy'],
        ['', '', ''],
        ['YEAR 1', '', ''],
        ['Charitable Contributions', '$15,000', '$30,000 (2 years!)'],
        ['Property Tax', '$5,000', '$7,500 (3 payments)'],
        ['State Income Tax', '$6,035', '$6,035'],
        ['Mortgage Interest', '$10,000', '$10,000'],
        ['Total Itemized', '$36,035', '$53,535 ✓'],
        ['Deduction Used', 'Itemized ($36,035)', 'Itemized ($53,535)'],
        ['Federal Tax', '$14,900', '$11,099'],
        ['', '', ''],
        ['YEAR 2', '', ''],
        ['Charitable Contributions', '$15,000', '$0'],
        ['Property Tax', '$5,000', '$2,500'],
        ['State Income Tax', '$6,035', '$6,035'],
        ['Mortgage Interest', '$10,000', '$10,000'],
        ['Total Itemized', '$36,035', '$18,535'],
        ['Deduction Used', 'Itemized ($36,035)', 'Standard ($31,500)'],
        ['Federal Tax', '$14,900', '$15,898'],
        ['', '', ''],
        ['2-YEAR TOTALS', '', ''],
        ['Total Deductions', '$72,070', '$85,035'],
        ['Total Federal Tax', '$29,800', '$26,997'],
        ['TAX SAVINGS', '-', '$2,803 💰'],
    ]

    # Create color mapping
    colors = []
    for i, row in enumerate(table_data):
        if i == 0:  # Header
            colors.append(['#2c3e50'] * 3)
        elif i in [2, 11, 20]:  # Section headers
            colors.append(['#34495e'] * 3)
        elif i == len(table_data) - 1:  # Last row (savings)
            colors.append(['white', 'white', '#2ecc71'])
        else:
            colors.append(['white'] * 3)

    table = ax.table(cellText=table_data, cellLoc='left', loc='center',
                     cellColours=colors, colWidths=[0.25, 0.35, 0.35])

    table.auto_set_font_size(False)
    table.set_fontsize(11)
    table.scale(1, 2.5)

    # Style the header row
    for i in range(3):
        cell = table[(0, i)]
        cell.set_text_props(weight='bold', color='white', size=13)
        cell.set_facecolor('#2c3e50')

    # Style section headers
    for row_idx in [2, 11, 20]:
        for col_idx in range(3):
            cell = table[(row_idx, col_idx)]
            cell.set_text_props(weight='bold', color='white', size=12)
            cell.set_facecolor('#34495e')

    # Style the last row (savings)
    for col_idx in range(3):
        cell = table[(len(table_data) - 1, col_idx)]
        cell.set_text_props(weight='bold', size=12)

    # Highlight Year 1 itemized amounts
    for row_idx in [7, 8, 9]:
        cell = table[(row_idx, 2)]
        cell.set_text_props(weight='bold')

    plt.title('Tax Bunching: Complete 2-Year Comparison\n$150k Income | MFJ | California | 2025 Tax Law',
              fontsize=15, fontweight='bold', pad=20)

    plt.savefig('images/tax_comparison_table.png', dpi=300, bbox_inches='tight')
    print("Created: images/tax_comparison_table.png")
    plt.close()


# Graph 6: Savings by Income Level (showing who benefits most)
def create_savings_by_income():
    # Different income levels
    incomes = np.array([100, 125, 150, 175, 200, 250, 300])  # in thousands

    # Approximate state tax at different income levels (California progressive)
    state_taxes = np.array([3000, 4500, 6035, 7500, 10300, 15000, 20000])

    # Calculate total itemized deductions (bunched year)
    charity = incomes * 1000 * 0.10  # 10% of income over 2 years
    property_tax = 7500  # constant
    mortgage = 10000  # constant

    total_itemized = charity + property_tax + state_taxes + mortgage
    standard = 31500

    # Calculate extra deductions
    extra_deductions = np.maximum(0, total_itemized - standard)

    # Calculate savings (22% bracket for most, 24% for higher incomes)
    tax_rates = np.where(incomes <= 206.7, 0.22, 0.24)
    savings = extra_deductions * tax_rates

    fig, ax = plt.subplots(figsize=(12, 7))

    # Create bar chart
    bars = ax.bar(incomes, savings, color='#2ecc71', alpha=0.8,
                   edgecolor='black', linewidth=1.5)

    # Add value labels
    for bar in bars:
        height = bar.get_height()
        if height > 0:
            ax.text(bar.get_x() + bar.get_width()/2., height + 50,
                    f'${height:,.0f}',
                    ha='center', va='bottom', fontsize=10, fontweight='bold')

    ax.set_xlabel('Household Income ($1000s)', fontsize=12, fontweight='bold')
    ax.set_ylabel('Tax Savings Over 2 Years ($)', fontsize=12, fontweight='bold')
    ax.set_title('Tax Bunching Savings by Income Level\n(10% Charity | $10k Mortgage | $5k Property Tax | California)',
                 fontsize=14, fontweight='bold', pad=20)
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x:,.0f}'))
    ax.set_xticks(incomes)
    ax.set_xticklabels([f'${x}k' for x in incomes])
    ax.grid(True, alpha=0.3, axis='y')

    # Add annotation
    ax.annotate('Higher income = more state tax\n= more benefit from bunching',
                xy=(250, savings[5]), xytext=(200, savings[5] + 500),
                arrowprops=dict(arrowstyle='->', color='darkgreen', lw=2),
                fontsize=11, color='darkgreen', fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.5', facecolor='lightgreen', alpha=0.7))

    plt.tight_layout()
    plt.savefig('images/savings_by_income.png', dpi=300, bbox_inches='tight')
    print("Created: images/savings_by_income.png")
    plt.close()


if __name__ == '__main__':
    print("Creating visualizations for tax bunching blog post...")
    print("-" * 60)

    create_deductions_comparison()
    create_salt_cap_comparison()
    create_deductions_breakdown()
    create_threshold_analysis()
    create_tax_comparison_table()
    create_savings_by_income()

    print("-" * 60)
    print("All visualizations created successfully!")
    print("\nGenerated files:")
    print("  - images/deductions_comparison.png")
    print("  - images/salt_cap_comparison.png")
    print("  - images/deductions_breakdown.png")
    print("  - images/threshold_analysis.png")
    print("  - images/tax_comparison_table.png")
    print("  - images/savings_by_income.png")
