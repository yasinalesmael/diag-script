import psutil
import socket

def check_disk_usage(threshold=80):
    usage = psutil.disk_usage('/')
    percent_used = usage.percent
    if percent_used > threshold:
        return f"Warning: Disk usage is {percent_used}%!"
    return f"Disk usage is {percent_used}%."

def check_cpu_memory(threshold=80):
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    alerts = []
    if cpu > threshold:
        alerts.append(f"Warning: CPU usage is {cpu}%!")
    if memory > threshold:
        alerts.append(f"Warning: Memory usage is {memory}%!")
    return alerts if alerts else [f"CPU: {cpu}%, Memory: {memory}%."]

def check_network(host="8.8.8.8", port=53, timeout=3):
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return "Network connectivity is fine."
    except socket.error as ex:
        return f"Warning: Network connectivity issue! {ex}"
