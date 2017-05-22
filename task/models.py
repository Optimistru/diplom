from django.db import models
from contest import models as from_contest

class Problem(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(default='')

    def __str__(self):
        return self.name + ' (' + self.description + ')'

class ProblemModification(models.Model):
    name = models.CharField(max_length=200)
    problem = models.ForeignKey(Problem)
    archive = models.ForeignKey(from_contest.Archive)
    prefix = models.CharField(max_length=200, blank=True)
    comment = models.TextField()

    def __str__(self):
        return self.name + ' --- мод. ' + str(self.problem)

class AttachmentType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Attachment(models.Model):
    problem = models.ForeignKey(Problem, blank=True)
    problem_modification = models.ForeignKey(ProblemModification, blank=True)
    type = models.ForeignKey(AttachmentType)
    contents = models.FileField() #is Binaryfield??
    comment = models.TextField()



