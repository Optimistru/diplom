from django.contrib.auth.models import User
from django.db import models
from contest import models as from_contest


class Company(models.Model):
    user = models.OneToOneField(User)
    is_company = models.BooleanField(verbose_name="Является компанией")

    def __str__(self):
        return self.user.username + ['', ' (компания)'][self.is_company == True]

class Problem(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(default='')
    author = models.ForeignKey(Company, related_name='p_author', blank=True, null=True)

    def __str__(self):
        return self.name + ' (' + self.description + ')'

class ProblemModification(models.Model):
    name = models.CharField(max_length=200)
    problem = models.ForeignKey(Problem, related_name='modification')
    archives = models.ManyToManyField(from_contest.Archive, related_name='archive')
    prefix = models.CharField(max_length=200, blank=True)
    comment = models.TextField()
    author = models.ForeignKey(Company, related_name='pm_author', blank=True, null=True)

    def __str__(self):
        return self.name + ' --- мод. ' + str(self.problem)


class AttachmentType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Attachment(models.Model):
    problem = models.ForeignKey(Problem, blank=True, null=True, on_delete=models.CASCADE)
    problem_modification = models.ForeignKey(ProblemModification, blank=True, null=True, on_delete=models.CASCADE)
    type = models.ForeignKey(AttachmentType)
    contents = models.FileField(upload_to="files/media", blank=True) #or Binaryfield
    text = models.TextField(blank=True)


class Tag(models.Model):
    name = models.CharField(max_length=200)
    coeff = models.FloatField(default=1.0)
    problem = models.ManyToManyField(Problem, through='TagProblem', blank=True)
    problem_modification = models.ManyToManyField(ProblemModification, through='TagProblem', blank=True)

    def __str__(self):
        return self.name


class TagProblem(models.Model):
    tag = models.ForeignKey(Tag)
    problem = models.ForeignKey(Problem)
    problem_modification = models.ForeignKey(ProblemModification)
    weight = models.IntegerField()


