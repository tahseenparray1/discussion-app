from django.db import models
from django.contrib.auth.models import User

class Link(models.Model):
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=400)
    submitter = models.ForeignKey(User,related_name='links',on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    score = models.IntegerField(default=0)
    upvoters = models.ManyToManyField(User,related_name='upvoted',blank=True,null=True)
    downvoters = models.ManyToManyField(User,related_name='downvoted',blank=True,null=True)
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    text = models.TextField()
    submitter = models.ForeignKey(User,related_name='comments',on_delete=models.CASCADE)
    link = models.ForeignKey(Link,on_delete=models.CASCADE,related_name='comments')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    parent = models.ForeignKey('self',on_delete=models.SET_NULL,related_name='children',null=True,blank=True)
    def __str__(self):
        return f"{self.submitter}/{self.id}" # type: ignore

