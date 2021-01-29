from django.db import models


class Record(models.Model):
    """
        Model schema for `Record`
    """

    link = models.URLField(max_length=1000)
    site = models.CharField(max_length=2)
    price = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return f'<site: "{self.site}", email:"{self.email}">'