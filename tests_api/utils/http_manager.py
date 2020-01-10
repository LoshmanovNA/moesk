import requests


class HttpManager:
    headers = {
        'Content-Type': 'application/json',
        'charset': 'utf-8',
    }

    @staticmethod
    def auth(url, data):
        result = requests.post(url, data=data)
        response = result.json()
        HttpManager.headers['X-User-Token'] = response["sessionId"]
        return result

    @staticmethod
    def get(url):
        result = requests.get(url, headers=HttpManager.headers)
        return result

    @staticmethod
    def post(url, body):
        result = requests.post(url,
                               json=body,
                               headers=HttpManager.headers)
        return result

    @staticmethod
    def delete(url):
        params = {'X-User-Token': HttpManager.headers['X-User-Token']}
        result = requests.delete(url, params=params)
        return result
