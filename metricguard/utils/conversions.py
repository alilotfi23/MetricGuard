def bytes_to_gb(bytes_value: int) -> float:
    """Convert bytes to gigabytes."""
    return round(bytes_value / (1024 ** 3), 2)
