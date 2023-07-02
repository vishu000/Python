class person:
    
    section = "A"
    
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    
s1 = person("hari", 20, "male")

print(s1.name)
print(s1.age)
print(s1.sex)

print(person.section)