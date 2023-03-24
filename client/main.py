import os
import logging
import json
import requests
from dotenv import load_dotenv

load_dotenv()
logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    request = {"name": "world"}
    response = requests.post("{}/hello".format(os.getenv("API_URL")), data=json.dumps(request))
    results = response.json()
    logger.info(results)
except Exception as e:
    logger.error(e)
