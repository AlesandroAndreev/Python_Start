class School:
    def __init__(self, school_name, teachers, students):
        self._school_name = school_name
        self._teachers = teachers
        self._students = students

    def get_all_classes(self):
        classes = set([student.get_class_room for student in self._students])
        return list(sorted(classes, key=lambda x: int(x[:-1])))

    def get_students(self, class_room):
        return [student.get_short_name for student in self._students if
                class_room == student.get_class_room]

    def get_teachers(self, class_room):
        return [teacher.get_short_name for teacher in self._teachers if
                class_room in teacher.get_classes]

    def find_student(self, student_full_name):
        for person in self._students:
            if student_full_name == person.get_full_name:
                teachers = [teachers.get_short_name for teachers in
                            self._teachers if person.get_class_room in
                            teachers.get_classes]
                lessons = [teachers.get_courses for teachers in
                           self._teachers if person.get_class_room in
                           teachers.get_classes]
                parents = person.get_parents

                return {
                    'full_name': student_full_name,
                    'class_room': person.get_class_room,
                    'teachers': teachers,
                    'lessons': lessons,
                    'parents': parents
                    }

    @property
    def name(self):
        return 'School name ' \
               '"{}"'.format(self._school_name)




class People:
    def __init__(self, last_name, first_name, middle_name):
        self._last_name = last_name
        self._first_name = first_name
        self._middle_name = middle_name

    @property
    def get_full_name(self):
        return '{0} {1} {2}'.format(self._last_name,
                                    self._first_name,
                                    self._middle_name)

    @property
    def get_short_name(self):
        return '{0} {1}.{2}.'.format(self._last_name,
                                     self._first_name[:1],
                                     self._middle_name[:1])


class Student(People):
    def __init__(self, last_name, first_name, middle_name,
                 class_room, mather, father):
        People.__init__(self, last_name, first_name, middle_name)
        self._class_room = class_room
        self._parents = {
            'mather': mather,
            'father': father
            }

    @property
    def get_class_room(self):
        return self._class_room

    @property
    def get_parents(self):
        return self._parents


class Teacher(People):
    def __init__(self, last_name, first_name, middle_name,
                 courses, classes):
        People.__init__(self, last_name, first_name, middle_name)
        self._courses = courses
        self._classes = classes

    @property
    def get_courses(self):
        return self._courses

    @property
    def get_classes(self):
        return self._classes


teachers = [
    Teacher('Lotov', 'Lil', 'Arty', 'Java',
            ['1J', '2J', '1P']),
    Teacher('Belkin', 'Vi', 'Va', 'Python',
            ['1P', '2P', '2J'])]

students = [
    Student('Lol', 'lili', 'lulu', '1P', 'lol О. А.', 'lol А. В.'),
    Student('Patter', 'pa', 'Ki', '1P', 'patter Т.В.', 'Patter А.В.'),
    Student('Mor', 'Mar', 'Mir', '1P', 'Mor А.E.', 'Mor С.А.'),
    Student('Ass', 'Oss', 'Iss', '1P', 'Ass А.К.', 'Ass Н.В.'),
    Student('Bob', 'Arr', 'Ass', '1P', 'Bob В.А.', 'Bob А.Т'),
    Student('Nikkk', 'No', 'Yes', '1P', 'Nikkk Н.А.', 'Nikk Н.С.')]

school = School('GB', teachers, students)

print(school.name)
print(school.get_all_classes())
print(school.get_students('1P'))
student = school.find_student('Nikkk No Yes')
print('Student: {0} Class: "{1}" ''Teacher: {2} Subject: {3}'.format(student['full_name'],
student['class_room'], ', '.join(student['teachers']), ', '.join(student['lessons'])))
print('Parents: {0}, {1}'.format(student['parents']['father'], student['parents']['mather']))
print('Class: "1P" Teacher: ''{0}'.format(', '.join(school.get_teachers('1P'))))

