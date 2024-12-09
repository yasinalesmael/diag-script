# Automated System Diagnostics Script
A Python script to perform basic system diagnostics such as checking disk usage, CPU/memory usage, and network connectivity.

## Features
- Checks:
  - Disk usage.
  - CPU and memory usage.
  - Network connectivity.
- Logs results to a file.
- Sends desktop notifications for warnings.

## Requirements
- Python 3.x
- Libraries: psutil, plyer

## Installation
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the script:
   ```bash
   python main.py
   ```

## Usage
- Customize thresholds in `diagnostics.py` (e.g., disk usage warning level).
- Logs are stored in `diagnostics.log`.

## License
This project is licensed under the MIT License.
