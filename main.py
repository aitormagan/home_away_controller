import logging
from utils import status_file, configuration, dynamic_importer


logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)


AWAY = "AWAY"
AT_HOME = "AT_HOME"


def main():
    config = configuration.get_config()
    away_controller_config = config["away_controller"]
    controller = get_away_controller(away_controller_config)
    connected_devices = controller.get_connected_devices()
    devices_to_control = away_controller_config["devices_to_control"]

    devices_connected = map(lambda x: x.lower() in connected_devices, devices_to_control)
    current_status = AT_HOME if any(devices_connected) else AWAY
    previous_status = status_file.get_devices_previous_status()

    if current_status != previous_status:
        devices_managers = get_devices_managers(config["devices_managers"])
        if current_status == AWAY:
            logging.info("Detected away from home")
            for manager in devices_managers:
                manager.execute_home_away()
        else:
            logging.info("Detected at home")
            for manager in devices_managers:
                manager.execute_at_home()

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
