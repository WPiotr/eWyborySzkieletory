from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.models import auth

def index(request):
    return render_to_response('views/index.html')

def register(request):
    return render_to_response('user/register.html')

def profile(request):
    return render_to_response('user/userProfile.html')

def electionView(request):
    return render_to_response('election/electionView.html')

def activeElections(request):
    return render_to_response('election/activeElectionsList.html')

def inactiveElections(request):
    return render_to_response('election/inactiveElectionsList.html')

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
                
    return render_to_response('/', {'local': locals()})
    
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)                              
        if user is not None and user.is_active:
            auth.login(request, user)
            return render_to_response('/', {'local': locals()})
        else:
            request.session['bad_login'] = 1
            return render_to_response('aboutus/aboutus.html')
                       