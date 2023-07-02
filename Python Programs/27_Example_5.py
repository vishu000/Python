class person:
    
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    
    def student(self):
        print(self.name, "is of age :", self.age)
    
    def show(self):
        print("name :", self.name ,"age :", self.age , "sex :", self.sex)

obj = person("vishnu",20,"male")

obj.show()
obj.student()
