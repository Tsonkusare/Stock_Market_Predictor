import streamlit as st
from fetch_data import get_stock_candles
from news import get_news_headlines
from sentiment import get_sentiment_score
from batch_predict import classify_action

from datetime import datetime, timedelta
import pandas as pd

TOP_50 = [
    "AAPL", "MSFT", "AMZN", "GOOGL", "META", "NVDA", "TSLA", "BRK-B", "JPM", "JNJ",
    "V", "UNH", "HD", "MA", "PG", "PFE", "DIS", "BAC", "XOM", "VZ",
    "CVX", "KO", "ADBE", "PEP", "NFLX", "ABT", "MRK", "INTC", "T", "WMT",
    "CSCO", "CRM", "NKE", "ORCL", "TMO", "QCOM", "MCD", "LLY", "ACN", "TXN",
    "COST", "HON", "MDT", "AVGO", "NEE", "PM", "LIN", "UNP", "BA", "UPS"
]

st.title("📊 Stock Buy/Sell Recommendation App")

@st.cache_data(show_spinner=False)
def analyze(symbol):
    try:
        headlines = get_news_headlines(symbol)
        sentiment = get_sentiment_score(headlines)

        end = datetime.now().date()
        start = end - timedelta(days=7)
        price_data = get_stock_candles(symbol, start, end)

        if len(price_data) < 2:
            return None

        start_price = price_data.iloc[0]["close"]
        end_price = price_data.iloc[-1]["close"]
        trend = round(((end_price - start_price) / start_price) * 100, 2)

        action = classify_action(sentiment, trend)

        if action in ["BUY", "SELL"]:
            return {
                "Symbol": symbol,
                "Sentiment": sentiment,
                "7d Trend (%)": trend,
                "Action": action
            }
    except:
        return None

st.markdown("### Analyzing Top 50 Companies...")
results = []

with st.spinner("Running analysis..."):
    for symbol in TOP_50:
        result = analyze(symbol)
        if result:
            results.append(result)

if results:
    df = pd.DataFrame(results)
    st.dataframe(df, use_container_width=True)
else:
    st.info("No BUY or SELL recommendations found right now.")
    
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

# Allow user to enter or select a stock symbol
symbol = st.text_input("Enter a stock symbol (e.g. AAPL, TSLA, MSFT):", value="AAPL").upper()

# Get news headlines
with st.spinner("Fetching news headlines..."):
    headlines = get_news_headlines(symbol)
    sentiment_score = get_sentiment_score(headlines)

st.markdown(f"### 📰 News Sentiment for {symbol}")
st.write(f"**Sentiment Score:** {sentiment_score} (range: -5 to +5)")

# Show headlines
if headlines:
    st.markdown("#### Latest Headlines")
    for headline in headlines[:10]:
        st.markdown(f"- {headline}")
else:
    st.info("No recent news found.")

# Get 1-year price data
with st.spinner("Fetching 1-year price history..."):
    today = datetime.now().date()
    one_year_ago = today - timedelta(days=365)

    try:
        df = get_stock_candles(symbol, start_date=one_year_ago, end_date=today)
        if not df.empty:
            st.markdown("### 📊 1-Year Price Trend")
            fig, ax = plt.subplots(figsize=(10, 4))
            ax.plot(df["date"], df["close"], label="Close Price")
            ax.set_xlabel("Date")
            ax.set_ylabel("Price ($)")
            ax.set_title(f"{symbol} - 1 Year Trend")
            ax.grid(True)
            st.pyplot(fig)
        else:
            st.warning("No price data found for this symbol.")
    except Exception as e:
        st.error(f"Error fetching data: {e}")

