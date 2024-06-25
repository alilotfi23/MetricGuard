import psutil
import logging
from utils import bytes_to_gb
from typing import Dict

logger = logging.getLogger(__name__)


def get_memory_info() -> Dict[str, dict]:
    """Get detailed memory usage information."""
    try:
        memory_info = psutil.virtual_memory()
        swap_info = psutil.swap_memory()
        return {
            "virtual_memory": {
                "total": bytes_to_gb(memory_info.total),
                "available": bytes_to_gb(memory_info.available),
                "percent": memory_info.percent,
                "used": bytes_to_gb(memory_info.used),
                "free": bytes_to_gb(memory_info.free),
                "active": memory_info.active,
                "inactive": memory_info.inactive,
                "buffers": memory_info.buffers,
                "cached": memory_info.cached,
                "shared": memory_info.shared
            },
            "swap_memory": {
                "total": bytes_to_gb(swap_info.total),
                "used": bytes_to_gb(swap_info.used),
                "free": bytes_to_gb(swap_info.free),
                "percent": swap_info.percent,
                "sin": bytes_to_gb(swap_info.sin),
                "sout": bytes_to_gb(swap_info.sout)
            }
        }
    except Exception as e:
        logger.error(f"Error collecting memory info: {e}")
        return {}
