import json
import os
from pathlib import Path
from logging.config import fileConfig

import logging

os.chdir(Path(__file__).parent)

fileConfig("./logging.ini")

logger = logging.getLogger()

# Application started
logger.info("Application started successfully!")

# Loading Config Data
logger.info("Configuration loading..")

with open("./config.json", mode="r", encoding="UTF-8") as file:
    cfg = json.load(file)

APP_TITLE = cfg["application"]
