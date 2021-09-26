from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.



class KhojTheSearch(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    input_value = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username