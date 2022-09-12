from tabnanny import verbose
from django.db import models
from accounts.models import User

# Create your models here.

class WebWayText(models.Model):
    name=models.CharField(max_length=100,primary_key=True)
    describtion=models.TextField(config_name='awesome_ckeditor')
    place=models.CharField(max_length=100)
    created_time=models.DateTimeField(auto_now_add=True)
    updated=models.DateField(auto_now=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE,related_name='twebimage')

    class Meta:
        ordering=('name',)
        


    def __str__(self) -> str:
        return self.name

class WebWayImages(models.Model):
    tag=models.ForeignKey(WebWayText, on_delete=models.CASCADE,related_name='tagwebimage',)
    name=models.CharField(max_length=100)
    image=models.ImageField()
    created_time=models.DateTimeField(auto_now_Add=True)
    updated=models.DateTimeField(auto_now=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE,related_name='uwebimage')


    class Meta:
        ordering=('tag')

    def __str__(self) -> str:
        return self.tag

   



