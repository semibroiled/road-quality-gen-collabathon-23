from lib.imaga_data_extractor.metadata_extractor import extract_metadata
from lib.imaga_data_extractor.metadata_extractor import get_file_paths


def main():
    ...


if __name__ == "__main__":
    metadata = {}  # Running dict
    print("Initialized Docker Container 🐳")
    print("Starting Program 🟢")

    print("Getting filepaths for images ⛭⛭⛭")
    try:
        file_paths = get_file_paths()
        print("Retrieved File Paths ✅")
    except:
        # TODO: Logger and error collector here
        print("Put a Logger here later. We got some errors 🤡")

    try:
        print("Extracting Metadata ⛭⛭⛭")
        for index, file_path in enumerate(file_paths):
            metadata["index"](extract_metadata(file_path))
        print("Extracted File Paths ✅")
    except:
        # TODO Logger and exception cather here
        print("Put a Logger here later. We got some errors 🤡")
        pass

    print(metadata)
    main()

    print("Exiting code ❣️")
