import os
import requests
import json
import logging
from data_loader import load_data
from feature_engineering import preprocess_data
from model import predict_affordability
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def check_oauth_env_vars():
    required_vars = ['CLIENT_ID', 'CLIENT_SECRET']
    missing_vars = [var for var in required_vars if not os.getenv(var)]
    if missing_vars:
        raise EnvironmentError(f"Missing required OAuth environment variables: {', '.join(missing_vars)}")

def get_oauth_token():
    check_oauth_env_vars()

    CLIENT_ID = os.getenv('CLIENT_ID')
    CLIENT_SECRET = os.getenv('CLIENT_SECRET')

    logger.info("Fetching OAuth token...")
    client = BackendApplicationClient(client_id=CLIENT_ID)
    oauth = OAuth2Session(client=client)
    
    try:
        token = oauth.fetch_token(token_url='https://api.oauthprovider.com/token', client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
        logger.info("OAuth token fetched successfully.")
        return token
    except Exception as e:
        logger.error(f"Error fetching OAuth token: {e}")
        raise

def fetch_product_price(product_id, token):
    headers = {
        'Authorization': f"Bearer {token['access_token']}"
    }
    
    logger.info(f"Fetching product price for product ID: {product_id}")
    try:
        response = requests.get(f'https://api.products.com/products/{product_id}/price', headers=headers)
        response.raise_for_status()
        logger.info("Product price fetched successfully.")
        return response.json()['price']
    except requests.exceptions.HTTPError as http_err:
        logger.error(f"HTTP error occurred: {http_err}")
    except Exception as e:
        logger.error(f"An error occurred: {e}")
    return None

def main():
    logger.info("Loading and preprocessing data...")
    data = load_data("data/cashflow.csv")
    processed_data = preprocess_data(data)
    
    logger.info("Predicting affordability...")
    predicted_balances = predict_affordability(processed_data)
    
    if predicted_balances is None:
        logger.error("Predicted balances not available.")
        return
    
    token = get_oauth_token()
    product_id = "12345"
    price = fetch_product_price(product_id, token)
    
    if price is not None:
        logger.info(f"Product Price: {price}")
    else:
        logger.error("Failed to fetch product price.")

if __name__ == "__main__":
    main()
