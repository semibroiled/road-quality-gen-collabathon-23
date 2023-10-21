"""This module will save our Dictionary Data in some other format"""

import json, csv
from typing import Dict, List
from datetime import datetime

# Set datetime to name files
cur_time = datetime.now().strftime("%Y%m%d%S")


def flatten_dict(data: Dict) -> Dict:
    """_summary_

    Args:
        data (Dict): _description_

    Returns:
        Dict: _description_
    """
    flattened_data = []
    for key, value in data.items():
        flattened_entry = {
            "ID": key,
            "filename": value["filename"],
            "Location": value["Latitude and Longitude"],
            "Datetime": value["Datetime"],
            "Camera Make": value["Camera Make"],
            "Camera Model": value["Camera Model"],
            "Firmware": value["Firmware"],
            "DPI": value["DPI"],
        }
        flattened_data.append(flattened_entry)


def save_as_json(data: Dict) -> None:
    """_summary_

    Args:
        data (Dict): _description_
    """
    # Convert data to JSON string
    json_data = json.dumps(data, indent=4)
    # TODO: Add logger!
    # Save JSON String to a file
    with open(f"./data/{cur_time}.json", "w") as json_file:
        json_file.write(json_data)


def save_as_csv(data: Dict, fieldnames: List[str]) -> None:
    """_summary_

    Args:
        data (Dict): _description_
    """
    # Get Field names
    # TODO
    #! ADD LOGGER!!!!
    # TODO: Flatten data

    # Save as CSV
    with open(f"{cur_time}.csv", "w", newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
