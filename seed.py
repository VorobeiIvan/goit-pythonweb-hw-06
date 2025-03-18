from models import Session, Group, Teacher, Student, Subject, Grade
from faker import Faker
import random


def populate_database():
    session = Session()
    faker = Faker()

    try:
        groups = [Group(name=f"Group-{i}") for i in range(1, 4)]
        session.add_all(groups)

        teachers = [Teacher(name=faker.name()) for _ in range(4)]
        session.add_all(teachers)

        subjects = [Subject(name=faker.word(), teacher=random.choice(teachers)) for _ in range(6)]
        session.add_all(subjects)

        students = [Student(name=faker.name(), group=random.choice(groups)) for _ in range(40)]
        session.add_all(students)

        for student in students:
            for subject in subjects:
                for _ in range(random.randint(5, 10)):
                    session.add(Grade(student=student, subject=subject, value=random.randint(60, 100)))

        session.commit()
    except Exception as e:
        session.rollback()
        print(f"Error occurred: {e}")
    finally:
        session.close()
