from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Question_DB)
admin.site.register(Question_Paper)
admin.site.register(Section)
admin.site.register(Exam_Model)