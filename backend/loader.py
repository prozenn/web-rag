from llama_index.readers.web import WholeSiteReader
from selenium import webdriver


def get_web_documents(urls: list):
    docs = []
    for url in urls:
        scrapper = WholeSiteReader(
            prefix=url,
            max_depth=1,
            driver=webdriver.Chrome(),
        )
        docs.extend(scrapper.load_data(url))

    return docs
