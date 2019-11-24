import requests


class HttpOperation:
    def __init__(self, url, headers, params):
        self.url = url
        self.headers = headers
        self.params = params

    def get_http(self):
        """
        http下的get请求
        :return: response.content
        """
        response = requests.get(url=self.url, headers=self.headers, params=self.params)
        if response.status_code == 200:  # 请求成功
            return response.content  # 返回结果
        else:
            return '接口报错' + response.status_code

    def post_http(self):
        """
        http下host请求
        :return: response.content
        """
        response = requests.post(url=self.url, headers=self.headers, params=self.params)
        if response.status_code == 200:  # 请求成功
            return response.content  # 返回结果
        else:
            return '接口报错' + response.status_code



