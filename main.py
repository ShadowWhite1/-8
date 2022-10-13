import requests

class YaUploader:
    def __init__(self, token):
        self.token = token

    def upload(self, file_path, filename):
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {self.token}'}
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        params = {"path": file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        r = response.json()
        response = requests.put(r['href'], data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")

if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = 'netologi/test.txt'
    token = ""
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file, 'test.txt')




