from django.shortcuts import render, get_object_or_404


from .models import *

def index(request):
    ip_user = request.META.get('REMOTE_ADDR', None)

    profile, created = Profile.objects.get_or_create(name="Default Profile")

    if request.method == 'POST' and 'like' in request.POST:
        profile.process_like(ip_user)

    profi = Profile.objects.all()

    return render(request, 'index.html', {'profile': profile, 'ip_user': ip_user, 'profi':profi})