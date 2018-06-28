from django.shortcuts import render
from django.http import HttpResponseRedirect
from guestbook.models import Guestbook
# Create your views here.


def list(request):
    guestbook_lisk = Guestbook.objects.all().order_by('-regdate')
    context = {'guestbook_list':guestbook_lisk}

    return render(request, 'guestbook/list.html', context)


def add(request):
    guestbook = Guestbook()
    guestbook.name = request.POST['name']
    guestbook.password = request.POST['pass']
    guestbook.message = request.POST['content']

    guestbook.save()

    return HttpResponseRedirect('/guestbook')


def delete(request):
    return render(request, 'guestbook/deleteform.html')