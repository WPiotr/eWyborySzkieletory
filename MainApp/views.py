from django.shortcuts import render_to_response

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

