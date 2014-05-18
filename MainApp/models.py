# -*- coding: UTF-8 -*-
from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils.timezone import utc

class Elections (models.Model):
    """
    Klasa reprezentująca wybory.
    Pola:
    @field: string name - Nazwa wyborów np. "Do samorządu, na przewodniczącego".
    @field: string typ - Typ np. "Samorządowe, parlamentarne"
    @field: list whitelist - lista userów, którzy mogą brać udział w wyborach w przypadku gdy whitelist_on jest true
    @field: bool whitelist_on - czy whitelist jest brana pod uwagę
    @field: int allowed_votes_count - ilość możliwych głosów do odadnia przez użytkownika w danych wyborach
    @field: dataTime start_elections - data i godzina rozpoczeńcia wyborów
    @field: dataTime start_elections - data i godzina zakończenia wyborów
    """
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    whitelist_on = models.BooleanField(default=False)
    whitelist = models.ManyToManyField(User, blank=True)
    allowed_votes_count = models.IntegerField()
    start_elections = models.DateTimeField()
    end_elections = models.DateTimeField()
    
    class Meta:
        ordering = ['start_elections']

    def __unicode__(self):
        return '%s' % (self.name)
    
    def isActive(self):
        """
        Sprawdza czy wybory sa aktywne
        @return: bool - false jeżeli wybory sie zakonczyly, true w przeciwnym wypadku
        """
        now = datetime.datetime.utcnow().replace(tzinfo=utc)
        if((self.end_elections - now).total_seconds() < 0):
            return False
        if((self.start_elections - now).total_seconds() > 0):
            return False
        return True
    
    
    def canVote(self, user):
        """
        Sprawdza czy użytkownika może brać udział w tych głosowaniach
        @param User user - sprawdzany użytkownik
        @return: bool - false jeżeli użytkownik nie może brać udział w głosowaniu, true w przeciwnym przypadku 
        """
        now = datetime.datetime.utcnow().replace(tzinfo=utc)
        if((self.end_elections - now).total_seconds() < 0):
            return False
        if((self.start_elections - now).total_seconds() > 0):
            return False
        if(self.whitelist_on):
            if(not self.whitelist.filter(id=user.id)):
                return False 
        if(UserVote.objects.filter(user=user).count() >= self.allowed_votes_count):
            return False
        return True
        
        
    def vote(self, user, candidate):
        """
        @user: User
        Użytkownik podany w parametrze głosuje na kandydata podanego w parametrze w bierzących wyborach
        @param User user - sprawdzany użytkownik 
        """
        if(not self.canVote(user)):
            raise Exception("Użytkownik nie może głosować w tych wyborach")
        if(UserVote.objects.filter(user=user, candidate=candidate).exists()):
            raise Exception("Użytkownik już głosował na tego kandydata w tych wyborach")
        user_vote = UserVote(user=user, elections=self, candidate=candidate, when=datetime.datetime.now())
        user_vote.save()
        return 0

    def getVoteCount(self,candidate):
        """
        @param User user - sprawdzany użytkownik
        @return int - liczbę głosów oddanych na kandydata w danych wyborach 
        """
        return UserVote.objects.filter(elections=self,candidate=candidate).count()


class Candidate(models.Model):
    
    user = models.ForeignKey(User) 
    
    class Meta:
        ordering = ['user']

    def __unicode__(self):
        return '%s %s' % (self.user.first_name, self.user.last_name)
    
    description = models.CharField(max_length=200)


class UserVote(models.Model):
    
    user = models.ForeignKey(User)
    elections = models.ForeignKey(Elections)
    candidate = models.ForeignKey(Candidate, related_name='candidates')
    when = models.DateTimeField()
    
    class Meta:
        ordering = ['elections', 'candidate']

    def __unicode__(self):
        return 'Wybory %s na %s. /n Użytkownik %s oddał głos na %s : %s.' \
    % (self.elections.type, self.elections.name, self.user.name, self.candidate, self.when)


class electionsCandidate(models.Model):
    
    elections = models.ForeignKey(Elections)
    candidate = models.ForeignKey(Candidate)
    voteCount = models.IntegerField()
    
    class Meta:
        ordering = ['elections']

    def __unicode__(self):
        return 'Wybory %s na %s. Kandydat %s ma %d głosów' \
            % (self.elections.type, self.elections.name, self.candidate, self.voteCount)
    