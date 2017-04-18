from django.contrib import admin
from .models import Faculty
from .models import Department
from .models import Lecturer

admin.site.register(Faculty)
admin.site.register(Department)
admin.site.register(Lecturer)

# Register your models here.
