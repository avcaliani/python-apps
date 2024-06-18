import json
import os
import re
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from zipfile import ZipFile

import requests
from bs4 import BeautifulSoup
from bs4.element import Tag

from app import DOWNLOAD_PATH


def now() -> str:
    return datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")


def to_json(data: dict, indent: int = None) -> str:
    return json.dumps(
        data,
        ensure_ascii=False,
        sort_keys=True,
        indent=indent,
        default=str,
    )


def file_metadata(link: Tag) -> dict:
    url = link.get("href")
    if not url.endswith(".zip"):
        return None
    return {
        "title": link.text,
        "url": url,
        "file_name": re.search(r'.*\/(.*\.zip)', url, re.I).group(1),
        "consulted_at": now(),
        "download": {
            "started_at": None,
            "finished_at": None,
        }
    }


def scrape_files(url: str) -> dict:
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    files = []
    for link in soup.find_all("a", class_="external-link"):
        meta = file_metadata(link)
        if meta:
            files.append(meta)
    return {"source": url, "files": files}


def unzip(path: str) -> None:
    folder_name = re.search(r'(.*)\.zip', path, re.I).group(1)
    with ZipFile(path, 'r') as zip:
        zip.extractall(folder_name)


def download_file(idx, file: dict) -> dict:
    print(f"[{idx}] URL: {file['url']}")
    file["download"]["started_at"] = now()
    path = f"{DOWNLOAD_PATH}/{file['file_name']}"

    response = requests.get(file["url"])
    with open(path, "wb") as f:
        f.write(response.content)
        print(f"[{idx}] File saved at {path}")

    unzip(path)
    print(f"[{idx}] Unzipped File!")
    file["download"]["finished_at"] = now()
    return file


def run(**kwargs) -> None:
    threads = kwargs.get("threads", os.cpu_count())
    metadata = scrape_files(kwargs.get("url"))

    print(f"{len(metadata['files'])} files found!")
    os.makedirs(DOWNLOAD_PATH, exist_ok=True)
    with ThreadPoolExecutor(threads) as executor:
        futures = []
        for idx, file in enumerate(metadata["files"]):
            futures.append(executor.submit(download_file, idx+1, file))
        for future in as_completed(futures):
            print(to_json(future.result(), indent=4))

    with open(f"{DOWNLOAD_PATH}/metadata.json", "wb") as f:
        f.write(to_json(metadata))
