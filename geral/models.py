from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=100)
    cpf = models.CharField(max_length=30)
    birth = models.DateField()
    sex = models.CharField(max_length=50)
    phone = models.CharField(max_length=30)
    email = models.EmailField(blank=True)
    observation = models.TextField(blank=True)

class Doctor(models.Model):
    name=models.CharField(max_length=100)
    specialization = models.CharField(max_length=50)
    document = models.CharField(max_length=30)
    phone = models.CharField(max_length=30, blank=True)

class Exam(models.Model) :
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    image = models.ImageField()
    status = models.CharField(max_length=50, blank=True)
    report = models.TextField(blank=True)
    validated = models.BooleanField(default=False)
    date = models.DateField(auto_now= True)

class Institution(models.Model):
    logo = models.ImageField()
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
