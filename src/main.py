from lib.imaga_data_extractor.metadata_extractor import extract_metadata
from lib.imaga_data_extractor.metadata_extractor import get_file_paths
from lib.imaga_data_extractor.save_data import save_as_csv, save_as_json, flatten_dict


def main():
    ...


if __name__ == "__main__":
    metadata_collector = {}  # Running dict
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
            #print(file_path)
            metadata_collector[index] = extract_metadata(file_path)
        print("Extracted Metadata ✅")
    except:
        # TODO Logger and exception cather here
        print("Put a Logger here later. We got some errors 🤡")
        pass

    #print(metadata_collector)  # TODO: Remove later
    #main()

    # Save metadata as datasets
    try:
        print("Saving dataset as json ⛭⛭⛭")
        save_as_json(metadata_collector)
        print("Saved to a json file in Path(./data/) ✅")

    except Exception as e:
        # TODO Logger and exception cather here
        print("Put a Logger here later. We got some errors 🤡")
        print(e)
        pass

    try:
        print("Saving dataset as csv ⛭⛭⛭")
        save_as_csv(metadata_collector)
        print("Saved to a csv file in Path(./data/) ✅")
    except Exception as e:
        # TODO Logger and exception cather here
        print("Put a Logger here later. We got some errors 🤡")
        print(e)
        pass

    print("Exiting code ❣️")
