from django.db import models


# Create your models here.

class Faculty(models.Model):
    # TODO:burada iki primary olmuş oldu normalde uygun fakat bence birini seçmemiz gerekiyor ne olacak
    #id = models.AutoField(primary_key=True)
    faculty_code = models.CharField(max_length=3, primary_key=True)
    name = models.TextField()


class Department(models.Model):
    department_code = models.CharField(max_length=3, primary_key=True)
    name=models.TextField()
    faculty = models.ForeignKey('Faculty')



class Lecturer(models.Model):
    lecturer_code = models.TextField(primary_key=True)
    first_name = models.TextField()
    last_name = models.TextField()

