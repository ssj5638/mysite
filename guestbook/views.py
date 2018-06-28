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


def deleteform(request):
    print(request)
    id_value = request.GET.get('id')
    context = {'id_value':id_value}
    return render(request, 'guestbook/deleteform.html', context)

def delete(request):
    id_value = request.POST.get('no')
    pw_input = request.POST.get('password')
    Guestbook.objects.filter(id=id_value).filter(password=pw_input).delete()

    return HttpResponseRedirect('/guestbook')
