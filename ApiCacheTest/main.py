from ApiCacheTest import CacheOperation
from ApiCacheTest import HttpOperation
from datetime import datetime as d
import os

if __name__ == '__main__':
    # 以下面接口数据为例
    url = 'https://app-zh.beta.baby-bus.com//super_class_v2'
    headers = {
        'CommonHeaderData': 'ew0KICAiYXBwX2lkIiA6ICIyMTIiLA0KICAiYWNjb3VudF9zaWduIiA6ICIiLA0KICAiY2hhbm5lbC'
                            'IgOiAiYXBwU3RvcmUiLA0KICAiZGV2aWNlX3BsYXRmb3JtIiA6ICJpUGhvbmUiLA0KICAiYXBwX2FnZ'
                            'SIgOiAiMCIsDQogICJhcHBfdmVyc2lvbiIgOiAiMTAuMDAuMDMxNCIsDQogICJhY2NvdW50X3NpZ25fd'
                            'HlwZSIgOiAiIiwNCiAgImRldmljZV90eXBlIiA6ICJpUGhvbmUiLA0KICAiZGV2aWNlX3NjcmVlbiIgO'
                            'iAiMTMzNCo3NTAiLA0KICAicGxhdGZvcm0iIDogIjEiLA0KICAibG9jYXRpb24iIDogIuemj+W7ui3npo'
                            '/lt54iLA0KICAiZGV2aWNlX25hbWUiIDogIuWbveihjOOAgeaXpeeJiOOAgea4r+ihjGlQaG9uZSA3Iiw'
                            'NCiAgImlkZW50IiA6ICIzRDdGREJFNS02OURELTQ3RTEtOTgwQS0yMUE0OTI2OUQwNkQiLA0KICAic2lnb'
                            'l9pZGVudCIgOiAiOEVEOTM0MDYtNEY1Mi00Qzg5LUE3QjItNDRDNEY4QzU4Q0JBIiwNCiAgImxhbmd1YWdl'
                            'IiA6ICJ6aCIsDQogICJvc192ZXJzaW9uIiA6ICIxMi4xMCIsDQogICJjb3VudHJ5IiA6ICJHQiIsDQogICJh'
                            'Y2NvdW50X2lkIiA6ICIiLA0KICAiYXBwX2tleSIgOiAiY29tLnNpbnllZS5iYWJ5YnVzLnJhbmNoIg0KfQ==',
        'CommonHeaderSign': 'C1E0F5F649A7EF1D12E9825496C38D10',
        'CommonHeaderSignType': 'md5'}
    data = {
        'app_key': 'com.sinyee.babybus.world',
        'lang': 'en',
        'age': 0,
        'type': 1
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
