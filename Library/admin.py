from django.contrib import admin
from .models import Course,Student,Borrowing,Mentor,Book

admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Mentor)
admin.site.register(Borrowing)
admin.site.register(Book)
# Register your models here.

