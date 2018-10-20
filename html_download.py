# encoding=utf-8
from urllib import request
from urllib import response
class HtmlDownloader:
    pass
    def download(self, url):
        if url is None:
            return None

        response = request.urlopen(url)
        if response.getcode() != 200:
            return None
        return response.read()