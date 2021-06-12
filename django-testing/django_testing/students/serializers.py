from rest_framework import serializers
from django.conf import settings

from students.models import Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ("id", "name", "students")

    def validate_students(self, data):
        maxlen = settings.MAX_STUDENTS_PER_COURSE
        if len(data) >= maxlen:
            raise serializers.ValidationError(f'На курсе уже есть {maxlen} студентов')
        return data
