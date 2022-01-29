from catloader.catloader import get_cat_url_list, download_cats


if __name__ == '__main__':
    urls = get_cat_url_list()
    download_cats(cat_urls=urls)
