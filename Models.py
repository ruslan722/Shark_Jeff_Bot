from peewee import *

db = SqliteDatabase('school.db')

class BaseModel(Model):
    class Meta:
        database = db

class Teacher(BaseModel):
    name = CharField()
    telegram_id = CharField(unique=True)

class Student(BaseModel):
    name = CharField()
    telegram_id = CharField(unique=True)

class Achievement(BaseModel):
    description = CharField()
    student = ForeignKeyField(Student, backref='achievements')

def create_teacher(name, telegram_id):
    teacher, created = Teacher.get_or_create(name=name, telegram_id=telegram_id)
    return teacher

def create_student(name, telegram_id):
    student, created = Student.get_or_create(name=name, telegram_id=telegram_id)
    return student

def add_achievement(student, description):
    achievement, created = Achievement.get_or_create(description=description, student=student)
    return achievement


db.connect()
db.create_tables([Teacher, Student, Achievement])


teacher_yuri = create_teacher('Юрий Силенок', '@YuriSilenok')


student_ruslan = create_student('Руслан Оноприенко', 'CazSong')
achievement_ruslan = add_achievement(student_ruslan, 'Победитель олимпиады по программированию')

