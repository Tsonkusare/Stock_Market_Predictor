import os
import requests
from dotenv import load_dotenv
from news import get_news_headlines
from sentiment import get_sentiment_score

load_dotenv()
FINNHUB_API_KEY = os.getenv("FINNHUB_API_KEY")

def get_price_score(symbol):
    url = f"https://finnhub.io/api/v1/quote?symbol={symbol}&token={FINNHUB_API_KEY}"
    r = requests.get(url).json()

    try:
        current = r['c']
        previous = r['pc']
        change = (current - previous) / previous

        if change > 0.05:
            return 3
        elif change > 0.01:
            return 2
        elif change > -0.01:
            return 0
        elif change > -0.05:
            return -2
        else:
            return -3
    except:
        return 0

def get_company_score(symbol):
    headlines = get_news_headlines(symbol)
    sentiment = get_sentiment_score(headlines)
    price = get_price_score(symbol)
    total = sentiment + price
    return max(min(total, 10), -10)

