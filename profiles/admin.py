from django.contrib import admin
from .models import Profile, Address, Contact, Student, Guardian, Parent


# Register your models here.

admin.site.register(Profile)
admin.site.register(Address)
admin.site.register(Contact)
admin.site.register(Student)
admin.site.register(Guardian)
admin.site.register(Parent)