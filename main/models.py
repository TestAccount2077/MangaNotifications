from django.db import models


class Subscriber(models.Model):
    
    email = models.EmailField()
    
    mangas = models.ManyToManyField('Manga', related_name='subscribers', blank=True)
    
    def __str__(self):
        
        return self.email


class Manga(models.Model):
    
    name = models.CharField(max_length=300, default='', blank=True)
    
    upcoming_chapter = models.IntegerField(default=1)
    
    url_pattern = models.CharField(max_length=500, default='', blank=True)
    
    def __str__(self):
        
        return self.name
    
    @property
    def url(self):
        
        if self.url_pattern:
            return self.url_pattern.format(chapter=self.upcoming_chapter)
        
        return ''
