import logging

# Setup basic logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def log_message(message):
    """Log messages for debugging."""
    logging.info(message)
