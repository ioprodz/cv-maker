from django.db import models

class UserInfo(models.Model):
   fname  = models.CharField("First name", max_length=50)
   lname  = models.CharField("Last name", max_length=50)
   gender = models.CharField("Gender", max_length=50)
   birthday  = models.DateField('Date of Birthday', auto_now=False, auto_now_add=False)
   email  = models.EmailField("Email", max_length=254)
   phone  = models.CharField("Phone Number", max_length=254)
   
   @property
   def full_name(self):
      return f'{self.fname} {self.lname}'
   
   def __str__(self):
       return self.full_name
   
class JobInfo(models.Model):
   job_title      = models.CharField('Job Profile', max_length=50)
   years_of_exp   = models.IntegerField('Years of Experience')
   main_tech      = models.CharField("Main Technologies", max_length=256)
   second_tech    = models.CharField("Secondary Technologies", max_length=254)
   
   def __str__(self):
       return self.job_title
   
class Skills(models.Model):
   soft_skills    = models.CharField('Soft Skills', max_length=50) 
   team_exp       = models.CharField("Team Experience", max_length=50)
   methodologies  = models.CharField("Methodologies", max_length=50)
   
   def __str__(self):
       return self.soft_skills