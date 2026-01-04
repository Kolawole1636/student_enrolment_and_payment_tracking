from django.contrib import admin

# Register your models here.

from .models import Course, Student, Payment, Staff, PaymentTrack

admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Payment)
admin.site.register(Staff)
admin.site.register(PaymentTrack)
