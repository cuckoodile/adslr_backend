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

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.user.username})"


class Address(models.Model):
    province = models.CharField(max_length=50)
    municipality = models.CharField(max_length=50)
    barangay = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    house_number = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=10)

    profile = models.ForeignKey(Profile, verbose_name='profile', on_delete=models.CASCADE,  related_name='address')

    def __str__(self):
        return f"{self.street}, {self.barangay}, {self.municipality}, {self.province} ({self.postal_code}) - ({self.profile.user.username})"


class Contact(models.Model):
    type = models.CharField(max_length=15, choices=contact_options)
    value = models.CharField(max_length=30)

    profile = models.ForeignKey(Profile, verbose_name='profile', on_delete=models.CASCADE, related_name='contact')

    def __str__(self):
        return f"{self.type}: {self.value} ({self.profile.user.username})"


class Student(models.Model):
    birthplace = models.CharField(max_length=100, null=True, blank=True)
    religion = models.CharField(max_length=50, null=True, blank=True)

    profile = models.OneToOneField(Profile, verbose_name='profile', on_delete=models.CASCADE, related_name='student')

    def __str__(self):
        return f"{self.profile.first_name} {self.profile.last_name} ({self.profile.user.username})"


class Guardian(models.Model):
    occupation = models.CharField(max_length=30)
    relationship = models.CharField(max_length=30, null=True, blank=True)
    
    profile = models.OneToOneField(Profile, verbose_name='profile', on_delete=models.CASCADE, related_name='guardian')
    children = models.ManyToManyField(Student, verbose_name='children', related_name='guardian')

    def __str__(self):
        return f"{self.profile.first_name} {self.profile.last_name} ({self.profile.user.username}) - Guardian of {self.children.first().profile.first_name} {self.children.first().profile.last_name}"


class Parent(models.Model):
    occupation = models.CharField(max_length=30)
    
    profile = models.OneToOneField(Profile, verbose_name='profile', on_delete=models.CASCADE, related_name='parent')
    children = models.ManyToManyField(Student, verbose_name='children', related_name='parent')

    def __str__(self):
        return f"{self.profile.first_name} {self.profile.last_name} ({self.profile.user.username}) - Parent"