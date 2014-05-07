from MainApp.models import *
from django.contrib import admin

admin.site.register(User)
admin.site.register(Elections)
admin.site.register(Candidate)
admin.site.register(UserVote)
admin.site.register(electionsCandidate)