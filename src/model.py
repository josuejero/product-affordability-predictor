import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def predict_affordability(data):
    try:
        data['Predicted Affordability'] = data['Balance'] * 0.5
        logger.info("Predicted affordability successfully calculated.")
        return data[['Date', 'Predicted Affordability']]
    except Exception as e:
        logger.error(f"Error in prediction: {e}")
        return None
