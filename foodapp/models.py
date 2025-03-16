from django.db import models

# Create your models here.
from django.db import models
# Create your tests here.
class Dish(models.Model):
    id = models.AutoField(primary_key=True)
    dish_name=models.CharField(max_length=200)
    dish_desc=models.CharField(max_length=500)
    dish_recipe=models.CharField(max_length=1000)
    dish_type=models.CharField(max_length=50)
    dish_image=models.ImageField(upload_to='dishes/', blank=True, null=True)

    def __str__(self):
        return self.dish_name
    