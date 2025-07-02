from fetch_data import get_stock_candles
from news import get_news_headlines
from sentiment import get_sentiment_score

from datetime import datetime, timedelta

TOP_50 = [
    "AAPL", "MSFT", "AMZN", "GOOGL", "META", "NVDA", "TSLA", "BRK-B", "JPM", "JNJ",
    "V", "UNH", "HD", "MA", "PG", "PFE", "DIS", "BAC", "XOM", "VZ",
    "CVX", "KO", "ADBE", "PEP", "NFLX", "ABT", "MRK", "INTC", "T", "WMT",
    "CSCO", "CRM", "NKE", "ORCL", "TMO", "QCOM", "MCD", "LLY", "ACN", "TXN",
    "COST", "HON", "MDT", "AVGO", "NEE", "PM", "LIN", "UNP", "BA", "UPS"
]

def get_price_trend(symbol, days=7):
    end = datetime.now().date()
    start = end - timedelta(days=days)
    data = get_stock_candles(symbol, start, end)

    if len(data) < 2:
        return 0.0

    start_price = data.iloc[0]["close"]
    end_price = data.iloc[-1]["close"]

    change = (end_price - start_price) / start_price
    return round(change * 100, 2)  # percent change

def classify_action(sentiment, trend):
    if sentiment >= 2 and trend >= 2:
        return "BUY"
    elif sentiment <= -2 and trend <= -2:
        return "SELL"
    else:
        return "HOLD"

def analyze_top_50():
    results = []

    for symbol in TOP_50:
        try:
            headlines = get_news_headlines(symbol)
            sentiment = get_sentiment_score(headlines)
            trend = get_price_trend(symbol)
            action = classify_action(sentiment, trend)

            results.append({
                "symbol": symbol,
                "sentiment": sentiment,
                "trend (%)": trend,
                "action": action
            })

            print(f"{symbol}: Sentiment={sentiment}, Trend={trend}%, Action={action}")

        except Exception as e:
            print(f"❌ Error with {symbol}: {e}")

    return results

if __name__ == "__main__":
    analyze_top_50()
