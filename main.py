from catloader import get_cat_url_list, download_cats
from decorators import execute_in_threads, timer

from typing import List


@timer
def download_cats_single(cat_urls: List[str]):
    return download_cats(cat_urls)


@timer
@execute_in_threads(max_threads=4, urls_per_thread=5)
def download_cats_4_5(cat_urls: List[str]):
    return download_cats(cat_urls)


@timer
@execute_in_threads(max_threads=4, urls_per_thread=10)
def download_cats_4_10(cat_urls: List[str]):
    download_cats(cat_urls)


@timer
@execute_in_threads(max_threads=4, urls_per_thread=25)
def download_cats_4_25(cat_urls: List[str]):
    download_cats(cat_urls)


@timer
@execute_in_threads(max_threads=8, urls_per_thread=5)
def download_cats_8_5(cat_urls: List[str]):
    download_cats(cat_urls)


@timer
@execute_in_threads(max_threads=8, urls_per_thread=10)
def download_cats_8_10(cat_urls: List[str]):
    download_cats(cat_urls)


@timer
@execute_in_threads(max_threads=16, urls_per_thread=5)
def download_cats_16_5(cat_urls: List[str]):
    download_cats(cat_urls)


@timer
@execute_in_threads(max_threads=50, urls_per_thread=2)
def download_cats_50_2(cat_urls: List[str]):
    download_cats(cat_urls)


@timer
@execute_in_threads(max_threads=100, urls_per_thread=1)
def download_cats_100_1(cat_urls: List[str]):
    download_cats(cat_urls)


print('---------------------------------')
print('--------- Single thread ---------')
print('---------------------------------')

urls = get_cat_url_list()
download_cats_single(cat_urls=urls)

print()
print('---------------------------------')
print('--- 4 threads, 5 urls/thread ----')
print('---------------------------------')

urls = get_cat_url_list()
download_cats_4_5(cat_urls=urls)

print()
print('---------------------------------')
print('--- 4 threads, 10 urls/thread ---')
print('---------------------------------')

urls = get_cat_url_list()
download_cats_4_10(cat_urls=urls)

print()
print('---------------------------------')
print('--- 4 threads, 25 urls/thread ---')
print('---------------------------------')

urls = get_cat_url_list()
download_cats_4_25(cat_urls=urls)

print()
print('---------------------------------')
print('--- 8 threads, 5 urls/thread ----')
print('---------------------------------')

urls = get_cat_url_list()
download_cats_8_5(cat_urls=urls)

print()
print('---------------------------------')
print('--- 8 threads, 10 urls/thread ---')
print('---------------------------------')

urls = get_cat_url_list()
download_cats_8_10(cat_urls=urls)


print()
print('---------------------------------')
print('--- 16 threads, 5 urls/thread ----')
print('---------------------------------')

urls = get_cat_url_list()
download_cats_16_5(cat_urls=urls)


print()
print('---------------------------------')
print('--- 50 threads, 2 urls/thread ----')
print('---------------------------------')

urls = get_cat_url_list()
download_cats_50_2(cat_urls=urls)


print()
print('---------------------------------')
print('--- 100 threads, 1 urls/thread ----')
print('---------------------------------')

urls = get_cat_url_list()
download_cats_100_1(cat_urls=urls)
