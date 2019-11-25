import unittest
from ApiCacheTest import HttpOperation
import json

# 测试http
class TestHttpOperationMethods(unittest.TestCase):
    def test_HttpOperation(self):
        url = 'http://beta.api.baby-bus.com/api.php/v3/resource_url'
        url_2 = 'https://app-zh.beta.baby-bus.com//super_class_v2'
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
        test_1 = HttpOperation(url, None, None)
        test_2 = HttpOperation(url_2, headers, data)
        #self.assertEqual(50, test_1.get_http())
        #self.assertEqual(30, test_1.damage)
        #self.assertNotEqual(50, test_1.blood)
        #self.assertNotEqual(30, test_1.damage)
        #self.assertTrue(25 <= test_1.hit() <= 35)
        #self.assertIsNone(test_1.get_http())
        #self.assertIsNone(test_1.get_http())
        self.assertIsNotNone(test_1.get_http())
        self.assertIsNotNone(test_2.post_http())
        Str = json.dumps(test_2.post_http())
        Dict = json.loads(Str)
        #dict = test_2.post_http()['states']
        #self.assertEqual(1, dict)
        print(Dict)

if __name__ == '__main__':
    unittest.main()
