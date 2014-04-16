from django.db import models

class User (models.Model):
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    login = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    
class Elections (models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    userID = models.ForeignKey(User)
    allowedVotes = models.IntegerField()
    startElections = models.DateField()
    endElections = models.DateField()

class Candidate(models.Model):
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    
class UserVote(models.Model):
    userID = models.ForeignKey(User)
    voted = models.BooleanField()
    allowed = models.BooleanField()
    electionsID = models.ForeignKey(Elections)
    
class electionsCandidate(models.Model):
    electionsID = models.ForeignKey(Elections)
    candidateID = models.ForeignKey(Candidate) 