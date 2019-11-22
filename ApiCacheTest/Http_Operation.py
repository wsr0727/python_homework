import requests
import json

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



url = 'http://beta.api.baby-bus.com/api.php/Api/Test/createHeader'
headers = None
data = {
        "app_id": "212",
        "account_sign": "",
        "channel": "appStore",
        "device_platform": "iPhone",
        "app_age": "0",
        "app_version": "10.00.0309",
        "account_sign_type": "",
        "device_type": "iPhone",
        "device_screen": "1334*750",
        "platform": "1",
        "location": "福建-福州",
        "device_name": "国行、日版、港行iPhone 7",
        "ident": "3D7FDBE5-69DD-47E1-980A-21A49269D06D",
        "sign_ident": "8ED93406-4F52-4C89-A7B2-44C4F8C58CBA",
        "language": "zh",
        "os_version": "12.10",
        "country": "US",
        "account_id": "",
        "app_key": "com.sinyee.babybus.ranch"
    }
http1 = HttpOperation(url, headers, data)
print(http1.post_http())
