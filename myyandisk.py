import requests


class YaCreate:
    def __init__(self, token: str):
        self.token = token

    def create_folder(self):
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        params = {"path": "Тест_новая_папка"}
        headers = {"Authorization": token}
        
        response = requests.put(url, headers=headers, params=params)
        print(response)
        return response


if __name__ == '__main__':
    token = ''
    creater = YaCreate(token)
    result = creater.create_folder()