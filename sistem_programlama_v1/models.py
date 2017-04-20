from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.

class Faculty(models.Model):
    # TODO:burada iki primary olmuş oldu normalde uygun fakat bence birini seçmemiz gerekiyor ne olacak
    id = models.AutoField(primary_key=True)
    faculty_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)], unique=True)
    name = models.CharField(max_length=255)


class Department(models.Model):
    id = models.AutoField(primary_key=True)
    department_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)], unique=True)
    name=models.CharField(max_length=255)
    faculty = models.ForeignKey('Faculty')



class Lecturer(models.Model):
    id = models.AutoField(primary_key=True)
    lecturer_code = models.CharField(max_length=10, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    department = models.ForeignKey('Department')

class BasicLecture(models.Model):
    id = models.AutoField(primary_key=True)
    courseCode =  models.CharField(max_length=7, validators=[MinLengthValidator(7)], unique=True)
    courseName = models.CharField(max_length=255)


class Principle(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField()
    importance = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    basic_lecture = models.ForeignKey('BasicLecture')

class Vote(models.Model):
    id = models.AutoField(primary_key=True)
    value = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    lecture = models.ForeignKey('Lecture')
    student = models.ForeignKey('Student')
