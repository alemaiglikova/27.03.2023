import json
import requests


class Getjson:
    def __init__(self, url, path):
        self.url=url
        self.path=path

    def get_data(self):
        response=requests.get(url=self.url)
        return response.json()

    def data_json(self, data):
        with open(self.path, "w") as f:
            json.dump(data, f)

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/todos"
    path = "data.json"
    todo_data = Getjson(url, path)
    data = todo_data.get_data()
    todo_data.data_json(data)


