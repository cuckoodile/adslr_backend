from django.db import models
from django.contrib.auth.models import User

# Create your models here.

gender_options = [("Male", "Male"), ("Female", "Female")]
contact_options = [("Gmail", "Gmail"), ("Phone Number", "Phone Number"), ("Facebook Link", "Facebook Link")]

class Profile(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, null=True, blank=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=gender_options)

    user = models.OneToOneField(User, verbose_name='user', on_delete=models.CASCADE,  related_name='profile')


class Address(models.Model):
    province = models.CharField(max_length=50)
    municipality = models.CharField(max_length=50)
    barangay = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    house_number = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=10)

    profile = models.ForeignKey(Profile, verbose_name='profile', on_delete=models.CASCADE,  related_name='address')


class Contact(models.Model):
    type = models.CharField(max_length=15, choices=contact_options)
    value = models.CharField(max_length=30)

    profile = models.ForeignKey(Profile, verbose_name='profile', on_delete=models.CASCADE, related_name='contact')


class Student(models.Model):
    birthplace = models.CharField(max_length=100, null=True, blank=True)
    religion = models.CharField(max_length=50, null=True, blank=True)

    profile = models.OneToOneField(Profile, verbose_name='profile', on_delete=models.CASCADE, related_name='student')


class Guardian(models.Model):
    occupation = models.CharField(max_length=30)
    
    profile = models.OneToOneField(Profile, verbose_name='profile', on_delete=models.CASCADE, related_name='guardian')
    children = models.ManyToManyField(Student, verbose_name='children', related_name='guardian')


class Parent(models.Model):
    occupation = models.CharField(max_length=30)
    
    profile = models.OneToOneField(Profile, verbose_name='profile', on_delete=models.CASCADE, related_name='parent')
    children = models.ManyToManyField(Student, verbose_name='children', related_name='parent')