import logging
import os
import datetime
from datetime import datetime

class LogGen:
    
   
    @staticmethod
    def loggen():
# Make sure the Logs folder exists in your project root
        os.makedirs("./logs", exist_ok=True)
        logger = logging.getLogger("automationLogger")
# Avoid adding multiple handlers if loggen() is called multiple times
        if not logger.handlers:
            logger.setLevel(logging.INFO)
# Create a file handler for logging
            file_handler = logging.FileHandler(f"./logs/automation_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log")
            formatter = logging.Formatter(
                fmt="%(asctime)s - %(levelname)s - %(message)s",
                datefmt="%m/%d/%Y %I:%M:%S %p"
            )
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
        return logger