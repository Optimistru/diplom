from django.db import models

class ArchiveType(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name

class Archive(models.Model):
    type = models.ForeignKey(ArchiveType)
    name = models.CharField(max_length=200)
    prefix = models.CharField(max_length=200, blank=True)
    start_time = models.DateTimeField()
    finish_time = models.DateTimeField()

    def __str__(self):
        return self.name + ' / ' + self.start_time.strftime('%d/%m/%Y %H:%M') + ' -- ' + self.finish_time.strftime('%d/%m/%Y %H:%M')

