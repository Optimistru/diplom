from django.db import models
from contest import models as from_contest

class User(models.Model):
    name = models.CharField(max_length=200, verbose_name=u"Имя / название")
    is_team = models.BooleanField(verbose_name=u"Является командой" )


    def __str__(self):
        return self.name + ('', ' (Team)')[self.is_team == True]

class TeamMember(models.Model):
    user = models.ForeignKey(User, related_name='which_user')    #id участника (Users)
    team = models.ForeignKey(User, related_name='in_what_team')  #id команды (Users)

class ParticipationType(models.Model):
    name = models.CharField(max_length=200)

class UsersInStanding(models.Model):
    contest = models.ForeignKey(from_contest.Archive)
    user = models.ForeignKey(User)
    participation_type = models.ForeignKey(ParticipationType)
    start_time = models.DateTimeField()



