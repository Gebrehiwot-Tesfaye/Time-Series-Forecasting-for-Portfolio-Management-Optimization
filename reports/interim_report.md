# Interim Report: Time Series Forecasting for Portfolio Management Optimization

## 1. Introduction

Guide Me in Finance (GMF) Investments is a forward-thinking financial advisory firm that leverages data-driven insights and advanced analytics to deliver personalized portfolio management. In today’s volatile financial markets, the ability to forecast asset price movements and optimize portfolios is crucial for maximizing returns and managing risk. This project aims to apply both classical and deep learning time series models to historical financial data, providing actionable insights for portfolio optimization.

---

## 2. Business Objective

The primary objective is to use time series forecasting to enhance portfolio management strategies for GMF clients. By analyzing historical data for TSLA (Tesla), BND (Vanguard Total Bond Market ETF), and SPY (S&P 500 ETF), we seek to:

- Predict future price trends and volatility,
- Quantify and manage risk,
- Optimize asset allocation using Modern Portfolio Theory (MPT),
- Backtest and validate the performance of model-driven investment strategies.

---

## 3. Data Analysis and Preparation

### 3.1 Data Sources and Extraction

- **Assets:** TSLA, BND, SPY
- **Source:** Yahoo Finance (via yfinance API)
- **Period:** July 1, 2015 – July 31, 2025
- **Features:** Date, Open, High, Low, Close, Adj Close, Volume

Data was programmatically downloaded using the `fetch_data.py` script, ensuring reproducibility and up-to-date information. Raw CSV files are stored in `data/raw/`.

### 3.2 Data Cleaning

- **Date Handling:** All date columns were parsed and standardized to datetime format.
- **Missing Values:** Forward and backward fill methods were used to address missing data, preserving the time series structure.
- **Data Types:** All price and volume columns were converted to numeric types to prevent calculation errors.

### 3.3 Feature Engineering

- **Returns:** Daily percentage returns and log returns were calculated for each asset.
- **Volatility:** 21-day rolling standard deviation was computed to capture short-term risk.
- **Rolling Statistics:** Rolling mean and rolling standard deviation were added for trend and volatility analysis.
- **Outlier Detection:** Z-scores were calculated for daily returns to identify extreme market events.
- **Stationarity Preparation:** Differencing and transformation steps were considered for modeling.

Processed datasets are saved in `data/processed/` for use in modeling and analysis.

---

## 4. Exploratory Data Analysis (EDA) Insights

### 4.1 Price and Trend Analysis

- **TSLA:** Demonstrates rapid growth and high volatility, especially post-2019. Notable price surges and drawdowns are visible, reflecting both company-specific and market-wide events.
- **BND:** Exhibits stable, low-volatility price movement, consistent with its role as a bond ETF.
- **SPY:** Tracks the S&P 500 index, showing broad market trends and moderate volatility.

### 4.2 Returns and Volatility

- **Daily Returns:** TSLA has the highest mean and standard deviation of returns, indicating both high risk and high potential reward. BND’s returns are the most stable.
- **Rolling Volatility:** The 21-day rolling standard deviation highlights periods of market stress, such as the COVID-19 crash in 2020, with TSLA experiencing the most pronounced spikes.
- **Outlier Detection:** Z-score analysis reveals frequent extreme returns for TSLA, while BND rarely exhibits outliers.

### 4.3 Stationarity and Statistical Properties

- **ADF Test on Prices:** All assets’ price series are non-stationary, as expected for financial time series.
- **ADF Test on Returns:** Returns are stationary, validating their use in ARIMA and LSTM modeling.
- **Distribution:** Return distributions are non-normal, with fat tails and skewness, especially for TSLA.

### 4.4 Risk Metrics

- **Value at Risk (VaR 95%):** Quantifies the worst expected daily loss at the 5th percentile. TSLA’s VaR is much larger in magnitude than BND or SPY, reflecting its risk profile.
- **Sharpe Ratio:** TSLA offers higher risk-adjusted returns but with much greater volatility. BND provides stability and lower risk, while SPY offers a balanced profile.

### 4.5 Visual Presentation

- **Line Plots:** Used for adjusted close prices, daily returns, and rolling volatility to visualize trends and risk.
- **Histograms:** Show the distribution of returns and highlight the presence of outliers.
- **Summary Tables:** Present descriptive statistics and risk metrics for each asset.

---

## 5. Professional Communication and Visual Presentation

- **Code Quality:** All scripts and notebooks are modular, well-commented, and follow best practices for readability and reproducibility.
- **Visualization:** Consistent color schemes, clear axis labels, and legends are used throughout for effective communication.
- **Documentation:** This report and the project README provide clear, step-by-step guidance for users and reviewers.
- **Reproducibility:** All data processing and analysis steps are automated and documented, enabling easy replication of results.

---

## 6. Key Insights and Takeaways

- TSLA is a high-growth, high-risk asset, suitable for aggressive portfolios.
- BND offers stability and acts as a risk mitigator in diversified portfolios.
- SPY provides broad market exposure and moderate risk.
- The combination of these assets allows for a range of portfolio strategies, from conservative to aggressive.
- Proper preprocessing and EDA are crucial for robust modeling and risk management.

---

## 7. Next Steps

1. **Modeling:** Build and tune ARIMA/SARIMA and LSTM models for TSLA price forecasting.
2. **Forecasting Analysis:** Compare model performance and interpret forecast results, including confidence intervals and risk implications.
3. **Portfolio Optimization:** Use forecasted and historical returns to construct the efficient frontier and recommend optimal asset allocations using Modern Portfolio Theory.
4. **Backtesting:** Simulate the performance of the recommended portfolio and compare it to a benchmark (e.g., 60% SPY / 40% BND).

---

**Prepared by:**  
Gebrehiwot Tesfaye  
August 2025
