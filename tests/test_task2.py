from unittest import TestCase
from my_yandisk import YaCreate


class Test_response(TestCase):
    def test_response_ok(self):
        res = YaCreate(lambda: self.create_folder())
        expected = '<Response [201]>'
        self.assertEqual(res, expected)
        print(f'Код ответа соответствует ', {res})
        
    def test_response_error(self):
        res = YaCreate(lambda: self.create_folder())
        expected = '<Response [409]>'
        self.assertEqual(res, expected)
        print(f'Код ответа соответствует ', {res})


if __name__ == '__main__':
    TestCase.main()