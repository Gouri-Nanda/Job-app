from django.db import models

# Create your models here.

def user_directory_path(instance, filename):
    
    return '{0}/{1}'.format("company_logo",filename)
def user_directory_path2(instance, filename):
    
    return '{0}/{1}'.format("applications",filename)

class job_data(models.Model):
    job_Id = models.AutoField(primary_key=True)
    job_position = models.CharField(max_length=100, blank=False, null=False )
    job_company = models.CharField(max_length=100, blank=False, null=False )
    job_location = models.CharField(max_length=100, blank=False, null=False )
    job_salary = models.IntegerField(max_length=15, blank=False, null=False)
    company_logo = models.FileField(upload_to=user_directory_path, null=True, verbose_name="")

    class Meta:
        db_table = 'job' 


class application_data(models.Model):
    
    cand_Id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False, null=False )
    email = models.CharField(max_length=100, blank=False, null=False )
    phone = models.CharField(max_length=100, blank=False, null=False )
    resume = models.FileField(upload_to=user_directory_path2, null=True, verbose_name="")
    

    class Meta:
        db_table = 'applications'