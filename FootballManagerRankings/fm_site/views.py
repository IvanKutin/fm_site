from django.http import HttpResponse
from django.shortcuts import render
from .models import *

posts = Player.objects.all()
club = Club.objects.all()
k = 0
next = 0
prev = 0


def index(request):
    global posts, k
    posts1 = posts[0:10]
    if len(posts[10:20]) == 0:
        k = 0
        return render(request, 'fm_site/index1.html', {'posts': posts1})
    else:
        k = 0
        return render(request, 'fm_site/index2.html', {'posts': posts1})


def clubs(request):
    global club
    club1 = club[:10]
    return render(request, 'fm_site/clubs.html', {'club': club1})


def next_page(request):
    global posts, k
    k = k + 1
    if len(posts[(k + 1) * 10:(k + 2) * 20]) == 0:
        posts1 = posts[k * 10:(k + 1) * 10]
        return render(request, 'fm_site/index3.html', {'posts': posts1, 'Возраст': k})
    else:
        posts1 = posts[k * 10:(k + 1) * 10]
        return render(request, 'fm_site/index.html', {'posts': posts1})


def prev_page(request):
    global posts, k
    k -= 1
    if k == 0:
        posts1 = posts[k * 10:(k + 1) * 10]
        return render(request, 'fm_site/index2.html', {'posts': posts1})
    else:
        posts1 = posts[k * 10:(k + 1) * 10]
        return render(request, 'fm_site/index.html', {'posts': posts1})
