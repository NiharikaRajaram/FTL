from django.contrib import admin
from .models import Member
from .models import Period

#Register members and their activity periods with the admin site
admin.site.register(Member)
admin.site.register(Period)