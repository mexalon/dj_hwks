from django.contrib import admin
from .models import Student, Course


@admin.register(Student)
class StudetAdmin(admin.ModelAdmin):
    pass


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass
