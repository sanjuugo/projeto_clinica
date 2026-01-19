from django.contrib import admin
from geral.models import Patient, Doctor, Institution, Exam

admin.site.register([Patient, Doctor, Institution, Exam])
