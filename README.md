# Stock_Market_Predictor
📈 Stock Buy/Sell Recommendation App
This is a Streamlit-based web application that analyzes the top 50 publicly traded companies in the U.S. to provide buy/sell investment recommendations using news sentiment analysis and 7-day price trends. Users can also enter a custom stock ticker to view detailed news sentiment and 1-year historical price data.

🚀 Features
🔍 Analyze Top 50 Stocks
Automatically evaluates stocks like AAPL, MSFT, TSLA, and more.

📰 News Sentiment Analysis
Fetches the latest headlines and calculates a sentiment score (range: -5 to +5).

📊 Trend-Based Classification
Uses 7-day stock price trends combined with sentiment to classify action as BUY, SELL, or HOLD.

📅 1-Year Price Chart
Visualizes historical price trends for any stock symbol.

🧠 Smart Recommendations
Combines real-time data and ML-based classification for actionable insights.

🛠️ Tech Stack
Streamlit – UI and app framework

pandas, matplotlib – Data processing and visualization

Custom modules:

fetch_data.py – For retrieving stock price data

news.py – For gathering news headlines

sentiment.py – For calculating sentiment scores

batch_predict.py – For classifying buy/sell actions

📥 Installation
Clone the repository

bash
Copy
Edit
git clone https://github.com/your-username/stock-recommendation-app.git
cd stock-recommendation-app
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Run the app

bash
Copy
Edit
streamlit run app.py
🖥️ Usage
On launch, the app automatically analyzes the top 50 stocks.

You can manually enter a stock symbol (e.g., AAPL) to:

View sentiment score from latest news

Read latest headlines

Visualize 1-year price trend

📷 Screenshots
Top 50 Summary	Custom Symbol View
