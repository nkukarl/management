import random
from unittest import TestCase

from logic.employee import Employee
from mtest.util import NameUtil


class TestEmployee(TestCase):
    def test_get_basic_info(self):
        """
        Test get_basic_info() in Employee class
        """
        # Setup
        gender = random.choice(['M', 'F'])
        name_util = NameUtil()
        first_name = name_util.get_employee_first_name(gender=gender)
        last_name = name_util.get_employee_last_name()
        age = random.randint(18, 50)

        # Exercise
        employee = Employee(first_name, last_name, age, gender)
        basic_info = employee.get_basic_info()

        # Verify
        expected_basic_info = {
            'first_name': first_name,
            'last_name': last_name,
            'age': age,
            'gender': gender,
        }
        self.assertEqual(basic_info, expected_basic_info)




