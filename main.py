import requests


URL = 'https://randomuser.me/api/'


class CredentialParser:

    def __init__(self, data):
        data = data['results'][0]
        self.first_name = data['name']['first']
        self.last_name = data['name']['last']
        self.username = data['login']['username']
        self.password = data['login']['salt']

    def log(self):
        print(self.first_name)
        print(self.last_name)
        print(self.username)
        print(self.password)
        print()


while True:
    data = requests.get(url=URL).json()
    credential = CredentialParser(data)
    credential.log()
    input()
