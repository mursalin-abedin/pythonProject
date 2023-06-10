class Employee:
    def __init__(self, name):
        self.name = name

    @classmethod
    def manager(cls, name_of_manager):
        _employee = cls(name_of_manager)
        return _employee

    @classmethod
    def executive(cls, name_of_executive):
        _employee = cls(name_of_executive)
        return _employee

    def isHired(self):
        print("Hired")


adam = Employee.manager("Adam")
joe = Employee.executive("joe")

adam.isHired()
joe.isHired()