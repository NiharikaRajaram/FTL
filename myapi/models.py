from django.db import models
from timezone_field import TimeZoneField

# A database of the members
class Member(models.Model):
   mid = models.CharField(max_length=12)
   real_name = models.CharField(max_length=60)
   tz = TimeZoneField(default='Europe/London')

# Database of activity periods of members with Member as foreign key
class Period(models.Model):
   member = models.ForeignKey(Member, on_delete=models.CASCADE)
   start = models.DateTimeField()
   end = models.DateTimeField()


