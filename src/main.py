from lib.imaga_data_extractor.metadata_extractor import extract_metadata
from lib.imaga_data_extractor.metadata_extractor import get_file_paths

def main():
    ...


if __name__ == "__main__":
    print("Initialized Docker Container 🐳")
    print("Starting Program 🟢")

    print("Getting filepaths for images ⛭⛭⛭")
    try:
        file_paths = get_file_paths()
    except:
        print("Put a Logger here later. We got some errors 🤡")

    for file_path in file_paths:
        extract_metadata(file_path)

    main()

    print("Exiting code ❣️")
