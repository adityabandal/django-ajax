from django.db import models

# Create your models here.
class Friend(models.Model):
    # NICK NAME should be unique
    repo_name = models.CharField(max_length=100, unique =  True)
    repo_description = models.CharField(max_length=100)
    rep_lang = models.CharField(max_length=100)
    forks = models.CharField(max_length = 250)
    created_on = models.DateField(auto_now=False, auto_now_add=False)
    collaborators = models.CharField(max_length=150, null = True, blank = True)

    def __str__(self):
        return self.repo_name