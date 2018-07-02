from django.shortcuts import render
from board.models import Board
from django.http import HttpResponseRedirect
from user.models import User

# Create your views here.


def list(request):
    board_list = Board.objects.all().order_by('-regdate')   # DB에 있는 board 테이블
    context = {'board_list': board_list}
    # print(context)
    return render(request, 'board/list.html', context)


def writeform(request):
    user = request.session['authuser']          # 로그인된 사용자의 정보
    userinfo = {'user': user}

    return render(request, 'board/write.html', userinfo)

def write(request):
    if request.session['authuser'] is not None:
        user_id = request.POST.get('user_id')
        board = Board()
        board.title = request.POST['title']
        board.message = request.POST['content']
        board.user = User.objects.get(id=user_id)

        board.save()

    return HttpResponseRedirect('/board')


def delete(request):
    Board.objects.filter(id=request.GET['id']).filter(user_id=request.session['authuser'].get('id')).delete()
    return HttpResponseRedirect('/board')


def view(request):
    board = Board.objects.filter(id=request.GET['id'])[0]
    context = {'board':board}
    return render(request, 'board/view.html',context)


def modifyform(request):
    board = Board.objects.filter(id=request.GET['id'])[0]
    context = {'board':board}

    return render(request, 'board/modify.html', context)


def modify(request):
    board = Board.objects.filter(id=request.POST['id'])[0]
    user_id = request.session['authuser']['id']
    board.title = request.POST['title']
    board.message = request.POST['content']
    board.user = User.objects.get(id=user_id)

    board.save()
    return HttpResponseRedirect('/board/view?id='+request.POST['id'])

def search(request):
    # print(request)
    # s_text = request.POST['kwd']
    # if s_text in Board.objects[0]:
    #     board_list = Board.objects.all().order_by('-regdate')
    #     context = {'board_list': board_list}
    # return HttpResponseRedirect('/board', context)
    pass