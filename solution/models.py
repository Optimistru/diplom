from django.db import models
from task import models as from_task
from users import models as from_users

class SolutionVerdict(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class SolutionLanguage(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Solution(models.Model):
    problem_modification = models.ForeignKey(from_task.ProblemModification)
    author = models.ForeignKey(from_users.User)
    verdict = models.ForeignKey(SolutionVerdict)
    show_in_standings = models.BooleanField()
    language = models.ForeignKey(SolutionLanguage)
    code = models.FileField() #or BinaryField()
    time = models.DateTimeField()
    comment = models.TextField(blank=True)

    def __str__(self):
        return 'Решение участника ' + str(self.author) + ' на ' + str(self.language) + ' // ' + str(self.comment)

