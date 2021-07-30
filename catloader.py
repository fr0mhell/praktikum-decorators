from constants import API_KEY
from decorators import timer

from pathlib import Path
from typing import List
import requests


API_URL = 'https://api.thecatapi.com/v1/images/search'
HEADERS = {
    'x-api-key': API_KEY,
}
SIZE = 'full'
LIMIT = 10
FOLDER = './cats'

# Create folder if it does not exist
if not Path(FOLDER).exists():
    Path(FOLDER).mkdir()


def get_cat_url_list(size: str = SIZE, limit: int = LIMIT) -> List[str]:
    response = requests.get(
        url=API_URL,
        headers=HEADERS,
        params={
            'size': size,
            'limit': limit,
        },
    )

    return [obj['url'] for obj in response.json() if obj.get('url')]


def download_cat(cat_url: str, cat_folder: str = FOLDER):
    if cat_folder.endswith('/'):
        raise ValueError(
            f'"cat_folder" value ({cat_folder}) '
            f'unexpectedly contains trailing slash symbol ("/")'
        )

    cat_picture = requests.get(cat_url, headers=HEADERS)
    # Extract filename from URL:
    # https://cdn2.thecatapi.com/images/RfpiTrLZ4.jpg
    # to
    # RfpiTrLZ4.jpg
    cat_filename = cat_url.split('/')[-1]
    cat_filepath = Path(f'{cat_folder}/{cat_filename}')

    with open(cat_filepath, 'wb') as cat_file:
        cat_file.write(cat_picture.content)


def download_cats(cat_urls: List[str]):
    for url in cat_urls:
        download_cat(url)
