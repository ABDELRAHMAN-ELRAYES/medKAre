# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from django.utils import timezone
import pytz

cairo_timezone = pytz.timezone('Africa/Cairo')

class Doctor(models.Model):
    doctor_id = models.IntegerField(primary_key=True)
    doctor_fname = models.CharField(db_column='doctor_Fname', max_length=64, blank=True, null=True) 
    doctor_lname = models.CharField(db_column='doctor_Lname', max_length=64, blank=True, null=True)  
    doctor_phone = models.CharField(max_length=64, blank=True, null=True)
    doctor_street = models.CharField(max_length=64, blank=True, null=True)
    doctor_city = models.CharField(max_length=64, blank=True, null=True)
    doctor_username = models.CharField(unique=True, max_length=64)
    doctor_gmail = models.CharField(unique=True, max_length=100)
    doctor_password = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'doctor'


class DoctorAppointment(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE)  
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)                            
    appointment_status = models.CharField(max_length=64, blank=True, null=True,default='scheduled')
    appointment_date = models.DateField(blank=True, null=False, primary_key=True)
    appointment_time = models.TimeField(blank=True, null=False)
    illness_description = models.TextField(blank=True, null=True)
    appointment_address = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'doctor_appointment'
        unique_together = (('appointment_date', 'appointment_time'),)


class DoctorSpecialization(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, blank=True, null=True)
    doctor_speciality = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'doctor_specialization'


class Medicine(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE)  
    medicine_id = models.IntegerField(primary_key=True,null=False)
    medicine_istaken = models.CharField(db_column='medicine_isTaken', max_length=64, blank=True, null=True,default='untaken')  
    medicine_name = models.CharField(max_length=64, blank=True, null=True)
    medicine_description = models.TextField(blank=True, null=True)

    medicine_date = models.DateField(blank=True, null=True, default=timezone.now().astimezone(cairo_timezone).date())    
    medicine_time = models.TimeField(blank=True, null=True, default=timezone.now().astimezone(cairo_timezone).time())  
    class Meta:
        managed = False
        db_table = 'medicine'
        unique_together = (('user', 'medicine_id'),)


class Message(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE, primary_key=True)  
    message_id = models.IntegerField()
    message_description = models.TextField(blank=True, null=True)
    egypt_timezone = pytz.timezone('Africa/Cairo')
    message_date = models.DateField(blank=True, null=True, default=timezone.now().astimezone(egypt_timezone))    #
    message_time = models.TimeField(blank=True, null=True, default=timezone.now().astimezone(egypt_timezone).time())                               
    class Meta:
        managed = False
        db_table = 'message'
        unique_together = (('user', 'message_id'),)


class Nurse(models.Model):
    nurse_id = models.IntegerField(primary_key=True)
    nurse_fname = models.CharField(db_column='nurse_Fname', max_length=64, blank=True, null=True) 
    nurse_lname = models.CharField(db_column='nurse_Lname', max_length=64, blank=True, null=True)  
    nurse_phone = models.CharField(max_length=64, blank=True, null=True)
    nurse_gender = models.CharField(max_length=64, blank=True, null=True)
    nurse_username = models.CharField(unique=True, max_length=64)
    nurse_gmail = models.CharField(unique=True, max_length=100)
    nurse_password = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'nurse'


class NurseAppointment(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE) 
    nurse = models.ForeignKey(Nurse, on_delete=models.CASCADE)
    appointment_status = models.CharField(max_length=64, blank=True, null=True,default='scheduled')
    appointment_date = models.DateField(blank=True, null=False, primary_key=True)
    appointment_time = models.TimeField(blank=True, null=False)
    illness_description = models.TextField(blank=True, null=True)
    appointment_address = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nurse_appointment'
        unique_together = (('appointment_date', 'appointment_time'),)


class Sanatorium(models.Model):
    sanatorium_id = models.IntegerField(primary_key=True)
    sanatorium_name = models.CharField(max_length=64, blank=True, null=True)
    sanatorium_phone = models.CharField(max_length=64, blank=True, null=True)
    sanatorium_street = models.CharField(max_length=64, blank=True, null=True)
    sanatorium_city = models.CharField(max_length=64, blank=True, null=True)
    sanatorium_username = models.CharField(unique=True, max_length=64)
    sanatorium_gmail = models.CharField(unique=True, max_length=100)
    sanatorium_password = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'sanatorium'


class SanatoriumAppointment(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE)  
    sanatorium = models.ForeignKey(Sanatorium, on_delete=models.CASCADE)
    appointment_status = models.CharField(max_length=64, blank=True, null=True,default='scheduled')
    appointment_date = models.DateField(blank=True, null=False, primary_key=True)
    appointment_time = models.TimeField(blank=True, null=False)
    illness_description = models.TextField(blank=True, null=True)
    appointment_address = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sanatorium_appointment'
        unique_together = (('appointment_date', 'appointment_time'),)


class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    user_fname = models.CharField(db_column='user_Fname', max_length=64, blank=True, null=True) 
    user_lname = models.CharField(db_column='user_Lname', max_length=64, blank=True, null=True)  
    user_ssn = models.CharField(db_column='user_SSN', max_length=64, blank=True, null=True)  
    user_birthdate = models.CharField(max_length=64, blank=True, null=True)
    user_phone = models.CharField(unique=True, max_length=64, blank=True, null=True)
    user_street = models.CharField(max_length=64, blank=True, null=True)
    user_city = models.CharField(max_length=64, blank=True, null=True)
    user_gender = models.CharField(max_length=64, blank=True, null=True)
    user_username = models.CharField(unique=True, max_length=64)
    user_gmail = models.CharField(unique=True, max_length=100)
    user_password = models.CharField(max_length=64)


    # def __str__(self):
    #     return self.user_id
    
    class Meta:
        db_table = 'user'
