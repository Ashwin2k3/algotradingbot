# Python Trading Bot

This is a Python trading bot script that uses NSEpy, Selenium, TradingView TA, and other libraries to automate trading decisions based on technical indicators.

## Prerequisites

1. Python 3.x installed
2. Install required Python packages by running the following command:

Reference Document - 

1. chromedriver - https://sites.google.com/a/chromium.org/chromedriver/getting-started
2. Tradingview sample code - https://python-tradingview-ta.readthedocs.io/en/latest/overview.html

## Getting Started

1. Clone or download the repository.
2. Open the terminal and navigate to the project directory.

## Usage

1. Run the script using the following command:


2. The script will prompt you to enter the details of the stock/crypto/forex you want to trade, screener, exchange, and the closing time of your trades.

3. It will then open the TradingView website, login, and search for the specified instrument.

4. The bot will analyze the technical indicators (RSI, EMA, and MACD) using the TradingView TA library and make trading decisions.

5. The bot will execute buy/sell orders based on the trading signals it receives.

6. The bot will continue to analyze the market and make trading decisions until the closing time you specified.


# Python Trading Bot with RSI, EMA, and MACD Strategy

This is a Python trading bot script that implements a simple trading strategy based on the Relative Strength Index (RSI), Exponential Moving Average (EMA), and Moving Average Convergence Divergence (MACD) indicators.

## Strategy Overview

The trading strategy implemented in this bot is a trend-following strategy that aims to identify potential buying and selling opportunities based on the RSI, EMA, and MACD signals.

1. **RSI (Relative Strength Index)**:
   - The bot uses the RSI indicator to determine whether an instrument is overbought (RSI > 70) or oversold (RSI < 30).
   - An RSI value above 70 suggests that the instrument is overbought, indicating a potential sell signal.
   - An RSI value below 30 suggests that the instrument is oversold, indicating a potential buy signal.

2. **EMA (Exponential Moving Average)**:
   - The bot uses the EMA indicator to determine the trend direction.
   - When the EMA value is rising, it suggests an uptrend, indicating a potential buy signal.
   - When the EMA value is falling, it suggests a downtrend, indicating a potential sell signal.

3. **MACD (Moving Average Convergence Divergence)**:
   - The bot uses the MACD indicator to further confirm the trend direction.
   - A positive MACD value suggests a bullish trend, indicating a potential buy signal.
   - A negative MACD value suggests a bearish trend, indicating a potential sell signal.

## How the Bot Works

1. The user is prompted to enter the details of the instrument they want to trade (stock/crypto/forex), the screener, the exchange, and the closing time for trades.

2. The bot then opens the TradingView website using Selenium, logs in, and searches for the specified instrument.

3. The bot fetches the technical indicator values (RSI, EMA, and MACD) using the TradingView TA library.

4. Based on the RSI, EMA, and MACD signals, the bot makes trading decisions:
   - If the RSI is in the 30 to 70 range and the EMA indicates a "BUY" signal, the bot considers a potential buy opportunity.
   - If the RSI is above 70 or the EMA indicates a "SELL" signal, the bot considers a potential sell opportunity.

5. The bot executes buy/sell orders on the TradingView website if the trading conditions are met.

6. The bot continues to analyze the market and execute trades until the specified closing time.

## Disclaimer

This trading bot is for educational purposes only and does not guarantee profits. Use it at your own risk.

## License

[MIT License](LICENSE)

