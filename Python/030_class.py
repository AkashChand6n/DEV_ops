class person:
    def __init__(self,fname='default_name',age=18):
        self.fname = fname
        self.age = age
        self.skills=[]
    def printing(self):
        return f'name={self.fname}\n age={self.age} \n skills={self.skills}'
    def add_skill(self,skill):
        self.skills.append(skill)


class student(person):
    def __init__(self, fname='default_name', age=18 ,stud_id=0):
        super().__init__(fname, age)
        self.student_id = stud_id

    def printing(self):
        return f'{super().printing()} \n student_id = {self.student_id}'


s1=student("akash",22,101)
s1.add_skill("kill")
print(s1.printing())

# name = input("enter the name:")
# a = input("enter the age:")
# s = input("enter the skills:")
# p = person(name,a)
# p.add_skill(s)
# print(p.printing())
