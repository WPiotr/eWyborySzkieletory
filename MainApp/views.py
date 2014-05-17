# -*- coding: UTF-8 -*-
from django.shortcuts import render_to_response
from MainApp.models import *
from django.contrib.auth.models import User
import sys
def index(request):
    return render_to_response('views/index.html')
def register(request):
    e = Elections.objects.filter(name='Test3')
    u1 = User.objects.filter(username='123')
    u2 = User.objects.filter(username='1234')
    c = Candidate.objects.filter()
    e = e[0]
    u1 = u1[0]
    u2 = u2[0]
    c = c[0]
    print >>sys.stderr, ' '+ str(e.getVoteCount(c))
    if(e.canVote(u1)):
        try:
            print >>sys.stderr, 'Użytkownik 1 stara się głosować!'
            e.vote(user=u1,candidate=c)
            print >>sys.stderr, 'Użytkownik 1 zagłosował!'
        except Exception as ex:
            print >>sys.stderr, 'Użytkownik 1 nie zagłosował bo!'
            print '%s' % (ex.message)
    else:
        print >>sys.stderr, 'Użytkownik 2 nie zagłosował bo tak!'
    if(e.canVote(u2)):
        try:
            print >>sys.stderr, 'Użytkownik 2 stara się głosować!'
            e.vote(user=u1,candidate=c)
            print >>sys.stderr, 'Użytkownik 2 zagłosował!'
        except Exception as ex:
            print >>sys.stderr, 'Użytkownik 2 nie zagłosował bo!'
            print '%s' % (ex.message)
    else:
        print >>sys.stderr, 'Użytkownik 2 nie zagłosował bo tak!'
    print >>sys.stderr, 'Goodbye, cruel world!'
    return render_to_response('user/register.html')

def profile(request):
    return render_to_response('user/userProfile.html')

def electionView(request):
    return render_to_response('election/electionView.html')

def activeElections(request):
    return render_to_response('election/activeElectionsList.html')

def inactiveElections(request):
    return render_to_response('election/inactiveElectionsList.html')

