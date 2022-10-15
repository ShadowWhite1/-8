import requests
from pprint import pprint


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def upload(self, file_path, filename):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {'path': file_path, 'overwrite': 'true'}
        source = requests.get(upload_url, headers = headers, params = params)
        source_getted = source.json()
        href = source_getted.get("href", "")
        result = requests.put(href, data = open(filename, 'rb'))
        return result

if __name__ == '__main__':
    token = ""
    uploader = YaUploader(token)
    pprint(uploader.upload('netology/test1015.txt', "test1015.txt"))