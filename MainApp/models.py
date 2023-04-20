from django.db import models

langs = (
    ('cpp', 'C++'),
    ('py', 'python'),
    ('js', 'javascript')
)



class Snippet(models.Model):
    name = models.CharField(max_length=100)
    lang = models.CharField(max_length=30, choices=langs)
    code = models.TextField(max_length=5000)
    creation_date = models.DateTimeField(auto_now=True)
