from django.contrib import admin

from .models import ToDo
from .models import ToMeet
from .models import Goal_for_month
from .models import Habits



admin.site.register(ToDo)
admin.site.register(ToMeet)

admin.site.register(Goal_for_month)

admin.site.register(Habits)