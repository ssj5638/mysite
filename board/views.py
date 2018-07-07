from django.shortcuts import render
from board.models import Board
from django.http import HttpResponseRedirect
from user.models import User
from django.db.models import F

# Create your views here.


def list(request):
    board_list = Board.objects.all().order_by('-regdate')   # DB에 있는 board 테이블 list.html에서 확인
    context = {'board_list': board_list}
    # print(context)
    return render(request, 'board/list.html', context)


def writeform(request):
    user = request.session['authuser']
    userinfo = {'user': user}
    return render(request, 'board/write.html', userinfo)
    ''' HTML에서 가능하도록 바꿈    
    if request.GET['user'] != '':
        user = request.session['authuser']
        userinfo = {'user': user}
        return render(request, 'board/write.html', userinfo)
    else:
        return HttpResponseRedirect('/user/loginform')
        '''

def write(request):
    print(request.POST)
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
    print(board)
    context = {'board':board}
    print(request)
    try:                                # modify함수에서 넘어온 경우
        if request.GET['noHit'] == 1:
            pass
    except:                             # title을 클릭하여 호출한 경우
        Board.objects.filter(id=request.GET['id']).update(hit=F('hit') + 1)
        # 해당 값만 업데이트
        # 업데이트 호출은 F()객체를 사용하여 모델의 다른 필드 값을 기반으로 한 필드를 업데이트 할 수 있음

    return render(request, 'board/view.html',context)


def modifyform(request):
    board = Board.objects.filter(id=request.GET['id'])[0]
    context = {'board':board}

    return render(request, 'board/modify.html', context)


def modify(request):
    print(Board.objects.filter(id=request.POST['id']))
    board = Board.objects.filter(id=request.POST['id'])[0]
    print(board)
    user_id = request.session['authuser']['id']
    board.title = request.POST['title']
    board.message = request.POST['content']
    board.user = User.objects.get(id=user_id)

    board.save
    return HttpResponseRedirect('/board/view?id='+request.POST['id']+'&noHit=1')

def search(request):
    keyword = request.GET['kwd']

    board_list = Board.objects.filter(title__contains = keyword)

    print(board_list)
    context={'board_list': board_list}

    # return HttpResponseRedirect('/board', context)
    return render(request, 'board/list.html', context)