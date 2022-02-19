from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # auth_token = models.CharFeild(max_length = 100, )
    id = models.CharField(max_length = 20, primary_key = True)
    dob = models.DateField()
    gender = models.CharField(max_length = 7)
    mobile_number = models.BigIntegerField()
    isStudent = models.BooleanField()
    isCreator = models.BooleanField()
    isApprover = models.BooleanField()

    def _str_(self):
        return self.user.username
    
