import numpy as np
import matplotlib.pyplot as plt

# Parameters
K1 = 270   # lower strike (long call)
K2 = 290   # higher strike (short call)

premium1 = 5   # paid (long call at K1)
premium2 = 3   # received (short call at K2)

C = premium1 - premium2   # net premium (debit)
contract_size = 100

# Stock price range at expiration
S = np.linspace(240, 320, 100)

# Payoff per share
payoff = np.maximum(S - K1, 0) - np.maximum(S - K2, 0) - C

# Scale to contract
payoff_total = payoff * contract_size

# Key metrics
breakeven = K1 + C
max_profit = (K2 - K1 - C) * contract_size
max_loss = -C * contract_size

# Separate profit/loss for coloring
profit = np.where(payoff_total > 0, payoff_total, np.nan)
loss = np.where(payoff_total <= 0, payoff_total, np.nan)

# Plot
plt.figure()

plt.plot(S, profit, color='green', label="Profit")
plt.plot(S, loss, color='red', label="Loss")

# Reference lines
plt.axhline(0)
plt.axvline(K1, linestyle='--', label="K1")
plt.axvline(K2, linestyle='--', label="K2")
plt.axvline(breakeven, color='red', linestyle='-.', label="Breakeven")

# Labels
plt.title("Bull Call Spread Payoff (per contract)")
plt.xlabel("Stock Price at Expiration")
plt.ylabel("Profit (€)")

# Annotate max profit / loss
plt.text(S[0], max_loss, f"Max Loss = {max_loss:.0f}", verticalalignment='bottom')
plt.text(S[-1], max_profit, f"Max Profit = {max_profit:.0f}", horizontalalignment='right')

plt.legend()
plt.grid()

plt.show()