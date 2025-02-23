from rest_framework import serializers
from .models import Class, Student, Subject, Teacher, Schedule


class ClassSerializer(serializers.ModelSerializer):
    student_count = serializers.IntegerField(source="student_count", read_only=True)

    class Meta:
        model = Class
        fields = ["name", "student_count"]


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ["name"]


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ["name"]


class ScheduleSerializer(serializers.ModelSerializer):
    school_class = ClassSerializer()
    subject = SubjectSerializer()
    teacher = TeacherSerializer()

    class Meta:
        model = Schedule
        fields = ["school_class", "subject", "day_of_week", "hour", "teacher"]
