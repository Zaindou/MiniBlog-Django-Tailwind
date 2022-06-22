from django.db import models

class Post(models.Model):
        title = models.CharField(max_length=20)
        content = models.TextField(max_length=300)

            
        def __str__(self):
            return self.title
    

