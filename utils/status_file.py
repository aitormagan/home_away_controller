STATUS_FILE = "status_file.txt"
SEPARATOR = "|"


def get_devices_previous_status():
    devices_last_status = {}
    try:
        with open(STATUS_FILE, "r") as f:
            for line in f:
                line_parts = line.split(SEPARATOR)
                devices_last_status[line_parts[0]] = line_parts[1]
    except FileNotFoundError:
        pass

    return devices_last_status


def write_status(current_status):
    with open(STATUS_FILE, "w") as f:
        for mac in current_status:
            f.write(f"{mac}{SEPARATOR}{current_status[mac]}")
