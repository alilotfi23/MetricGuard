import psutil
import time
import logging
from typing import Dict, Optional

logger = logging.getLogger(__name__)


def get_uptime() -> Optional[Dict[str, int]]:
    """Get system uptime in a human-readable format."""
    try:
        boot_time = psutil.boot_time()
        uptime_seconds = time.time() - boot_time
        days, remainder = divmod(uptime_seconds, 86400)
        hours, remainder = divmod(remainder, 3600)
        minutes, seconds = divmod(remainder, 60)
        return {
            "days": int(days),
            "hours": int(hours),
            "minutes": int(minutes),
            "seconds": int(seconds)
        }
    except Exception as e:
        logger.error(f"Error getting system uptime: {e}")
        return None


def get_users() -> Optional[list]:
    """Get logged-in users."""
    try:
        users = psutil.users()
        return [user._asdict() for user in users]
    except Exception as e:
        logger.error(f"Error getting users: {e}")
        return None
