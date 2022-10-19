import requests
import zipfile
import os
import logging

URL = "https://arctraining.github.io/python-2021-04/data/portal-teachingdb-master.zip"

def main():
    """
    Quick script for downloading required data
    """

    req = requests.get(URL, stream=True)

    with open("portal-teachingdb-master.zip", 'wb') as fd:
        for chunk in req.iter_content(chunk_size=128):
            fd.write(chunk)

    logging.info("Data zip file downloaded.")

    if os.path.isdir("data"):
      logging.info("Data directory already exists")
    else:
      os.mkdir("data")
      logging.info("Data directory created.")

    with zipfile.ZipFile("portal-teachingdb-master.zip", 'r') as zip_ref:
      zip_ref.extractall("data")

    logging.info("Data extracted to `data` directory.")

if __name__ == '__main__':
    main()