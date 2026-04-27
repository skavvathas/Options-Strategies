import numpy as np
import matplotlib.pyplot as plt

# Parameters
S0 = 270
K = 275
premium = 3
contract_size = 100

# Stock range
S = np.linspace(240, 320, 100)

# Payoff per contract
payoff = ((S - S0) + premium - np.maximum(S - K, 0)) * contract_size

# Break-even and max profit
breakeven = S0 - premium
max_profit = (K - S0 + premium) * contract_size

# Separate profit/loss
profit = np.where(payoff > 0, payoff, np.nan)
loss = np.where(payoff <= 0, payoff, np.nan)

# Plot
plt.figure()

plt.plot(S, profit, color='green', label="Profit")
plt.plot(S, loss, color='red', label="Loss")

# Reference lines
plt.axhline(0)
plt.axvline(K, linestyle='--', label="Strike (275)")
plt.axvline(S0, linestyle=':', label="Stock Price (270)")

# Break-even point
plt.scatter(breakeven, 0)
plt.text(breakeven, 0, f"  BE: {breakeven}", verticalalignment='bottom')

# Max profit point (flat region)
plt.scatter(K, max_profit)
plt.text(K, max_profit, f"  Max Profit: {max_profit}", verticalalignment='bottom')

# Labels
plt.title("Covered Call Payoff per Contract (100 shares)")
plt.xlabel("Stock Price at Expiration")
plt.ylabel("Profit (€)")

plt.legend()
plt.grid()

plt.show()