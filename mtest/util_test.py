import random
from unittest import TestCase

from nose_parameterized import parameterized

from mtest.util import NameUtil


class TestNameUtil(TestCase):
    name_util = NameUtil()

    @parameterized.expand([
        ('M', 'male'),
        ('m', 'male'),
        ('F', 'female'),
        ('f', 'female'),
        ('', None),
    ])
    def test_prepare_gender(self, input_value, expected_value):
        gender = self.name_util._prepare_gender(input_value)
        self.assertEqual(gender, expected_value)

    def test_get_unique_employee_names(self):
        count = random.randint(2, 6)
        employee_names = self.name_util.get_unique_employee_names(count)
        assert isinstance(employee_names, list)
        self.assertEqual(len(set(employee_names)), count)


