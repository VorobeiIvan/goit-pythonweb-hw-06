from models import Base, engine
from sqlalchemy.orm import sessionmaker
from seed import populate_database
from my_select import get_top_students, get_best_student_by_subject, get_avg_grade_by_group, \
    get_overall_avg_grade, get_teacher_subjects, get_students_in_group, get_student_grades_in_group, \
    get_teacher_avg_grade, get_student_courses, get_student_courses_by_teacher

Session = sessionmaker(bind=engine)
session = Session()

try:
    if __name__ == "__main__":
        Base.metadata.create_all(engine)
        populate_database()

        top_students = get_top_students(session)
        print("Top 5 students with the highest average grade:")
        for student in top_students:
            print(student)

        subject_id = 1
        best_student_subject = get_best_student_by_subject(session, subject_id)
        print(f"\nBest student in subject {subject_id}:")
        print(best_student_subject)

        avg_grade_by_group = get_avg_grade_by_group(session, subject_id)
        print(f"\nAverage grade by group for subject {subject_id}:")
        for group in avg_grade_by_group:
            print(group)

        overall_avg_grade = get_overall_avg_grade(session)
        print(f"\nOverall average grade for all subjects: {overall_avg_grade}")

        teacher_id = 1
        teacher_subjects = get_teacher_subjects(session, teacher_id)
        print(f"\nSubjects taught by teacher {teacher_id}:")
        for subject in teacher_subjects:
            print(subject)

        group_id = 1
        students_in_group = get_students_in_group(session, group_id)
        print(f"\nStudents in group {group_id}:")
        for student in students_in_group:
            print(student)

        student_grades_in_group = get_student_grades_in_group(session, group_id, subject_id)
        print(f"\nStudent grades in group {group_id} for subject {subject_id}:")
        for grade in student_grades_in_group:
            print(grade)

        teacher_avg_grade = get_teacher_avg_grade(session, teacher_id)
        print(f"\nAverage grade for teacher {teacher_id}: {teacher_avg_grade}")

        student_id = 1
        student_courses = get_student_courses(session, student_id)
        print(f"\nCourses taken by student {student_id}:")
        for course in student_courses:
            print(course)

        student_teacher_courses = get_student_courses_by_teacher(session, student_id, teacher_id)
        print(f"\nCourses taken by student {student_id} with teacher {teacher_id}:")
        for course in student_teacher_courses:
            print(course)


finally:
    session.close()