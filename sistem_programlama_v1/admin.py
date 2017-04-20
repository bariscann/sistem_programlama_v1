from django.contrib import admin
from .models import Faculty
from .models import Department
from .models import Lecturer
from .models import BasicLecture
from .models import Principle
from .models import Vote

admin.site.register(Faculty)
admin.site.register(Department)
admin.site.register(Lecturer)
admin.site.register(BasicLecture)
admin.site.register(Principle)
admin.site.register(Vote)

# Register your models here.
