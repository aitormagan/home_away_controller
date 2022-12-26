STATUS_FILE = "status_file.txt"
SEPARATOR = "|"


def get_devices_previous_status():
    previous_status = None
    try:
        with open(STATUS_FILE, "r") as f:
            previous_status = f.read()
    except FileNotFoundError:
        pass

    return previous_status


def write_status(current_status):
    with open(STATUS_FILE, "w") as f:
        f.write(current_status)
