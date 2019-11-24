import unittest
from WhoWillWin import Sprite


# 测试英雄和怪物的父类精灵类
class TestSpriteMethods(unittest.TestCase):
    def test_Sprite(self):
        test_1 = Sprite(50, 30)
        self.assertEqual(50, test_1.blood)
        self.assertEqual(30, test_1.damage)
        self.assertNotEqual(50, test_1.blood)
        self.assertNotEqual(30, test_1.damage)
        self.assertTrue(25 <= test_1.hit() <= 35)
        self.assertIsNone(test_1.hit())
        self.assertIsNone(test_1.hit())
        self.assertIsNotNone(test_1.hit())


if __name__ == '__main__':
    unittest.main()
