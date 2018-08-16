from django.db import models


class Mentor(models.Model):
    REGULAR = 1
    SUPERADMIN = 2
    MENTOR_TYPE_CHOICES = (
        (REGULAR, 'REGULAR'),
        (SUPERADMIN, 'SUPERADMIN'),
    )
    username = models.CharField(max_length=40, unique=True, blank=False, null=False)
    password = models.CharField(max_length=40, blank=False, null=False)
    phone = models.CharField(max_length=40, blank=True, null=True)
    email = models.CharField(max_length=40, unique=True, blank=False, null=False)
    mentor_type = models.IntegerField(choices=MENTOR_TYPE_CHOICES, default=REGULAR)
    full_name = models.CharField(max_length=40)
    created_time = models.DateTimeField(auto_now_add=True, blank=True, null=True)


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
    subject = models.CharField(max_length=100)
    chapter = models.CharField(max_length=100)
    chapter_number = models.IntegerField(blank=False, null=False)
    question_weightage = models.IntegerField(choices=QUESTION_WEIGHTAGE_CHOICES, null=True)
    question_type = models.IntegerField(choices=QUESTION_TYPE_CHOICES, null=True)
    uploaded_by = models.ForeignKey('Mentor', on_delete=models.CASCADE)
    text = models.TextField(null=False, blank=False)
    source = models.TextField(null = True, blank=True)


class MCQOptions(models.Model):
    question_id = models.ForeignKey('Questions', on_delete=models.CASCADE)
    option_value = models.CharField(max_length=100)


class SubjectSplit(models.Model):
    name = models.CharField(max_length=100)
    question_weightage = models.IntegerField(choices=Questions.QUESTION_WEIGHTAGE_CHOICES, null=True)
    question_type = models.IntegerField(choices=Questions.QUESTION_TYPE_CHOICES, null=True)
    total_questions = models.IntegerField(default=0)
    questions_to_attempt = models.IntegerField(default=0)
