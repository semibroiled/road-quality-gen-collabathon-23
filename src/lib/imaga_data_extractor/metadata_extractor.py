"""This module is used to extract metadata from images"""
from PIL import Image
from pathlib import Path
from typing import Dict

import os


# Reach data in nested directory
def get_file_paths(root_dir: Path = ".") -> list[str]:
    """This function returns a list of file paths for our images
    Args:
        root_dir (str, optional): Input is the root directory where we
        are currently working in. Defaults to ".".

    Returns:
        list[str]: The function returns a list with the relevant file paths
        from the Image folder. It looks for .jpeg files in
        the directories
    """
    # Empty List to store all filepaths
    file_paths = []

    # Recursively get all files from current working directory
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if ".jpeg" in file:
                # Append filepaths to empty list
                file_paths.append(os.path.join(root, file))

    return file_paths


def extract_metadata(image_path: Path) -> Dict:
    """
        Function to extract Metadata from images

    Args:
        image_path (Path): _description_

    Returns:
        Dict: _description_
    """

    # Initialize Dictionary for current Image
    data = {}
    data["filename"] = image_path

    # Empty Dictionary
    metadata = {}

    # Open the image using Pillow
    with Image.open(image_path) as img:
        # Print image information
        # print("Image Format:", img.format)
        # print("Image Mode:", img.mode)
        # print("Image Size:", img.size)

        # Extract EXIF data
        # 36867: time and date
        # 271: phone-Marke
        # 272: phone-Model
        # 305: Software
        # 34853: Latitude bzw. Longitude
        interesting_tags = [36867, 271, 272, 305, 34853, 282]
        tag_names = {
            36867: "Datetime",
            271: "Camera Make",
            272: "Camera Model",
            305: "Firmware",
            34853: "Latitude and Longtitude",
            282: "DPI",
        }

        exif_data = img._getexif()
        if exif_data:
            for tag, value in exif_data.items():
                if tag in tag_names:
                   ##start
                   #removes the binary value from the Latitude
                   #and Longtitude dict
                    if(type(value) == dict):
                        original_dict = value
                        del original_dict[5]
                        data[tag_names[tag]] = original_dict

                    else:
                        ##end
                        data[tag_names[tag]] = value

        return data
