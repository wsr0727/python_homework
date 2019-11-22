from ApiCacheTest import Cache_Operationg
from ApiCacheTest import Http_Operation
import json

if __name__ == '__main__':
    url = 'http://beta.api.baby-bus.com/api.php/Api/Test/createHeader'
    headers = 'Content-Type:application/json'
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


    http1 = Http_Operation.HttpOperation(url, headers, json.dumps(data))
    print(http1.post_http())
    file1 = Cache_Operationg.CaheOperationg(str(http1.post_http()))
    file1.operation_file()
