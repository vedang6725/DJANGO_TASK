from django.contrib import admin
from .models import User, Patient, Doctor
# Register your models here.

admin.site.register(User)
admin.site.register(Patient)
admin.site.register(Doctor)
