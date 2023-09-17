import requests

with open('token.txt', 'r') as file_object:
    token = file_object.read().strip()
class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, path: str):
        params = {'path': '/mountains.jpg', 'overwrite': 'true'}
        headers = {'Authorization': f'OAuth {token}'}
        response = requests.get(url, params=params, headers=headers)

        href = response.json()['href']

        with open(path, 'rb') as f:
            response = requests.put(href, files={'file': f})

        if response.status_code == 201:
            print('Файл  загружен на Яндекс.Диск.')
        else:
            print('Произошла ошибка при загрузке ')

if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    # URL для получения ссылки на загрузку файла
    url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
    path_to_file = r'C:\Users\ig\Pictures\mountains.jpg'
    token = token
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)