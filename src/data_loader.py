import os
import psycopg2
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def check_env_vars():
    required_vars = ['DB_NAME', 'DB_USER', 'DB_PASSWORD', 'DB_HOST', 'DB_PORT']
    missing_vars = [var for var in required_vars if not os.getenv(var)]
    if missing_vars:
        raise EnvironmentError(f"Missing required environment variables: {', '.join(missing_vars)}")

def connect_to_db():
    check_env_vars()
    try:
        connection = psycopg2.connect(
            database=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            host=os.getenv('DB_HOST', 'localhost'),
            port=os.getenv('DB_PORT', '5432')
        )
        logger.info("Successfully connected to the PostgreSQL database.")
        return connection
    except psycopg2.Error as e:
        logger.error(f"Error connecting to the PostgreSQL database: {e}")
        raise

def load_data_from_db():
    conn = connect_to_db()
    cursor = conn.cursor()
    
    try:
        query = "SELECT * FROM cashflow;"
        cursor.execute(query)
        data = cursor.fetchall()
        if not data:
            logger.warning("No data fetched from the database.")
        logger.info("Data successfully loaded from the database.")
    except psycopg2.Error as e:
        logger.error(f"Error fetching data from the database: {e}")
        raise
    finally:
        cursor.close()
        conn.close()
    
    return data

def load_data(filepath=None):
    if filepath:
        logger.info(f"Loading data from {filepath}")
        return pd.read_csv(filepath)
    else:
        logger.info("Loading data from PostgreSQL database")
        return load_data_from_db()
