import numpy as np
import matplotlib.pyplot as plt

# Parameters
K = 270          # put strike
premium = 5      # premium received
contract_size = 100

# Stock range
S = np.linspace(240, 320, 100)

# Payoff per contract (short put, cash set aside to buy the stock if assigned)
payoff = (premium - np.maximum(K - S, 0)) * contract_size

# Break-even and max profit
breakeven = K - premium
max_profit = premium * contract_size

# Separate profit/loss
profit = np.where(payoff > 0, payoff, np.nan)
loss = np.where(payoff <= 0, payoff, np.nan)

# Plot
plt.figure()

plt.plot(S, profit, color='green', label="Profit")
plt.plot(S, loss, color='red', label="Loss")

# Reference lines
plt.axhline(0)
plt.axvline(K, linestyle='--', label="Strike (270)")

# Break-even point
plt.scatter(breakeven, 0)
plt.text(breakeven, 0, f"  BE: {breakeven}", verticalalignment='bottom')

# Max profit point (flat region)
plt.scatter(K, max_profit)
plt.text(K, max_profit, f"  Max Profit: {max_profit}", verticalalignment='bottom')

# Labels
plt.title("Cash-Secured Put Payoff per Contract (100 shares)")
plt.xlabel("Stock Price at Expiration")
plt.ylabel("Profit (€)")

plt.legend()
plt.grid()

plt.show()
