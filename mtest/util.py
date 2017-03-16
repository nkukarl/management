import random

import names


class NameUtil(object):

    def _prepare_gender(self, gender=''):
        gender_dict = {
            'M': 'male',
            'F': 'female',
        }
        return gender_dict.get(gender.upper())

    def get_employee_name(self, gender=''):
        if not isinstance(gender, str):
            error_message = 'gender: {} must be a string!'.format(gender)
            raise AssertionError(error_message)
        return names.get_full_name(gender=self._prepare_gender(gender))

    def get_unique_employee_names(self, count):
        if not (isinstance(count, int) and count > 0 and count <= 100):
            error_message = 'count: {} must be a positive integer ' \
                            'no greater than 100!'.format(count)
            raise AssertionError(error_message)
        existing_names = set()
        while count:
            gender = random.choice(['M', 'F'])
            name_ = self.get_employee_name(gender=gender)
            if name_ not in existing_names:
                existing_names.add(name_)
                count -= 1
        return list(existing_names)

    def get_employee_first_name(self, gender=''):
        return names.get_first_name(gender=self._prepare_gender(gender))

    def get_employee_last_name(self):
        return names.get_last_name()

