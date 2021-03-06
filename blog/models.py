from django.db import models

class Post(models.Model):
        title = models.CharField(max_length=20)
        content = models.TextField(max_length=300)
        updated_on = models.DateTimeField(auto_now= True)
        created_on = models.DateTimeField(auto_now_add=True)

            
        def __str__(self):
            return self.title
        
        class Meta:
            ordering = ['-created_on']

