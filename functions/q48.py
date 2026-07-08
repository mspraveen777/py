def tax_calculator(income):
    if income <= 250000:
        return f"Tax amount = 0"
    elif income  > 250000 and income < 500000:
        return f"Tax amount = {(income*5)/100}"
    elif income  > 500000 and income < 1000000:
        return f"Tax amount = {(income*20)/100}"
    return f"Tax amount = {(income *30)/100}"
tax_amount = tax_calculator(1200000)
print(tax_amount)
