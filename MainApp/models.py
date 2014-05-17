from django.db import models
from django.contrib.auth.models import User
    
class Elections (models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    whitelist = models.ManyToManyField(User)
    allowed_votes_count = models.IntegerField()
    start_elections = models.DateField()
    end_elections = models.DateField()

class Candidate(User):
    description = models.CharField(max_length=200)
    
class UserVote(models.Model):
    userID = models.ForeignKey(User)
    electionsID = models.ForeignKey(Elections)
    
class electionsCandidate(models.Model):
    electionsID = models.ForeignKey(Elections)
    candidateID = models.ForeignKey(Candidate)
    voteCount = models.IntegerField()