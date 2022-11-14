class Cat:
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age

    def __call__(self):
        return f'\tname: {self.name}, sex: {self.sex}, age: {self.age}'