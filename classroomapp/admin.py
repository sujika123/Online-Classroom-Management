from django.contrib import admin

from classroomapp import models

# Register your models here.
admin.site.register(models.Login)
admin.site.register(models.teacherlogin)
admin.site.register(models.courseadd)
admin.site.register(models.studentadd)
admin.site.register(models.notificationadd)
admin.site.register(models.stdleaveshedule)
admin.site.register(models.tchrleaveshedule)
admin.site.register(models.StdntComplaint)
admin.site.register(models.TchrComplaint)
admin.site.register(models.Question)