class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.av_grades = []

    def rate_lecturer(self, lector, course, grade):
        if isinstance(lector, Lecturer):
            if course in lector.grades:
                lector.grades[course] += grade
            else:
                lector.grades[course] = grade
        else:
            return 'Ошибка'

    def __str__(self):
        for k, v in self.grades.items():
            self.av_grades.append(v)
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за домашние задания: {sum(self.av_grades) / len(self.av_grades)}\n' \
              f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
              f'Завершенные курсы: {", ".join(self.finished_courses)}\n'
        return res


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.grades = {}
        self.av_grades = []

    def __str__(self):
        pass


class Lecturer(Mentor):
    def rate_hw(self, lector, course, grade):
        if isinstance(lector, Lecturer):
            if course in lector.grades:
                lector.grades[course] += grade
            else:
                lector.grades[course] = grade
        else:
            return 'Ошибка'

    def __str__(self):
        for k, v in self.grades.items():
            self.av_grades.append(v)
        self.res = f'Имя: {self.name}\nФамилия: {self.surname}\nОценка: {sum(self.av_grades) / len(self.av_grades)}'
        return self.res


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student):
            if course in student.grades:
                student.grades[course] += grade
            else:
                student.grades[course] = grade
        else:
            return 'Ошибка'

    def __str__(self):
        self.res = f'Имя: {self.name}\nФамилия: {self.surname}\n'
        return self.res


best_student_1 = Student('Ruoy', 'Eman', 'your_gender')
best_student_2 = Student('Nastya', 'Vasilyeva', 'your_gender')
best_student_1.courses_in_progress += ['Python', 'GIT']
best_student_1.finished_courses += ['Введение в программирование']
best_student_2.courses_in_progress += ['C++', 'MQTT']
best_student_2.finished_courses += ['Введение в программирование']

best_reviewer = Reviewer('Alex', 'Sigel')
best_reviewer.rate_hw(best_student_1, 'Python', 5)
best_reviewer.rate_hw(best_student_2, 'Python', 7)

best_lecturer_1 = Lecturer('Vlad', 'Dolmatov')
best_lecturer_2 = Lecturer('Kseniya', 'Andreeva')

best_student_1.rate_lecturer(best_lecturer_1, 'GIT', 9.9)
best_student_2.rate_lecturer(best_lecturer_2, 'GIT', 1)

print(best_reviewer)
print()
print(best_lecturer_1)
print()
print(best_student_1)

list_lecturer = [best_lecturer_1, best_lecturer_2]
list_student = [best_student_1, best_student_2]


def rate_college(colleges):
    name_1 = colleges[0].surname
    name_2 = colleges[1].surname

    average_grade = {}
    for l in colleges:
        average_grade[l.surname] = [v for k, v in l.grades.items()]
    print(average_grade)
    if sum(average_grade[name_1]) > sum(average_grade[name_2]):
        print(name_1, *average_grade[name_1])
    else:
        print(name_2, *average_grade[name_2])


rate_college(list_lecturer)
rate_college(list_student)


def rate_homework(list_lecturer, courses):
    average_grade = []
    for l in list_lecturer:
        average_grade.extend(l.av_grades)
    return sum(average_grade) / len(average_grade)
