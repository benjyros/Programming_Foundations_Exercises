# Programming Exercise 2-12: Stock Transaction Program
#
# Task: Write a program that calculates the profit or loss from a stock transaction.
#
# Requirements:
# 1. Calculate the amount paid for the stock (shares * purchase price)
# 2. Calculate the commission paid on the purchase (3% of amount paid)
# 3. Calculate the total amount paid (stock cost + purchase commission)
# 4. Calculate the amount the stock sold for (shares * selling price)
# 5. Calculate the commission paid on the sale (3% of selling amount)
# 6. Calculate the total amount received (selling amount - selling commission)
# 7. Calculate the profit or loss (total received - total paid)
# 8. Display all amounts formatted as currency
#
# Constants:
# - COMMISSION_RATE = 0.03 (3%)
# - NUM_SHARES = 2000
# - PURCHASE_PRICE = 40.0
# - SELLING_PRICE = 42.75
#
# Example output:
# Amount paid for the stock: $80,000.00
# Commission paid on the purchase: $2,400.00
# Amount the stock sold for: $85,500.00
# Commission paid on the sale: $2,565.00
# Profit (or loss if negative): $535.00

COMMISSION_RATE = 0.03
NUM_SHARES = 2000
PURCHASE_PRICE = 40.0
SELLING_PRICE = 42.75

amount_paid = NUM_SHARES * PURCHASE_PRICE
purchase_commission = amount_paid * COMMISSION_RATE
total_paid = amount_paid + purchase_commission
amount_sold = NUM_SHARES * SELLING_PRICE
selling_commission = amount_sold * COMMISSION_RATE
total_received = amount_sold - selling_commission
profit_loss = total_received - total_paid

print(f"""
Amount paid for the stock: ${amount_paid:,.2f}
Commission paid on the purchase: ${purchase_commission:,.2f}
Amount the stock sold for: ${amount_sold:,.2f}
Commission paid on the sale: ${selling_commission:,.2f}
Profit (or loss if negative): ${profit_loss:,.2f}
""")
