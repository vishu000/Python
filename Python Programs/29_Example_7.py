class person:
    
    section = "A"
    
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    @classmethod
    def modify_section_name(cls, new_section):
        # modify class variable
        cls.section = new_section
    
s1 = person("hari", 20, "male")
print(person.section)
s1.modify_section_name('B')
print(person.section)