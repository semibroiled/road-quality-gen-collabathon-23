from PIL import Image
import exifread
import subprocess
import pyheif


def extract_metadata(image_path):
    try:
        heif_file = pyheif.read(image_path)
        metadata = heif_file.metadata

        for item in metadata:
            if 'Exif' in item['type']:
                exif_data = item['data']
                # Process and print EXIF data as needed
                print("EXIF Data:", exif_data)
    except FileNotFoundError:
        print(f"File not found: {image_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    image_path = "/Users/fatmashalaby/Documents/road-quality-gen-collabathon-23/src/lib/imaga_data_extractor/images/62774941-A965-4DC8-8376-B88627E3FA33.heic"
    extract_metadata(image_path)