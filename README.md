# 📈 Market Forecasting & Regime Detection – NIFTY 50 Intelligence Dashboard  
### Time-Series Analysis, Market Regimes & Decision Support

An end-to-end **market forecasting and intelligence project** built on Indian equity market data (NIFTY 50 constituents), combining **time-series modeling**, **technical analysis**, and **interactive visualization** to support data-driven market insights rather than single-model predictions.

This project is designed to reflect how **real market analytics systems** are built: exploratory analysis in notebooks, followed by a **production-style Streamlit dashboard** for consumption by analysts and decision-makers.

---

## 🚩 Problem
Market participants often rely on:
- Single-indicator signals  
- Static trend assumptions  
- One-model forecasts without uncertainty awareness  

However, equity markets exhibit:
- Regime shifts (bull / bear cycles)  
- Volatility clustering  
- Structural breaks across time  

A single method rarely performs well across all market conditions.

**This project addresses that gap by building a multi-layered market intelligence framework that separates analysis, modeling, and presentation.**

---

## 🎯 Objectives
- Analyze long-term price behavior of NIFTY 50 stocks  
- Detect market regimes using trend-based indicators  
- Explore short-term forecasting techniques (ARIMA)  
- Model volatility behavior conceptually (GARCH framework)  
- Present insights through an interactive dashboard  
- Keep the workflow reproducible and production-oriented  

---

## 📊 Data
- **Dataset:** `NIFTY50_all.csv`  
- Historical OHLCV data for NIFTY 50 constituents  
- Time-indexed equity price data  
- Cleaned, column-safe preprocessing  
- Symbol-level filtering from a single master dataset  

All analysis is performed **per stock**, avoiding cross-sectional leakage.

---

## 🧠 Analytical Approach

Rather than committing to a single technique, the project layers multiple analytical perspectives:

### 1️⃣ Exploratory Data Analysis
- Long-term price trends  
- Structural changes across market cycles  
- Visual inspection of volatility behavior  

### 2️⃣ Technical Indicators
- Simple Moving Averages (SMA-50, SMA-200)  
- Trend-based regime identification  
- Rolling statistics for smoothing noise  

### 3️⃣ Market Regime Detection
- Bull / Bear regime classification based on SMA crossovers  
- Regime labeling aligned with market intuition  
- Visual validation through trend overlays  

### 4️⃣ Time-Series Forecasting
- **ARIMA** models for short-horizon forecasting  
- Focus on directional behavior rather than point precision  
- Emphasis on explainability over overfitting  

### 5️⃣ Volatility Modeling (Conceptual)
- GARCH-based volatility intuition  
- Recognition of volatility clustering in equity markets  

---

## 📈 Key Insights
- Market regimes persist for extended periods but shift sharply during stress events  
- Trend-based indicators provide interpretable regime signals  
- Short-term forecasts are sensitive to regime context  
- Volatility behavior is non-constant and regime-dependent  

Insights are intended to **support judgment**, not replace it.

---

## 🖥️ Interactive Dashboard
A **Streamlit dashboard** (`app.py`) allows users to:

- Select any NIFTY 50 stock dynamically  
- View historical price trends  
- Inspect trend-based market regimes  
- Explore indicators interactively  

The dashboard is designed as a **presentation layer**, decoupled from research notebooks.

---

## 📁 Project Structure
