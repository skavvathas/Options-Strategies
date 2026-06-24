Options Strategies Visualization

Options call strategies:
- **Long call** — buy a call to profit from a rising stock price with limited downside (the premium paid).
- **Protective call** — hold a short stock position and buy a call to cap the loss if the price rises.
- **Covered call** — own the stock and sell a call to earn premium income while capping upside.
- **Bull call spread** — buy a lower-strike call and sell a higher-strike call to bet on a moderate price rise at lower cost.

Options put strategies:
- **Long put** — buy a put to profit from a falling stock price with limited downside (the premium paid).
- **Protective put** — own the stock and buy a put to insure against a drop in price.
- **Bear put spread** — buy a higher-strike put and sell a lower-strike put to bet on a moderate price fall at lower cost.
- **Cash-secured put** — sell a put while holding cash to buy the stock if assigned, earning premium income.

## Requirements

Install the dependencies:

```bash
pip install numpy matplotlib
```

## How to run

Each strategy is a standalone script. Run it with Python to display its payoff chart:

```bash
python long_call.py
python protective_call.py
python covered_call.py
python bull_call_spread.py
python long_put.py
python protective_put.py
python cash_secured_put.py
```