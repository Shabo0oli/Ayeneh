from django.contrib import admin
from .models import *

# Register your models here.


admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Assessment)
admin.site.register(Parameter)
admin.site.register(Student)
admin.site.register(Result)


