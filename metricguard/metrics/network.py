import psutil
import logging
from typing import Dict, Any

logger = logging.getLogger(__name__)


def get_network_info() -> Dict[str, Any]:
    """Get detailed network usage information."""
    try:
        net_io = psutil.net_io_counters()._asdict()
        net_connections = [conn._asdict() for conn in psutil.net_connections()]
        net_if_addrs = {k: [addr._asdict() for addr in v] for k, v in psutil.net_if_addrs().items()}
        return {
            "io_counters": net_io,
            "connections": net_connections,
            "if_addrs": net_if_addrs,
            "if_stats": {k: v._asdict() for k, v in psutil.net_if_stats().items()}
        }
    except Exception as e:
        logger.error(f"Error collecting network info: {e}")
        return {}
