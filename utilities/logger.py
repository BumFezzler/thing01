import logging
import os

# Create a logs directory if it doesn't exist
if not os.path.exists("logs"):
    os.makedirs("logs")

# Set up basic logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("logs/logfile.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger()
