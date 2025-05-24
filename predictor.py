import finnhub
import os
from dotenv import load_dotenv

load_dotenv() #loading the secret API file
API_KEY = os.getenv("API_KEY") #Set API_KEY = to your api key
finnhub_client = finnhub.Client(api_key=API_KEY)