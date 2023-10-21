from PIL import Image
import exifread


def extract_metadata(image_path):
    # Open the image using Pillow
    with Image.open(image_path) as img:
        # Print image information
        print("Image Format:", img.format)
        print("Image Mode:", img.mode)
        print("Image Size:", img.size)

        # Extract EXIF data
        exif_data = img._getexif()
        if exif_data:
            for tag, value in exif_data.items():
                tag_name = exifread.FIELD_TYPES[tag]
                print(f"{tag_name} ({tag}): {value}")

if __name__ == "__main__":
    image_path = "/Users/fatmashalaby/Documents/road-quality-gen-collabathon-23/src/lib/imaga_data_extractor/images/62774941-A965-4DC8-8376-B88627E3FA33.jpeg"
    extract_metadata(image_path)