from django.db import models

# Create your models here.

from django.db import models

from django.utils.crypto import get_random_string

class Service(models.Model):
    service_id = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='service_images/')

    def save(self, *args, **kwargs):
        if not self.service_id:
            self.service_id = get_random_string(length=10)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
# models.py
class Project(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    client = models.CharField(max_length=255)
    done_date = models.DateField()

    def __str__(self):
        return self.title

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='project_images/')

    def __str__(self):
        return f"Image for {self.project.title}"



class CarouselSlide(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='carousel_images/')

    def __str__(self):
        return self.title
    
class Appointment(models.Model):
    Customer_name = models.CharField(max_length=255)
    Customer_email = models.EmailField()
    mobile_number = models.CharField(max_length=15)
    service_type = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return f"Appointment for {self.Customer_name}"