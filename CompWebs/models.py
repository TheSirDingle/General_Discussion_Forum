
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField




# to make the migration do "python manage.py makemigrations CompWebs" (basically python manage.py makemigrations <homefolder>)
# to check what sql is going to execute inside the database do "python manage.py sqlmigrate CompWebs 0001"
# basically (python manage.py sqlmigrate <homefolder> <migrations py file first 4 numbers)
# Finally to add the new information/tables to the database run "python manage.py migrate"


class GamingTopic(models.Model):
    T_Title = models.CharField(max_length=250)
    Tdate_Created = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return self.T_Title


class GamingPost(models.Model):
    Post_Topic = models.ForeignKey(GamingTopic, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    Pdate_Created = models.DateTimeField()
    # Post_Content = models.CharField(max_length=99999 ,default="stuffman")
    Post_Content = RichTextField(blank=True, null=True)







