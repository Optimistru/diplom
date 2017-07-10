from django.db import models

class ArchiveType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Archive(models.Model):
    type = models.ForeignKey(ArchiveType)
    name = models.CharField(max_length=200)
    prefix = models.CharField(max_length=200, blank=True)
    start_time = models.DateTimeField(null=True, blank=True)
    finish_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        if (self.start_time is None):
            return self.name
        else:
            return self.name + ' / ' + self.start_time.strftime('%d/%m/%Y') + ' -- ' \
                   + self.finish_time.strftime('%d/%m/%Y')

