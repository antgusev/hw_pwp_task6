from unittest import TestCase
from my_yandisk import response


class Test_response(TestCase):
    def test_response_ok(self):
        res = response
        expected = '<Response [201]>'
        self.assertEqual(res, expected)
        print(f'Код ответа соответствует ', {res})
        
    def test_response_error(self):
        res = response
        expected = '<Response [409]>'
        self.assertEqual(res, expected)
        print(f'Код ответа соответствует ', {res})
        
        