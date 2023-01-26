from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from app.models import CustomUser, AdminHOD, Courses, Staffs, Subjects, Students


class UserModel(UserAdmin):
    pass


admin.site.register(CustomUser, UserModel)
admin.site.register(AdminHOD)
admin.site.register(Courses)
admin.site.register(Staffs)
admin.site.register(Subjects)
admin.site.register(Students)
