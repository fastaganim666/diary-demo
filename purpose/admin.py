from django.contrib import admin
from .models import *


admin.site.register(Purpose)
admin.site.register(Step)
admin.site.register(Constraint)
admin.site.register(Skill)
admin.site.register(Question)
admin.site.register(Comment)