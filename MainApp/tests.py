"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from MainApp.models import *

class ModelTests(TestCase):
    def vote(self):
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