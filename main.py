from diagnostics import check_disk_usage, check_cpu_memory, check_network
from logger import log_message
from notifier import send_notification

def run_diagnostics():
    print("Running diagnostics...")

    # Disk usage
    disk_message = check_disk_usage()
    log_message(disk_message)
    print(disk_message)

    # CPU and memory usage
    cpu_memory_messages = check_cpu_memory()
    for message in cpu_memory_messages:
        log_message(message)
        print(message)

    # Network connectivity
    network_message = check_network()
    log_message(network_message)
    print(network_message)

    # Notification for warnings
    warnings = [disk_message] + cpu_memory_messages + [network_message]
    for warning in warnings:
        if "Warning" in warning:
            send_notification("System Diagnostics Alert", warning)

if __name__ == "__main__":
    run_diagnostics()
