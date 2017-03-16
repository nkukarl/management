class Employee(object):
    # def __init__(self, name, age, gender, employee_id,
    #              title=None, manager=None):
    def __init__(self, first_name, last_name, age, gender, employee_id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.employee_id = employee_id
        # self.title = title
        # self.manager = manager

    def get_basic_info(self):
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age,
            'gender': self.gender,
        }

    # def set_title(self, title):
    #     self.title = title
    #
    # def get_title(self):
    #     return self.title
    #
    # def set_manager(self, manager):
    #     manager.add_subordinate(self)
    #     self.manager = manager
    #
    # def get_manager(self):
    #     return self.manager
    #
    # def get_peers(self):
    #     if not self.manager:
    #         return []
    #     return self.manager.get_subordinate()