from django.db import models

# Create your models here.
class Response(models.Model):
    generated_content = ((1,'Story'),(2,'Poem'))
    unique_id = models.CharField(max_length=1000)
    response_id = models.CharField(max_length=1000, null= True, blank=True)
    genated_content = models.CharField(max_length=50)
    story_text = models.TextField(null=True, blank=True)
    datetime = models.DateTimeField(auto_now_add=True)


class FormData(models.Model):    
    readers_age_choices = [
        ('Little Sprouts (Age 3 - 5) 🌱','3-5 years'),
        ('Young Adventurers (Age 6 - 8) 🌟','6-8 years'),
        ('Valiant Explorers (Age 9 - 12) 🗺️','9-12 years'),
        ('Teenage Trailblazers (Age 13 - 15) 🚀','13-15 years'),
        ('Timeless Tales for All (Age 16+) 🌍','16+ years'),]
    gender_choices = [
        ('Boy 🚶‍♂️','Boy'),
        ('Girl 🚶‍♀️','Girl'),
        ('Prefer not to specify 🌟','Prefer not to specify'),]
    unique_id = models.CharField(max_length=1000)
    response_id = models.CharField(max_length=1000, null= True, blank=True)
    readers_name= models.CharField(max_length=1000)
    story_format=models.CharField(max_length=1000)
    ebook_format=models.CharField(max_length=1000,null= True, blank=True)
    genre=models.CharField(max_length=1000)
    writing_style=models.CharField(max_length=1000)
    charcter_type=models.CharField(max_length=1000)
    charachter_name=models.CharField(max_length=1000)
    charcter_gender=models.CharField(max_length=1000, choices=gender_choices,null= True, blank=True)
    charachter_age=models.CharField(max_length=1000,null= True, blank=True)
    charachter_ethinicity=models.CharField(max_length=1000,null= True, blank=True)
    animal_type=models.CharField(max_length=1000,null= True, blank=True)
    readers_age_group=models.CharField(max_length=1000,choices=readers_age_choices)
    location=models.CharField(max_length=1000)
    moral=models.CharField(max_length=1000)
    audio_name=models.CharField(max_length=1000,null= True, blank=True)
    datetime = models.DateTimeField(auto_now_add=True)