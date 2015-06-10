import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Temp(models.Model):
    temp_value = models.DecimalField('temperature', max_digits=5, decimal_places=2)
    
    time_measured = models.DateTimeField(default=timezone.now)
   
    def __str__(self):
        return str(self.temp_value)
        
    def was_measured_recently(self):
        return self.time_measured >= timezone.now() - datetime.timedelta(days=1)
    was_measured_recently.admin_order_field = 'time_measured'
    was_measured_recently.boolean = True
    was_measured_recently.short_description = 'Measured recently?'

    def __float__(self):
        return self.temp_value
        
    
