from utils import status_file, configuration, dynamic_importer
import logging


logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)


CONNECTED = "CONNECTED"
DISCONNECTED = "DISCONNECTED"


def main():
    config = configuration.get_config()
    away_controller_config = config["away_controller"]
    controller = get_away_controller(away_controller_config)
    connected_devices = controller.get_connected_devices()
    devices_to_control = away_controller_config["devices_to_control"]

    current_status = {x: "CONNECTED" for x in connected_devices if x.lower() in devices_to_control}
    current_status.update({x: "DISCONNECTED" for x in devices_to_control if x not in current_status})
    previous_status = status_file.get_devices_previous_status()

    changes_detected = any(x for x in current_status if current_status[x] != previous_status.get(x, None))

    if changes_detected:
        status_summary = list(current_status.values())
        if len(status_summary) == 1:
            devices_managers = get_devices_managers(config["devices_managers"])
            if status_summary[0] == CONNECTED:
                logging.info("Detected at home")
                for manager in devices_managers:
                    manager.execute_at_home()
            else:
                logging.info("Detect away from home")
                for manager in devices_managers:
                    manager.execute_home_away()

        status_file.write_status(current_status)
    else:
        logging.info("No changes detected so no actions taken")


def get_devices_managers(device_managers_config):
    devices_managers = []
    for item in device_managers_config:
        manager_cls = dynamic_importer.import_class("devices_managers", item["class"])
        devices_managers.append(manager_cls(**item["config"]))

    return devices_managers


def get_away_controller(away_controller_config):
    controller_cls = dynamic_importer.import_class("away_controllers", away_controller_config["class"])
    return controller_cls(**away_controller_config["config"])


if __name__ == '__main__':
    main()
