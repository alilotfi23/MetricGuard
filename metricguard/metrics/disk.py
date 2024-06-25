import psutil
import logging
from typing import List, Dict

logger = logging.getLogger(__name__)

def get_disk_info() -> List[Dict[str, object]]:
    """Enhanced disk usage information."""
    try:
        partitions = psutil.disk_partitions(all=True)
        disks = []
        for partition in partitions:
            try:
                usage = psutil.disk_usage(partition.mountpoint)
                disk_info = {
                    "device": partition.device,
                    "fstype": partition.fstype,
                    "total": usage.total,
                    "used": usage.used,
                    "free": usage.free,
                    "percent": usage.percent,
                    "read_count": usage.read_count,
                    "write_count": usage.write_count,
                    "read_bytes": usage.read_bytes,
                    "write_bytes": usage.write_bytes,
                    "busy_time": usage.busy_time
                }
                disks.append(disk_info)
            except Exception as e:
                logger.warning(f"Error getting disk usage for {partition.mountpoint}: {e}")
        return disks
    except Exception as e:
        logger.error(f"Error collecting disk info: {e}")
        return []
