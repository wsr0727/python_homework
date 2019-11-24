from ApiCacheTest import CacheOperation
from ApiCacheTest import HttpOperation
from datetime import datetime as d
import os

if __name__ == '__main__':
    # 以下面接口数据为例
    url = 'http://beta.api.baby-bus.com/api.php/Api/Test/createHeader'
    headers = None
    data = {
        "app_id": "212",
        "channel": "appStore",
        "device_platform": "iPhone",
        "app_version": "10.00.0309",
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
        "app_key": "com.sinyee.babybus.ranch"
    }
# ---------分割线--------
    '''
    请求接口前，判断当天缓存文件是否存在，如果存在直接输出缓存数据，如果不存在则请求接口并写入文件
    '''
    # 当天的文件地址
    today_cache = "./cache/" + "{}-{}-{}.txt".format(d.now().year, d.now().month, d.now().day)
    # 判断缓存文件是否存在
    if os.path.exists(today_cache):
        # 今日缓存文件存在，读取缓存数据
        http_content = open(today_cache, 'r', encoding='utf-8-sig')
        http_content_str = http_content.read()
        http_content.close()
        print("以下是缓存数据:", http_content_str)
    else:
        # 缓存文件不存在，请求接口，并写入文件
        http = HttpOperation(url, headers, data)
        file1 = CacheOperation(str(http.post_http().decode()))
        file1.operation_file()
        print("将接口数据已经存入缓存")
