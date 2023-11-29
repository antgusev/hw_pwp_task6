from unittest import TestCase
from unique_name import unique_names
from most_dur_course import min, max
from unique_name import unique_names

class Test_task1(TestCase):
    def test_len_list(self):
        res = len(unique_names)
        expected = 33
        self.assertEqual(res, expected)

    def test_duration(self):
        res = min, max
        expected = 12, 20
        self.assertEqual(res, expected)

    def test_unique_name(self):
        res = unique_names
        expected = ('Павел', 'Эдгар', 'Азамат', 'Алена', 'Сергей', 'Кирилл', 'Никита',
                    'Дмитрий', 'Николай', 'Александр', 'Илья', 'Елена', 'Тимур', 'Денис',
                    'Владимир', 'Михаил', 'Анна', 'Юрий', 'Константин', 'Олег', 'Валерий',
                    'Татьяна', 'Роман', 'Вадим', 'Евгений', 'Филипп', 'Алексей', 'Ринат',
                    'Анатолий', 'Иван', 'Максим', 'Антон', 'Адилет')
        self.assertCountEqual(res, expected)

    
