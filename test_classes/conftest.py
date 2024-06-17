import pytest
from classes import Teacher, DisciplineTeacher


@pytest.fixture
def teacher():
    Teacher.teachers_list.clear()
    teacher = Teacher('test_name test_surname', 'test_education', 'test_experience')
    return teacher


@pytest.fixture
def discipline_teacher():
    Teacher.teachers_list.clear()
    discipline_teacher = DisciplineTeacher('test_name test_surname', 'test_education',
                                           'test_experience', 'test_discipline', 'test_job_title')
    return discipline_teacher
