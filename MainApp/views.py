from MainApp.models import Elections
from _threading_local import local
from django.contrib.auth.models import User, auth
from django.contrib.auth.views import logout
from django.shortcuts import render_to_response, redirect
from django.utils.timezone import utc
from models import Elections, electionsCandidate
import datetime
import sys

def index(request):
    elections = getActiveElections()
    return render_to_response('views/index.html',{'local': locals(), 'elections': elections})

def aboutUs(request):
    elections = getActiveElections()
    return render_to_response('views/aboutUs.html',{'local': locals(), 'elections': elections})

def register(request):
    elections = getActiveElections()
    return render_to_response('user/register.html',{'local': locals(), 'elections': elections})

def profile(request):
    elections = getActiveElections()
    return render_to_response('user/userProfile.html',{'local': locals(), 'elections': elections})



def electionView(request, election):
    elections = getActiveElections()
    ele_id = election
    ele = Elections.objects.filter(id=ele_id)
    
    candidate_list = electionsCandidate.objects.filter(elections=ele_id)
    election = ele[0]
    u = request.user
    if(election.canVote(u)):
        return render_to_response('election/electionVote.html',{'local': locals(),'cand_list':candidate_list, 'election':election, 'elections': elections, 'user': u})
    chartList = dict()
    for cand in candidate_list :
        chartList[cand.candidate.user.first_name + " " + cand.candidate.user.last_name] = cand.voteCount
    library = { 
               "backgroundColor": "#c7d9c3",
               "legend": {"position": "top"},
               }
    return render_to_response('election/electionView.html',{'local': locals(),'cand_list':candidate_list, 'election':ele, 'elections': elections, 'chartList': chartList, 'library': library,})

def activeElections(request):
    elections = getActiveElections()
    return render_to_response('election/activeElectionsList.html',{'local': locals(), 'elections': elections})

def inactiveElections(request):
    elections = getActiveElections()
    inactive_elections = getInActiveElections()
    return render_to_response('election/inactiveElectionsList.html',{'local': locals(), 'elections': elections, 'inactive_elections': inactive_elections})

def registerUser(request):
    elections = getActiveElections()
    if request.method == 'POST':
        if request.POST['password'] == request.POST['secPassword']:
            if request.POST['email'] == request.POST['secEmail']:
                user = User.objects.create_user(username=request.POST['userName'], email=request.POST['email'], password=request.POST['password'])
                user.first_name = request.POST['firstName']
                user.last_name = request.POST['lastName']
                user.save()
                user = auth.authenticate(username=request.POST['userName'], password=request.POST['password'])
                auth.login(request, user)
    return redirect('/')

def electionVote(request):
    elections = getActiveElections()
    current_user = request.user
    checkedList = request.POST.getlist('candidate_id')
    election_unicode = request.POST['ele']
    election = elections[0]
    for e in elections:
        if e.__unicode__ == election_unicode:
            election = e
    for checked in checkedList:
        print checked
        Elections.vote(election, current_user, checked)
    return redirect('/')

def login(request):
    elections = getActiveElections()
    if request.method == 'POST':
        username = request.POST['login']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)                              
        if user is not None and user.is_active:
            auth.login(request, user)
            return redirect('/')
        else:
            request.session['bad_login'] = 1
            return render_to_response('views/aboutUs.html',{'local': locals(), 'elections': elections})

def editProfile(request):
    elections = getActiveElections()
    user = request.user
    user.username = request.POST['login']
    user.first_name = request.POST['firstName']
    user.last_name = request.POST['lastName']
    user.email = request.POST['email']
    if request.POST['password'] is not None and request.POST['password'] == request.POST['secPassword']:
        user.set_password(str(request.POST['password']))
    if user.email == request.POST['oldEmail']:
        if request.POST['email'] is not None and request.POST['email'] == request.POST['secEmail']:
            user.email = request.POST['email']
    user.save()
    return redirect('/user/profile/',{'local': locals(), 'elections': elections})

def getActiveElections():
    now = datetime.datetime.utcnow().replace(tzinfo=utc)
    elections = Elections.objects.extra(where=['end_elections>%s', 'start_elections<%s'], params=[now,now])
    return elections

def getInActiveElections():
    now = datetime.datetime.utcnow().replace(tzinfo=utc)
    elections = Elections.objects.extra(where=['end_elections<%s', 'start_elections>%s'], params=[now,now])
    return elections
