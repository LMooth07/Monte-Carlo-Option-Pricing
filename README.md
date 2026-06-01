# Monte-Carlo-Option-Pricing
## Overview
This project mplements a Monte Carlo simulation to price European call options
This model:
- Downloads historical Apple stock data using yahoo finance
- Estimates volatility and drift from historical data over a four year period
- Simulates stock prices using a geometric Brownian motion model
- Prices options using a Monte Carlo simulation with an adjustable amount of simulations
- Has the option to compare against the Black-Scholes formula

Modules used:
- numpy
- matplotlib
- yfinance
- scipy

Key concepts:
- Volatility estimation from a data set
- Geometric Brownian motion
- Black-Scholes option pricing

## Background 
Options are financial derivatives that give the holder the option to purchase stock for a predetermined price after a maturity period. Since future stock prices are uncertain, probabalistic models can be used to estimate option values. This project uses Monte Carlo simulation to estimate the value of a European call option and compares the result with the analytical Black-Scholes solution.

## Mathematical Background 
### Geometric Brownian Motion
The stock price is assumed to follow geometic brownian motion satisfying the equation:
```math
dS_t = \mu S_tdt + \sigma S_tdW_t
```
Where:
- S_t is the stock price at time t
- μ is the drift parameter, representing the expected rate of return
- σ is the volatility parameter, representing the uncertainty in returns
- W_t is a standard Brownian motion

### Parameter estimation:
The geometric Brownian Motion model requires estimates for both drift and volatility parameters.
##### Drift
```math
\hat{\mu} = 252 \times \text{mean(log returns)}
```
The daily log returns are annualised using the approximate number of trading days in the year, 252.
##### Volatility
```math
\hat{\sigma} = \sqrt{252} \times \text{std(log returns)}
```
The standard deviation is scaled in a similar way but uses √252 instead as we are using STD and not variance.

### Log returns:
``` math
R_t = \ln\left(\frac{S_t}{S_{t-1}}\right)
```
Log returns are more useful for analisis than returns as they are addative and align with the assumptions of Geometric Brownian Motion.

### Monte Carlo simulation:
The stock price path is simulated using the Euler-Maruyama approximation:
```math
S_{t+\Delta t}
=
S_t
+
\mu S_t \Delta t
+
\sigma S_t \sqrt{\Delta t} Z
```
Where:
```math
Z \sim N(0,1)
```
### Option payoff:
The payoff of a European call option is:
```math
\max(S_T-K,0)
```
Where:

- S_T is the stock price at expiry
- K is the strike price

The average payoff across all simulations provides an estimate of the option value.

### Black-Scholes comparison:
```math
C=S_0N(d_1)-Ke^{-rT}N(d_2)
```
This gives a rough idea for validating the simulated value.
