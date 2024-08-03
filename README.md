#  MetricGuard

## Overview

This project is a Linux monitoring system built using FastAPI and psutil. It provides detailed metrics about the system's CPU, memory, disk usage, network, uptime, and logged-in users through a RESTful API.

## Features

- Retrieve CPU information including count, stats, usage percentage, times, frequency, load average, interrupts, and cache info.
- Get detailed memory usage information including virtual memory and swap memory.
- Access detailed disk usage information.
- Fetch detailed network usage information including IO counters, connections, interface addresses, and stats.
- Get system uptime in a human-readable format.
- List logged-in users.


## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/alilotfi23/linux-monitoring-system.git
    cd MetricGuard
    ```

2. Create a virtual environment and activate it:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Running the Application

1. Start the FastAPI application using `uvicorn`:
    ```sh
    uvicorn main:app --reload
    ```

2. Open your browser and navigate to `http://127.0.0.1:8000` to see the welcome message.

3. To access the metrics, go to `http://127.0.0.1:8000/metrics`.

## Configuration

You can set the logging level using environment variables. For example, in a Unix-like environment, you can set the logging level to DEBUG when running the server:

```sh
export LOGGING_LEVEL=DEBUG
uvicorn main:app --reload
```

## Usage

- **GET /**: Returns a welcome message.
- **GET /metrics**: Returns all system metrics.

## Metrics Details

### CPU Information
- `count`: Number of CPU cores.
- `stats`: CPU statistics.
- `percent`: CPU usage percentage.
- `times`: CPU times.
- `freq`: CPU frequency.
- `load_avg`: Load average.
- `interrupts`: Number of interrupts.
- `cache_info`: Cache information.

### Memory Information
- `virtual_memory`: Virtual memory details (total, available, percent, used, free, active, inactive, buffers, cached, shared).
- `swap_memory`: Swap memory details (total, used, free, percent, sin, sout).

### Disk Information
- `device`: Device name.
- `fstype`: File system type.
- `total`: Total disk space.
- `used`: Used disk space.
- `free`: Free disk space.
- `percent`: Disk usage percentage.
- `read_count`: Read count.
- `write_count`: Write count.
- `read_bytes`: Bytes read.
- `write_bytes`: Bytes written.
- `busy_time`: Busy time.

### Network Information
- `io_counters`: Network I/O counters.
- `connections`: Network connections.
- `if_addrs`: Network interface addresses.
- `if_stats`: Network interface stats.

### System Uptime
- `days`: Days since last boot.
- `hours`: Hours since last boot.
- `minutes`: Minutes since last boot.
- `seconds`: Seconds since last boot.

### Users
- `username`: Username of the logged-in user.
- `terminal`: Terminal.
- `host`: Host.
- `started`: Start time.


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please create a pull request with your changes or open an issue to discuss what you would like to improve.
