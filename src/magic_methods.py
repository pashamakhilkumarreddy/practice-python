class MyList(list):
    def __getitem__(self, index):
        if index == 0:
            raise ValueError("Invalid index")
        index = index - 1
        return list.__getitem__(self, index)

    def __setitem__(self, index, val):
        if index == 0:
            raise ValueError("Invalid index")
        index = index - 1
        return list.__setitem__(self, index, val)

    def __delitem__(self, key):
        key = key - 1
        return list.__delitem__(self, key)

    def __mul__(self, other):
        result = [x * y for x, y in zip(self, other)]
        return MyList(result)

custom_list = MyList([12, 14, 16, 20])
print(f'First Item is {custom_list[1]}')
custom_list[1] = 9
print(f'First Item is {custom_list[1]}')

class Employee(object):
    def __init__(self, name: str, age: int, role: str):
        self.name = name
        self.age = age
        self.role = role

    def __call__(self, age: int, role: str):
        self.age = age
        self.role = role

    def __repr__(self):
        return f'Employee is {self.name} of {self.age} and is the {self.role}'

    def __str__(self):
        return f'Employee is {self.name} of {self.age} and is the {self.role}'

stacy = Employee('Gwen Stacy', 25, 'CFO')
print(stacy)
print(f'Employee {stacy.__dict__}')
print(id(stacy))
stacy(26, 'CEO')
print(stacy)

print(f'Employee after call {stacy.__dict__}')
print(id(stacy))
