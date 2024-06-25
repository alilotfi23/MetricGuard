import psutil
import logging
from typing import Optional, Dict

logger = logging.getLogger(__name__)


def get_cpu_info() -> Dict[str, Optional[dict]]:
    """Get detailed CPU information."""
    try:
        return {
            "count": psutil.cpu_count(),
            "stats": psutil.cpu_stats()._asdict(),
            "percent": psutil.cpu_percent(interval=1),
            "times": psutil.cpu_times()._asdict(),
            "freq": psutil.cpu_freq()._asdict() if psutil.cpu_freq() else None,
            "load_avg": psutil.getloadavg(),
            "interrupts": psutil.cpu_stats().interrupts,
            "cache_info": psutil.cpu_stats()
        }
    except Exception as e:
        logger.error(f"Error collecting CPU info: {e}")
        return {}
