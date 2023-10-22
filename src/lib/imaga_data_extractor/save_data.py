"""This module will save our Dictionary Data in some other format"""

import json, csv
from typing import Dict, List
from datetime import datetime
import os

# Set datetime to name files
cur_time = datetime.now().strftime("%Y%m%d%H%M%S")


def flatten_dict(data: Dict) -> Dict:
    """_summary_

    Args:
        data (Dict): _description_

    Returns:
        Dict: _description_
    """
    flattened_data = []
    for key, value in data.items():
        # print(value)
        # print(value["filename"])
        # print(type(value["Datetime"]))
        # print(type(value["Camera Make"]))
        # print(type(value["Firmware"]))
        # print(type(value["Camera Model"]))
        # print(type(float(value["DPI"])))
        # print(type(value["Latitude and Longtitude"]))
        try:
            try:
                if value["Latitude and Longtitude"]:
                    loc_dict = value["Latitude and Longtitude"]
                    location = f"{loc_dict[1]} {loc_dict[2]} {loc_dict[3]} {loc_dict[4]} {loc_dict[6]} {loc_dict[12]} {loc_dict[13]} {loc_dict[17]} {loc_dict[23]} {loc_dict[24]} {loc_dict[29]}"
                    # print(f"Entry has valuable GPS Data")
                    flattened_entry = {
                        "ID": key,
                        "filename": value["filename"],
                        "Location": location,
                        "Datetime": value["Datetime"],
                        "Camera Make": value["Camera Make"],
                        "Camera Model": value["Camera Model"],
                        "Firmware": value["Firmware"],
                        "DPI": float(value["DPI"]),
                    }
            except:
                # print(f"No GPS Data")
                # try:
                #     print(value["Latitude and Longtitude"])
                #     #! Watchout for spelling
                # except:
                #     print("No GPS frfr")
                flattened_entry = {
                    "ID": key,
                    "filename": value["filename"],
                    "Location": None,
                    "Datetime": value["Datetime"],
                    "Camera Make": value["Camera Make"],
                    "Camera Model": value["Camera Model"],
                    "Firmware": value["Firmware"],
                    "DPI": float(value["DPI"]),
                }
        except:
            # print(f"Error Occured with Entries. No Data.")
            flattened_entry = {
                "ID": key,
                "filename": None,
                "Location": None,
                "Datetime": None,
                "Camera Make": None,
                "Camera Model": None,
                "Firmware": None,
                "DPI": None,
            }

        flattened_data.append(flattened_entry)
    return flattened_data


def save_as_json(data: Dict) -> None:
    """_summary_

    Args:
        data (Dict): _description_
    """
    # Flatten data
    print(f"Flattening Dictionary...")
    data = flatten_dict(data)

    # Convert data to JSON string
    print(f"Jsonifying...")
    json_data = json.dumps(data, indent=4)
    # TODO: Add logger!
    # Check if save path exists
    if not os.path.exists("./src/data"):
        print(f"Creating Save Path...")
        os.makedirs("./src/data")
    # Save JSON String to a file
    with open(f"./src/data/{cur_time}.json", "w") as json_file:
        json_file.write(json_data)


def save_as_csv(data: Dict) -> None:
    """_summary_

    Args:
        data (Dict): _description_
    """

    #! ADD LOGGER!!!!
    # TODO: Flatten data

    # Flatten Data
    print(f"Flattening Dictionary...")
    data = flatten_dict(data)

    # Get Field Names
    print(f"Getting field names...")
    fieldnames = list(data[0].keys())
    # print(fieldnames)

    # Check if save path exists
    if not os.path.exists("./src/data"):
        print(f"Creating Save Path...")
        os.makedirs("./src/data")

    # Save as CSV
    print("Saving to file...")
    with open(f"./src/data/{cur_time}.csv", "w", newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
