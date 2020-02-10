from django.db import models


# Aktualności widoczne na głównych kafelkach na stronie.
class Offer(models.Model):
    title = models.CharField(max_length=200)
    pubdate = models.DateTimeField(blank=True, null=True)  # Data widoczności w publikacji
    body = models.TextField()
    image = models.ImageField(upload_to='images', blank=True, null=True)
    maplink = models.CharField(max_length=500, blank=True, null=True)
    file1 = models.FileField(upload_to='docs', blank=True, null=True)
    file2 = models.FileField(upload_to='docs', blank=True, null=True)
    file3 = models.FileField(upload_to='docs', blank=True, null=True)
    file4 = models.FileField(upload_to='docs', blank=True, null=True)
    file5 = models.FileField(upload_to='docs', blank=True, null=True)
    file6 = models.FileField(upload_to='docs', blank=True, null=True)
    mapdraw = models.ImageField(upload_to='images', blank=True, null=True)

    class Meta:
        ordering = ['-pubdate']

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:150]

    def pubdate_short(self):
        return self.pubdate.strftime('%a %d %b %Y')


# Bardziej permanentne "ważne informacje" dla klientów.
class Info(models.Model):
    title = models.CharField(max_length=200)
    pubdate = models.DateTimeField(blank=True, null=True)  # Data widoczności w publikacji
    body = models.TextField()
    image = models.ImageField(upload_to='images', blank=True, null=True)

    class Meta:
        ordering = ['-pubdate']

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:150]

    def pubdate_short(self):
        return self.pubdate.strftime('%a %d %b %Y')


class Service(models.Model):
    title = models.CharField(max_length=200)
    pubdate = models.DateTimeField(blank=True, null=True)  # Data widoczności w publikacji
    body = models.TextField()
    image1 = models.ImageField(upload_to='images', blank=True, null=True)
    image2 = models.ImageField(upload_to='images', blank=True, null=True)
    image3 = models.ImageField(upload_to='images', blank=True, null=True)
    image4 = models.ImageField(upload_to='images', blank=True, null=True)
    image5 = models.ImageField(upload_to='images', blank=True, null=True)
    image6 = models.ImageField(upload_to='images', blank=True, null=True)
    gallery = models.BooleanField(default=False)  # czy wyświetlić obrazki?

    class Meta:
        ordering = ['-pubdate']

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:150]

    def pubdate_short(self):
        return self.pubdate.strftime('%a %d %b %Y')
