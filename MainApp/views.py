from django.contrib.auth.views import logout
from django.contrib.auth.models import User, auth
from django.shortcuts import render_to_response, redirect
from MainApp.models import Elections
from models import Elections, electionsCandidate


def index(request):
    all_Elections = Elections.objects.all()
    elections = list()
    for election in all_Elections :
        if election.isActive() :
            elections.append(election)
    return render_to_response('views/index.html',{'local': locals(), 'elections': elections})

def aboutUs(request):
    all_Elections = Elections.objects.all()
    elections = list()
    for election in all_Elections :
        if election.isActive() :
            elections.append(election)
    return render_to_response('views/index.html',{'local': locals(), 'elections': elections})

def register(request):
    all_Elections = Elections.objects.all()
    elections = list()
    for election in all_Elections :
        if election.isActive() :
            elections.append(election)
    return render_to_response('user/register.html',{'local': locals(), 'elections': elections})

def profile(request):
    all_Elections = Elections.objects.all()
    elections = list()
    for election in all_Elections :
        if election.isActive() :
            elections.append(election)
    return render_to_response('user/userProfile.html',{'local': locals(), 'elections': elections})

def electionView(request):
    #ele_id = request.GET('eid')
    #cand_id = request.GET('cid')
    all_Elections = Elections.objects.all()
    elections = list()
    for election in all_Elections :
        if election.isActive() :
            elections.append(election)
    candidate_list = []
    ele = Elections.objects.get(id=1)
    elecand = electionsCandidate.objects.get(id=2)
    print elecand.elections.type
    temp = electionsCandidate.objects.all()
    for i in temp:
        if i.elections.id == ele.id:
            candidate_list.append(i)
    #ele = Elections.objects.get(id=int(ele_id))
    #cand = electionsCandidate.objects.get(id=int(cand_id))
    return render_to_response('election/electionView.html',{'local': locals(),'cand_list':candidate_list, 'election':ele, 'elections': elections})

def activeElections(request):
    all_Elections = Elections.objects.all()
    elections = list()
    for election in all_Elections :
        if election.isActive() :
            elections.append(election)
    return render_to_response('election/activeElectionsList.html',{'local': locals(), 'elections': elections})

def inactiveElections(request):
    all_Elections = Elections.objects.all()
    
    elections = list()
    for election in all_Elections :
        if election.isActive() :
            elections.append(election)
    
    inactive_elections = list()
    for election in all_Elections :
        if not election.isActive() :
            inactive_elections.append(election)
    return render_to_response('election/inactiveElectionsList.html',{'local': locals(), 'elections': elections, 'inactive_elections': inactive_elections})

def registerUser(request):
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
    
def login(request):
    all_Elections = Elections.objects.all()
    elections = list()
    for election in all_Elections :
        if election.isActive() :
            elections.append(election)
    if request.method == 'POST':
        username = request.POST['login']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)                              
        if user is not None and user.is_active:
            auth.login(request, user)
            return redirect('/')
        else:
            request.session['bad_login'] = 1
            return render_to_response('/views/aboutus.html',{'local': locals(), 'elections': elections})
                       