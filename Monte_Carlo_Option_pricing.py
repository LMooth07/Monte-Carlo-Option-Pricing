#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 30 00:58:52 2026

@author: lucmoothia
"""

import numpy as np 
import matplotlib.pyplot as plt
import yfinance as yf
from scipy.stats import norm






def simulation (s0, r, sig, T, N):
    dt = T/N
    prices = [s0]
    for i in range (N):
        Z = np.random.normal()
        old_price = prices[-1]
        prices.append(old_price + r * old_price * dt + sig * old_price * np.sqrt(dt) * Z)
    plt.plot(prices)
    plt.xlabel('Days from s0')
    plt.ylabel('Stock Price')
    plt.title('Random Stock Price Simulation')

  
      
def repeated_simulation (s0, r, sig, T, N, M) :
    dt = T/N
    for j in range(M):
        prices = [s0]
        for i in range (N):
            Z = np.random.normal()
            old_price = prices[-1]
            prices.append(old_price + r * old_price * dt + sig * old_price * np.sqrt(dt) * Z)
        plt.plot (prices, linewidth='0.5')
    plt.xlabel('Days from s0')
    plt.ylabel('Stock Price')
    plt.title('Multiple Random Stock Price Simulation')
 
    
 
def option_price (s0, k, r, sig, T, N, M) :
    payoffs = []
    dt = T/N
    for j in range(M):
        prices = [s0]
        for i in range (N):
            Z = np.random.normal()
            old_price = prices[-1]
            prices.append(old_price + r * old_price * dt + sig * old_price * np.sqrt(dt) * Z)
        St = prices[-1]
        payoff=max(St - k,0)
        payoffs.append(payoff)
    option_price = np.exp(-r * T) * np.mean(payoffs)
    return option_price



def black_scholes_call(S0, K, r, sig, T):
    d1 = (np.log(S0 / K) + (r + 0.5 * sig**2) * T) / (sig * np.sqrt(T))
    d2 = d1 - sig * np.sqrt(T)
    return S0 * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)



def final_price_plot(s0, r, sig, T, N, M) :
    final_prices = []
    dt = T/N
    for j in range(M):
        prices = [s0]
        for i in range (N):
            Z = np.random.normal()
            old_price = prices[-1]
            prices.append(old_price + r * old_price * dt + sig * old_price * np.sqrt(dt) * Z)
        final_prices.append(prices[-1])
    plt.hist(final_prices, bins=50)
    plt.xlabel("Final Stock Price")
    plt.ylabel("Frequency")
    plt.title("Distribution of Simulated Final Stock Prices")



def convergence_plot(s0, k, r, sig, T, N):
    M_values = [100,300,500,750,1000,3000,5000,7500,10000,20000,50000]
    prices = []
    for M in M_values:
        prices.append(option_price(s0, k, r, sig, T, N, M))
    plt.plot(M_values, prices, marker='o')
    plt.xscale('log')
    plt.xlabel("Number of Simulations")
    plt.ylabel("Option Price Estimate")
    plt.title("Monte Carlo Convergence")



TSLA_data = yf.download('TSLA',
                        start = '2020-01-01',
                        end = '2026-05-31')


AAPL_data = yf.download('AAPL',
                   start = '2020-01-01',
                   end = '2025-01-01')



def AAPL_stock_plot ():
    AAPL_data["Close"].plot()
    plt.title('Apple Stock Price')

def TSLA_stock_plot ():
    TSLA_data["Close"].plot()
    plt.title('Tesla Stock Price')

    

AAPL_data["Returns"] = np.log(AAPL_data["Close"]/AAPL_data["Close"].shift(1))
AAPL_returns = AAPL_data["Returns"].dropna()

AAPL_mu_daily = AAPL_returns.mean()
AAPL_sigma_daily = AAPL_returns.std()
AAPL_mu = AAPL_mu_daily * 252
AAPL_sigma = AAPL_sigma_daily * np.sqrt(252)



TSLA_data["Returns"] = np.log(TSLA_data["Close"]/TSLA_data["Close"].shift(1))
TSLA_returns = TSLA_data["Returns"].dropna()      

TSLA_mu = TSLA_returns.mean() * 252
TSLA_sigma = TSLA_returns.std() * np.sqrt(252)
