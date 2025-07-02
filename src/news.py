import os
import requests
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()
FINNHUB_API_KEY = os.getenv("FINNHUB_API_KEY")

def get_news_headlines(symbol, days_back=10):
    url = "https://finnhub.io/api/v1/company-news"
    start = (datetime.now() - timedelta(days=days_back)).strftime('%Y-%m-%d')
    end = datetime.now().strftime('%Y-%m-%d')

    params = {
        'symbol': symbol,
        'from': start,
        'to': end,
        'token': FINNHUB_API_KEY
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        return [article["headline"] for article in response.json()]
    return []
