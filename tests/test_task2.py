from unittest import TestCase
from myyandisk import *


class Test_response(TestCase):
    def test_response_ok(self):
        res = YaCreate.create_folder(self)
        expected = '<Response [201]>'
        self.assertEqual(res, expected)
        print(f'Код ответа соответствует ', {res})
        
    def test_response_error(self):
        res = YaCreate.create_folder(self)
        expected = '<Response [409]>'
        self.assertEqual(res, expected)
        print(f'Код ответа соответствует ', {res})
        
        