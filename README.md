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
Options are financial derivatives that give the holder the option to purchase stock for a predetermined price after a maturity period. Since future stock prices are uncertain, probabalistic models can be used to estimate option values. This project 
