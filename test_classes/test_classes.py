import pytest
from classes import Teacher, DisciplineTeacher


def test_teacher_init(teacher):
    assert len(Teacher.teachers_list) == 1


def test_get_name(teacher):
    assert teacher.get_name() == 'test_name test_surname'


def test_get_education(teacher):
    assert teacher.get_education() == 'test_education'


def test_get_experience(teacher):
    assert teacher.get_experience() == 'test_experience'


def test_set_experience(teacher):
    assert teacher.set_experience('test_new_experience') == 'test_new_experience'


def test_teacher_get_teacher_data(teacher):
    assert teacher.get_teacher_data() == ('test_name test_surname, образование test_education, '
                                          'опыт работы test_experience лет.')


def test_teacher_add_mark(teacher):
    assert teacher.add_mark('test_student_name', 'test_value') == ('test_name test_surname поставил оценку '
                                                                   'test_value студенту test_student_name.')


def test_teacher_remove_mark(teacher):
    assert teacher.remove_mark('test_student_name', 'test_value') == ('test_name test_surname удалил оценку '
                                                                      'test_value студенту test_student_name.')


def test_teacher_give_a_consultation(teacher):
    assert teacher.give_a_consultation('test_student_class') == ('test_name test_surname провел консультацию '
                                                                 'в классе test_student_class.')


def test_fire_teacher(teacher):
    assert Teacher.fire_teacher(teacher) == 'Учитель уволен'
    assert Teacher.fire_teacher(teacher) == 'Учитель уже был уволен'
    assert len(Teacher.teachers_list) == 0


def test_discipline_teacher_get_discipline(discipline_teacher):
    assert discipline_teacher.get_discipline() == 'test_discipline'


def test_discipline_teacher_get_job_title(discipline_teacher):
    assert discipline_teacher.get_job_title() == 'test_job_title'


def test_discipline_teacher_get_teacher_data(discipline_teacher):
    assert discipline_teacher.get_teacher_data() == ('test_name test_surname, образование test_education, '
                                                     'опыт работы test_experience лет. Предмет test_discipline, '
                                                     'Должность test_job_title.')


def test_discipline_teacher_add_mark(discipline_teacher):
    assert discipline_teacher.add_mark('test_student_name', 'test_value') == ('test_name test_surname поставил оценку '
                                                                              'test_value студенту test_student_name. '
                                                                              'Предмет: test_discipline.')


def test_discipline_teacher_remove_mark(discipline_teacher):
    assert discipline_teacher.remove_mark('test_student_name', 'test_value') == ('test_name test_surname удалил оценку '
                                                                                 'test_value студенту '
                                                                                 'test_student_name.  '
                                                                                 'Предмет: test_discipline.')


def test_discipline_teacher_give_a_consultation(discipline_teacher):
    assert discipline_teacher.give_a_consultation('test_student_class') == ('test_name test_surname провел консультацию'
                                                                            ' в классе test_student_class. По предмету'
                                                                            ' test_discipline как test_job_title.')
