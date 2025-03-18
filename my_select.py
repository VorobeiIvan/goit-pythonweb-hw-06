from sqlalchemy import select, func, desc
from sqlalchemy.orm import Session
from models import Student, Grade, Group, Subject


def get_top_students(session: Session):
    stmt = (
        select(Student.id, Student.name, func.avg(Grade.value).label("avg_grade"))
        .join(Grade)
        .group_by(Student.id, Student.name)
        .order_by(desc("avg_grade"))
        .limit(5)
    )
    return session.execute(stmt).fetchall()


def get_best_student_by_subject(session: Session, subject_id):
    stmt = (
        select(Student.name, func.avg(Grade.value).label("avg_grade"))
        .join(Grade)
        .filter(Grade.subject_id == subject_id)
        .group_by(Student.id, Student.name)
        .order_by(desc("avg_grade"))
        .limit(1)
    )
    return session.execute(stmt).fetchone()



def get_avg_grade_by_group(session: Session, subject_id):
    stmt = (
        select(Group.name, func.avg(Grade.value).label("avg_grade"))
        .join(Student, Student.group_id == Group.id)
        .join(Grade, Grade.student_id == Student.id)
        .filter(Grade.subject_id == subject_id)
        .group_by(Group.id)
    )
    return session.execute(stmt).fetchall()


def get_overall_avg_grade(session: Session):
    stmt = select(func.avg(Grade.value).label("overall_avg"))
    return session.execute(stmt).scalar()


def get_teacher_subjects(session: Session, teacher_id):
    stmt = select(Subject.name).filter(Subject.teacher_id == teacher_id)
    return session.execute(stmt).fetchall()


def get_students_in_group(session: Session, group_id):
    stmt = select(Student.name).filter(Student.group_id == group_id)
    return session.execute(stmt).fetchall()


def get_student_grades_in_group(session: Session, group_id, subject_id):
    stmt = (
        select(Student.name, Grade.value)
        .join(Grade)
        .filter(Student.group_id == group_id, Grade.subject_id == subject_id)
    )
    return session.execute(stmt).fetchall()


def get_teacher_avg_grade(session: Session, teacher_id):
    stmt = (
        select(func.avg(Grade.value).label("avg_grade"))
        .join(Subject, Subject.id == Grade.subject_id)
        .filter(Subject.teacher_id == teacher_id)
    )
    return session.execute(stmt).scalar()


def get_student_courses(session: Session, student_id):
    stmt = (
        select(Subject.name)
        .join(Grade, Grade.subject_id == Subject.id)
        .filter(Grade.student_id == student_id)
        .distinct()
    )
    return session.execute(stmt).fetchall()


def get_student_courses_by_teacher(session: Session, student_id, teacher_id):
    stmt = (
        select(Subject.name)
        .join(Grade, Grade.subject_id == Subject.id)
        .filter(Grade.student_id == student_id, Subject.teacher_id == teacher_id)
        .distinct()
    )
    return session.execute(stmt).fetchall()
