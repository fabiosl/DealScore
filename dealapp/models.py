from django.db import models
from django.contrib import admin

# Create your models here.


class Category(models.Model):
    verbose_name_plural = "stories"
    name = models.CharField(max_length=20);
    class Meta:
        verbose_name_plural = "Categories"
 
    def __unicode__(self):
        return self.name;

class Deal(models.Model):
    code = models.IntegerField();
    categories = models.ManyToManyField(Category) 
    business_name = models.CharField(max_length=30);
    location = models.CharField(max_length=30);
    description = models.CharField(max_length=60);  
    price = models.IntegerField();
    deadline = models.DateField();
    picture_url = models.CharField(max_length=400);
    
    positive_votes = models.IntegerField();
    negative_votes = models.IntegerField();
    
    def save(self):
        if(len(Deal.objects.all()) == 0):
            self.code = 1;
        elif self.code>0 : 
            pass;
        else:
            self.code = len(Deal.objects.all()) + 1
            
        super(Deal, self).save()
    
    def __unicode__(self):
        return self.business_name+ ": " + self.description;

admin.site.register(Category)
admin.site.register(Deal)
