from django.db import models
from django.contrib.auth.models import User


class Mentor(models.Model):
    REGULAR = 1
    SUPERADMIN = 2
    MENTOR_TYPE_CHOICES = (
        (REGULAR, 'REGULAR'),
        (SUPERADMIN, 'SUPERADMIN'),
    )
    username = models.CharField(
        max_length=40, unique=True, blank=False, null=False)
    password = models.CharField(max_length=40, blank=False, null=False)
    phone = models.CharField(max_length=40, blank=True, null=True)
    email = models.CharField(
        max_length=40, unique=True, blank=False, null=False)
    mentor_type = models.IntegerField(
        choices=MENTOR_TYPE_CHOICES, default=REGULAR)
    full_name = models.CharField(max_length=40)
    created_time = models.DateTimeField(
        auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.username


class Board(models.Model):
    board = models.CharField(
        max_length=4,blank=False, null=False, default='CBSE', unique=True)

    def __str__(self):
        return self.board


class MinMaxFloat(models.IntegerField):
    def __init__(self, min_value=None, max_value=None, *args, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        super(MinMaxFloat, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value': self.max_value}
        defaults.update(kwargs)
        return super(MinMaxFloat, self).formfield(**defaults)


class Grade(models.Model):
    grade = MinMaxFloat(min_value=1, max_value=12, default=10)
    board = models.ForeignKey('Board', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.grade)


class Subject(models.Model):
    subject_name = models.CharField(max_length=100, blank=False, null=False)
    grade = models.ForeignKey('Grade', on_delete=models.CASCADE)

    def __str__(self):
        return self.subject_name


class Questions(models.Model):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    QUESTION_WEIGHTAGE_CHOICES = (
        (ONE, 'ONE'),
        (TWO, 'TWO'),
        (THREE, 'THREE'),
        (FOUR, 'FOUR'),
        (FIVE, 'FIVE'),
        (SIX, 'SIX'),
        (SEVEN, 'SEVEN'),
    )
    TEXT = 1
    FILL_IN_THE_BLANKS = 2
    MCQ = 3
    QUESTION_TYPE_CHOICES = (
        (TEXT, 'TEXT'),
        (FILL_IN_THE_BLANKS, 'FILL IN THE BLANKS'),
        (MCQ, 'MCQ'),
    )
    chapter = models.ForeignKey('Chapter', on_delete=models.CASCADE, null=True)
    question_weightage = models.IntegerField(
        choices=QUESTION_WEIGHTAGE_CHOICES, null=True)
    question_type = models.IntegerField(
        choices=QUESTION_TYPE_CHOICES, null=True)
    uploaded_by = models.ForeignKey('Mentor', on_delete=models.CASCADE)
    text = models.TextField(null=False, blank=False)
    source = models.TextField(null=True, blank=True)


class MCQOptions(models.Model):
    question_id = models.ForeignKey('Questions', on_delete=models.CASCADE)
    option_value = models.CharField(max_length=100)


class SubjectSplit(models.Model):
    name = models.CharField(max_length=100)
    board = models.ForeignKey('Board', on_delete=models.CASCADE, null=True)
    question_weightage = models.IntegerField(
        choices=Questions.QUESTION_WEIGHTAGE_CHOICES, null=True)
    question_type = models.IntegerField(
        choices=Questions.QUESTION_TYPE_CHOICES, null=True)
    total_questions = models.IntegerField(default=0)
    questions_to_attempt = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class GeneratedCustomizedPaper(models.Model):
    token = models.CharField(max_length=100)
    file_path = models.CharField(max_length=200, default=None, null=True)
    is_ready = models.BooleanField(default=False)
    mentor = models.ForeignKey(User, on_delete=models.CASCADE)
    submitted_date = models.DateTimeField(null=True, default=None)

    def __str__(self):
        return self.token


class GeneratedTestAndGenericPaper(models.Model):
    token = models.CharField(max_length=100)
    file_path = models.CharField(max_length=200, default=None, null=True)
    is_ready = models.BooleanField(default=False)
    submitted_date = models.DateTimeField(null=True, default=None)

    def __str__(self):
        return self.token


class Chapter(models.Model):
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE)
    chapter_name = models.CharField(max_length=100)

    def __str__(self):
        return self.chapter_name
