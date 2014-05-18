from django.contrib.auth.views import logout
from django.contrib.auth.models import User, auth
from django.shortcuts import render_to_response, redirect
from models import Elections, electionsCandidate


def index(request):
    return render_to_response('views/index.html',{'local': locals()})

def aboutUs(request):
    return render_to_response('views/aboutUs.html',{'local': locals()})

def register(request):
    return render_to_response('user/register.html',{'local': locals()})

def profile(request):
    return render_to_response('user/userProfile.html',{'local': locals()})

def electionView(request):
    #ele_id = request.GET('eid')
    #cand_id = request.GET('cid')
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
    return render_to_response('election/electionView.html',{'cand_list':candidate_list, 'election':ele})

def activeElections(request):
    return render_to_response('election/activeElectionsList.html',{'local': locals()})

def inactiveElections(request):
    return render_to_response('election/inactiveElectionsList.html',{'local': locals()})

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
    if request.method == 'POST':
        username = request.POST['login']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)                              
        if user is not None and user.is_active:
            auth.login(request, user)
            return redirect('/')
        else:
            request.session['bad_login'] = 1
            return render_to_response('/views/aboutus.html',{'local': locals()})
                       
