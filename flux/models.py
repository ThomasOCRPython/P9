
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings
from django.db import models
from PIL import Image



class Ticket(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField(max_length=2048, blank=True, null=True)
    image = models.ImageField(null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    starred = models.BooleanField(default=False)
    
    IMAGE_MAX_SIZE = (200, 200)
    
    def resize_image(self):
        image = Image.open(self.image)
        image.thumbnail(self.IMAGE_MAX_SIZE)

        image.save(self.image.path)

    def save(self, *args, **kwargs):
    
        super().save(*args, **kwargs)
        if self.image:
            self.resize_image()

    
class Review(models.Model):
    ticket = models.ForeignKey(Ticket, related_name="reviews_set" ,on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)])
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    headline = models.CharField(max_length=128)
    body = models.TextField(max_length=8192, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    



        

    

    

    
    
    