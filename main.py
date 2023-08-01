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

student_1 = Student('Иван', 'Иванов', 'M')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['Excel']
student_1.courses_in_progress += ['Java']

student_2 = Student('Елена', 'Еленова', 'Ж')
student_2.courses_in_progress += ['Python']
student_2.courses_in_progress += ['C++']
student_2.courses_in_progress += ['JavaScript']

reviewer_1 = Reviewer('Петр', 'Петров')
reviewer_1.courses_attached += ['Python']
reviewer_1.courses_attached += ['Java']
reviewer_1.courses_attached += ['Excel']
print(f'Проверяющий: {reviewer_1.name} {reviewer_1.surname}\nВедёт курсы: {" ".join(reviewer_1.courses_attached)}\n')

reviewer_2 = Reviewer('Юлия', 'Юльева')
reviewer_2.courses_attached += ['Python']
reviewer_2.courses_attached += ['C++']
reviewer_2.courses_attached += ['JavaScript']
print(f'Проверяющий: {reviewer_2.name} {reviewer_2.surname}\nВедёт курсы: {" ".join(reviewer_2.courses_attached)}\n')

reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Java', 5)
reviewer_1.rate_hw(student_1, 'Excel', 6)

reviewer_2.rate_hw(student_2, 'Python', 7)
reviewer_2.rate_hw(student_2, 'C++', 9)
reviewer_2.rate_hw(student_2, 'JavaScript', 5)

print(f'Оценки студента: {student_1.name} {student_1.surname}\n{student_1.grades}')
print(f'Оценки студента: {student_2.name} {student_2.surname}\n{student_2.grades}')
print("-----------------\n")

lecturer_1 = Lecturer('Сидор', 'Сидоров')
lecturer_1.courses_attached += ['Python']
lecturer_1.courses_attached += ['Java']
lecturer_1.courses_attached += ['Excel']

lecturer_2 = Lecturer('Евгений', 'Евгеньев')
lecturer_1.courses_attached += ['Python']
lecturer_1.courses_attached += ['C++']
lecturer_1.courses_attached += ['JavaScript']

student_1.rate_lec(lecturer_1, 'Python', 9)
student_1.rate_lec(lecturer_1, 'Java', 8)
student_1.rate_lec(lecturer_1, 'Excel', 2)

student_2.rate_lec(lecturer_2, 'Python', 7)
student_2.rate_lec(lecturer_2, 'C++', 6)
student_2.rate_lec(lecturer_2, 'JavaScript', 5)

print(f'Оценки лектору: {lecturer_1.name} {lecturer_1.surname}\n{lecturer_1.grades}')
print(f'Оценки лектору: {lecturer_2.name} {lecturer_2.surname}\n{lecturer_2.grades}')
print("-----------------\n")

print(student_1)
print(student_2)
print(reviewer_1)
print(reviewer_2)
print(lecturer_1)
print(lecturer_2)
print(best_student.grades)
