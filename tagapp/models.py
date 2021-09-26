from django.db import models
from django.contrib.auth.models import User

class TagModel(models.Model):
    title = models.CharField(max_length=30,unique=True)
    class Meta:
        db_table = 'tags'

class TagUser(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    auth_user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.OneToOneField(TagModel, on_delete=models.CASCADE)
    content = models.CharField(max_length=30, null=True)
    class Meta:
        db_table = 'tag_user'

   