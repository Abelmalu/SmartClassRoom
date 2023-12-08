from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User

class Section(models.Model):
    professor = models.ForeignKey(User, limit_choices_to={'groups__name': "Professor"}, on_delete=models.CASCADE)
    section_name = models.CharField(max_length=10)
    students = models.ManyToManyField(User, limit_choices_to={'groups__name': "Student"}, related_name='student_groups')

    def __str__(self):
        return self.section_name


class Group_Form(ModelForm):
    class Meta:
        model = Section
        fields = '__all__'
        exclude = ['professor']