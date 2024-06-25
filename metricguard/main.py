from fastapi import FastAPI, HTTPException
from metrics import get_all_metrics
import logging
import os

app = FastAPI()

# Configure logging
logging_level = os.getenv('LOGGING_LEVEL', 'INFO').upper()
logging.basicConfig(level=logging_level)
logger = logging.getLogger(__name__)


@app.get("/")
def read_root():
    return {"message": "Linux Monitoring System"}


@app.get("/metrics")
def get_metrics():
    try:
        metrics = get_all_metrics()
        logger.info("Metrics collected successfully")
        return metrics
    except Exception as e:
        logger.error(f"Error collecting metrics: {e}")
        raise HTTPException(status_code=500, detail=str(e))
