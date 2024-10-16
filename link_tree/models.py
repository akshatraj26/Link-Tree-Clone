from django.db import models

class Profile(models.Model):
    BG_CHOICE = (
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('yellow', 'Yellow'),
        
    )
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    bg_color = models.CharField(max_length=50, choices=BG_CHOICE)

    def __str__(self):
        return self.name


class Link(models.Model):
    # text, url, profile
    name = models.CharField(max_length=100)
    url = models.URLField()
    profile = models.ForeignKey(to=Profile, on_delete=models.CASCADE, related_name="links")

    def __str__(self):
        return f"{self.name} | {self.url}"
    

