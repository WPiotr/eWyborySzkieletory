from django.shortcuts import render_to_response

def index(request):
    local = locals();
    return render_to_response('views/index.html', {'local' : local})