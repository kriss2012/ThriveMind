from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from datetime import date
from django.utils import timezone
from datetime import datetime, timedelta


# Create your models here.

class Therapist(models.Model):
    name = models.CharField(max_length=20)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    contact = models.CharField(validators=[phone_regex], max_length=17,blank=True) 
    region=models.CharField(max_length=30,default='online')
    def __unicode__(self):
        return self.name
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Added on_delete argument
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', 
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    age = models.IntegerField()
    region = models.CharField(max_length=30)
    def __unicode__(self):
        return self.user.username
    def get_region(self):
        return self.region

from django.db import models
from django.contrib.auth.models import User

class CBT_therapy(models.Model):
    """
    CBT_therapy: 
    - Has a one-to-one relationship with user and therapist.
    - Many-to-one relationship with weekly sessions.
    """
    start_date = models.DateField()
    session_time = models.TimeField()
    therapist = models.ForeignKey('Therapist', on_delete=models.CASCADE)  # Added on_delete
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('therapist', 'user'),)

from django.db import models
from datetime import date, timedelta
from django.utils import timezone

class WeeklySession(models.Model):
    session_date = models.DateField()
    session_time = models.TimeField()
    week_no = models.IntegerField()
    challenge = models.CharField(max_length=150)
    therapy = models.ForeignKey('CBT_therapy', on_delete=models.CASCADE)  # Added on_delete

    def is_past_due(self):
        """Check if the session date is past due."""
        return date.today() > self.session_date

    def start_session(self):
        """Check if the current time is within the session window (session_time and 2 hours after)."""
        current_date = date.today()
        current_time = timezone.now().time()

        if current_date == self.session_date:
            session_end_time = (datetime.combine(self.session_date, self.session_time) + timedelta(hours=2)).time()

            if self.session_time <= current_time <= session_end_time:
                return True
        return False

class Challenge(models.Model):
    title=models.CharField(max_length=150)
    def __unicode__(self):
        return self.title
    