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
        #36867: time and date
        #271: phone-Marke
        #272: phone-Model
        #305: Software
        #34853: Latitude bzw. Longitude
        interesting_tags = [36867, 271, 272, 305, 34853]
        tag_names = {
         36867: "Date and Time Taken",
         271: "Camera Make",
         272: "Camera Model",
         305: "Software",
         34853: "Latitude and Longtitude"
       }


        exif_data = img._getexif()
        if exif_data:
            for tag, value in exif_data.items():
                 if tag in tag_names:
                  print(f"{tag_names[tag]}: {value}")



                
if __name__ == "__main__":
    image_path = "/Users/fatmashalaby/Documents/road-quality-gen-collabathon-23/src/lib/imaga_data_extractor/images/62774941-A965-4DC8-8376-B88627E3FA33.jpeg"
    extract_metadata(image_path)