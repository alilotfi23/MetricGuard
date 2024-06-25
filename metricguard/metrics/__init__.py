from .cpu import get_cpu_info
from .memory import get_memory_info
from .disk import get_disk_info
from .network import get_network_info
from .system import get_uptime, get_users
import logging

logger = logging.getLogger(__name__)


def get_all_metrics() -> dict:
    """Collect all system metrics."""
    try:
        return {
            "cpu_info": get_cpu_info(),
            "memory_info": get_memory_info(),
            "disk_info": get_disk_info(),
            "network_info": get_network_info(),
            "uptime": get_uptime(),
            "users": get_users(),
        }
    except Exception as e:
        logger.error(f"Error collecting all metrics: {e}")
        raise
