from django.db import models


# Create your models here.
class Charityinformation(models.Model):
    charity_name = models.CharField(max_length=200)
    street_name = models.CharField(max_length=200)
    post_code = models.CharField(max_length=20)
    district_name = models.CharField(max_length=120)
    contact_number = models.CharField(max_length=15)
    extra_info = models.CharField(max_length=200)

    class Meta:
        db_table = "charityinfo"
