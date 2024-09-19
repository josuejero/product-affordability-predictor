import pandas as pd
import logging
from model import predict_affordability
from feature_engineering import preprocess_data

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def analyze_data(data):
    if data.empty:
        logger.error("Input data is empty. Analysis cannot proceed.")
        return

    logger.info("Preprocessing data...")
    processed_data = preprocess_data(data)
    
    if processed_data is None:
        logger.error("Preprocessed data is invalid or missing.")
        return

    logger.info("Predicting affordability...")
    predicted_balances = predict_affordability(processed_data)
    
    if predicted_balances is not None:
        logger.info("Affordability predictions generated successfully.")
        print(predicted_balances.head())
    else:
        logger.error("Error: Could not generate affordability predictions.")
