import os
import requests
import getpass
import bs4

from .file_tools import *
from .exceptions import NoInternetError

def download(dataset, version="latest", redownload=False):
    """Download data files for the specified datasets. Defaults to downloading latest version on server.
    Parameters:
    dataset (str): The name of the dataset to download data for, or "all" to download data for all datasets
    version (str, optional): Which version of the data files to download. Defaults to latest on server.
    redownload (bool, optional): Whether to redownload the data files, even if that version of the data is already downloaded. Default False.
    Returns:
    bool: Indicates whether download was successful.
    """
    # Process the optional "all" parameter
    if dataset == "all":
        datasets = [
            "HW3",
            "HW4",
            "HW5",
            "HW6",
            "HW18",
        ]

        overall_result = True
        for dataset in datasets:
            if not download(dataset, redownload=redownload):
                overall_result = False

        return overall_result

    # Get our dataset path
    dataset = dataset.lower()
    dataset_path = get_dataset_path(dataset)

    # Update the index
    update_index(dataset)

    # Load the index
    index = get_index(dataset)

    # Validate the version number, including parsing if it's "latest"
    version = validate_version(version, dataset, use_context="download")

    # Construct the path to the directory for this version
    version_path = os.path.join(dataset_path, f"{dataset}_v{version}")

    # See if they've downloaded this version before. Get list of files to download.
    version_index = index.get(version)
    if os.path.isdir(version_path):
        if redownload:
            files_to_download = list(version_index.keys())
        else:
            files_to_download = []
            for data_file in version_index.keys():
                # Compare the server and local hashes, to make sure there was no data corruption
                file_path = os.path.join(version_path, data_file)
                if os.path.isfile(file_path):
                    file_index = version_index.get(data_file)
                    server_hash = file_index.get("hash")
                    local_hash = hash_file(file_path)
                    if local_hash == server_hash:
                        continue
                files_to_download.append(data_file)

            if len(files_to_download) == 0:
                return True
    else:
        os.mkdir(version_path)
        files_to_download = list(version_index.keys())

    # Download the files
    password_protected_datasets = [
        "gbm",
        "hnscc",
        "lscc",
        ]
    password = None

    total_files = len(files_to_download)
    for data_file in files_to_download:

        if (dataset in password_protected_datasets) and (password is None):
            password = getpass.getpass(prompt=f'Password for {dataset} dataset: ') # We manually specify the prompt parameter so it shows up in Jupyter Notebooks
            print("\033[F", end='\r') # Use an ANSI escape sequence to move cursor back up to the beginning of the last line, so in the next line we can clear the password prompt
            print("\033[K", end='\r') # Use an ANSI escape sequence to print a blank line, to clear the password prompt

        file_index = version_index.get(data_file)
        server_hash = file_index.get("hash")
        file_url = file_index.get("url")

        file_path = os.path.join(version_path, data_file)
        file_number = files_to_download.index(data_file) + 1

        downloaded_path = download_file(file_url, file_path, server_hash, password=password, file_message=f"{dataset} v{version} data files", file_number=file_number, total_files=total_files)

        while downloaded_path == "wrong_password":
            password = getpass.getpass(prompt="Wrong password. Try again: ")
            print("\033[F", end='\r') # Use an ANSI escape sequence to move cursor back up to the beginning of the last line, so in the next line we can clear the password prompt
            print("\033[K", end='\r') # Use an ANSI escape sequence to print a blank line, to clear the password prompt

            downloaded_path = download_file(file_url, file_path, server_hash, password=password, file_message=f"{dataset} v{version} data files", file_number=file_number, total_files=total_files)
    return True

def update_index(dataset):
    """Check if the index of the given dataset is up to date with server version, and update it if needed.
    Parameters:
    dataset (str): The name of the dataset to check the index of.
    Returns:
    bool: Indicates if we were able to check the index and update if needed (i.e. we had internet)
    """
    # Get the path to our dataset
    dataset_path = get_dataset_path(dataset)

    # Define our file names we'll need
    index_urls_file = "index_urls.tsv"
    index_hash_file = "index_hash.txt"
    index_file = "index.txt"

    # Get, from the server, what the md5 hash of our index file should be
    index_urls_path = os.path.join(dataset_path, index_urls_file)
    urls_dict = parse_tsv_dict(index_urls_path)
    index_hash_url = urls_dict.get(index_hash_file)

    checking_msg = f"Checking that {dataset} index is up-to-date..."
    print(checking_msg, end='\r')
    try:
        server_index_hash = download_text(index_hash_url)
    finally:
        print(" " * len(checking_msg), end='\r') # Erase the checking message, even if there was an internet error

    index_path = os.path.join(dataset_path, index_file)

    if os.path.isfile(index_path):
        local_index_hash = hash_file(index_path)
        if local_index_hash == server_index_hash:
            return True

    index_url = urls_dict.get(index_file)
    download_file(index_url, index_path, server_index_hash, file_message=f"{dataset} index")

    if os.path.isfile(index_path):
        local_index_hash = hash_file(index_path)
        if local_index_hash == server_index_hash:
            return True
    # If we get here, something apparently went wrong with the download.
    raise NoInternetError("Insufficient internet. Check your internet connection.")

def download_text(url):
    """Download text from a direct download url for a text file.
    Parameters:
    url (str): The direct download url for the text.
    Returns:
    str: The downloaded text.
    """
    try:
        response = requests.get(url, allow_redirects=True)
        response.raise_for_status() # Raises a requests HTTPError if the response code was unsuccessful
    except requests.RequestException: # Parent class for all exceptions in the requests module
        raise NoInternetError("Insufficient internet. Check your internet connection.") from None

    text = response.text.strip()
    return text