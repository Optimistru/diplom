from django.db import models
from contest import models as from_contest

class User(models.Model):
    is_team = models.BooleanField()
    name = models.TextField()

    def __str__(self):
        return self.name + ('', ' (Team)')[self.is_team == True]

class TeamMember(models.Model):
    user = models.ForeignKey(User)
    team = models.ForeignKey(User)  #its not a bug

class ParticipationType(models.Model):
    name = models.CharField(max_length=200)

class UsersInStanding(models.Model):
    contest = models.ForeignKey(from_contest.Archive)
    user = models.ForeignKey(User)
    participation_type = models.ForeignKey(ParticipationType)
    start_time = models.DateTimeField()



