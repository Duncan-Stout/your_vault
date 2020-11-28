from django.db import models

# Create your models here.
class V_item(models.Model):
    description = models.CharField(max_length=50)
    my_file = models.FileField(upload_to='images/')
    stocked_date = models.DateTimeField(auto_now_add= True)


    def __str__(self):
        return self.description

