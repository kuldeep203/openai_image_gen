# image_generator/models.py

from django.db import models


# imagegen/models.py

from django.db import models

class Image(models.Model):
    prompt = models.CharField(max_length=255)
    image_url = models.URLField()
    task_id = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.prompt



from django.db import models

# Create your models here.
