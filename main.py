class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.finished_courses and course in self.courses_in_progress:
            if course in lecturer.lec:
                lecturer.lec[course] += [grade]
            else:
                lecturer.lec[course] = [grade]
        else:
            return 'Ошибка'

    def _count_rate_st(self, grade):
        for grades in self.grades:
            value = grades.value()
            average = sum(value)/len(value)

    def __lt__(self):
        def _count_rate_st(self, grade)
            return self

    print(f'Имя: {self.name}\nФамилия:{self.surname}\nСредняя оценка за лекции: {self._count_rate_st}\nКурсы в процессе изучения:{" ".join(self.courses_in_progress)}\nЗавершенные курсы:{" ".join(self.finished_courses)})

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.name = name
        self.surname = surname
        self.lec = {}

    def _count_rate(self, grade):
        for grades in self.lec:
            value = grades.value()
            new_grade = sum(value)/len(value)
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия:{self.surname}\nСредняя оценка за лекции: {self._count_rate}'
        return res
    def __lt__(self):
        def _count_rate(self, grade):
            return self


class Reviewer(Mentor):
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия:{self.surname}'
        return res
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


some_reviewer = Reviewer("Some", "Buddy")
some_lecturer = Lecturer("Some", "Buddy", ) #Не пойму, как вписать сюда значения оценок за лекции
some_student = Student('Ruoy', 'Eman', 'man', 'Введение в программирование', 'Python, Git') #И сюда тоже :(
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

print(best_student.grades)
