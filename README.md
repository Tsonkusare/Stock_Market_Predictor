# 📈 Stock Buy/Sell Recommendation App

This is a **Streamlit-based web application** that analyzes the top 50 publicly traded companies in the U.S. to provide **buy/sell investment recommendations** using **news sentiment analysis** and **7-day price trends**. Users can also enter a custom stock ticker to view detailed news sentiment and 1-year historical price data.

---

## 🚀 Features

- 🔍 **Analyze Top 50 Stocks**  
  Automatically evaluates stocks like AAPL, MSFT, TSLA, and more.

- 📰 **News Sentiment Analysis**  
  Fetches the latest headlines and calculates a sentiment score (range: -5 to +5).

- 📈 **Trend-Based Classification**  
  Uses 7-day stock price trends combined with sentiment to classify action as **BUY**, **SELL**, or **HOLD**.

- 🗕️ **1-Year Price Chart**  
  Visualizes historical price trends for any stock symbol.

- 🧠 **Smart Recommendations**  
  Combines real-time data and ML-based classification for actionable insights.

---

## 🛠️ Tech Stack

- [Streamlit](https://streamlit.io/) – UI and app framework  
- `pandas`, `matplotlib` – Data processing and visualization  
- Custom modules:
  - `fetch_data.py` – For retrieving stock price data
  - `news.py` – For gathering news headlines
  - `sentiment.py` – For calculating sentiment scores
  - `batch_predict.py` – For classifying buy/sell actions

---

## 📦 Installation

Follow these steps to set up the project locally:

### 1. Clone the repository

```bash
git clone https://github.com/your-username/stock-recommendation-app.git
cd stock-recommendation-app

### 2. Set up dependencies

Make sure Python 3.8 or later is installed on your machine.

#### Option A: Install directly

```bash
pip install -r requirements.txt

### 3. Set up environment variables

If your project requires API keys or secrets (e.g., for fetching stock data or news), create a `.env` file in the project root directory and define your variables like this:

```env
API_KEY=your_stock_data_api_key
NEWS_API_KEY=your_news_api_key
OTHER_ENV_VAR=value


### 4. Run the Streamlit app

After installing dependencies and setting environment variables, launch the app with:

```bash
streamlit run app.py
