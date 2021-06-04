from django.contrib import admin

from .models import Student, Teacher, S_T_Relation


class S_T_RelationInline(admin.TabularInline):
    model = S_T_Relation
    extra = 1


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    inlines = (S_T_RelationInline,)


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    inlines = (S_T_RelationInline,)
